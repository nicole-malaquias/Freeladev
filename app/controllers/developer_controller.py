from dataclasses import asdict
from datetime import datetime

import psycopg2
import sqlalchemy
from app.configs.database import db
from app.exceptions.contractor_exceptions import EmailAlreadyRegisteredError
from app.exceptions.developer_exceptions import InvalidFormatToBirthdateError
from app.exceptions.invalid_email_exceptions import InvalidEmailError
from app.exceptions.invalid_field_create_developer_exceptions import \
    FieldCreateDeveloperError
from app.exceptions.invalid_field_update_developer_exceptions import \
    FieldUpdateDeveloperError
from app.exceptions.invalid_password_exceptions import InvalidPasswordError
from app.exceptions.tech_exceptions import TechNotFoundError
from app.exceptions.users_exceptions import UserNotFoundError
from app.models.contractor_model import ContractorModel
from app.models.developer_model import DeveloperModel
from app.models.developers_techs import DevelopersTechsModel
from app.models.tech_model import TechModel
from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required


def create_profile():

    try:

        data = request.json
        email_already_used_as_contractor = ContractorModel.query.filter_by(email=data['email']).first()
        
        if email_already_used_as_contractor:
            return {'Message': 'Email is already used as contractor, please use another one for your developer account.'}, 409
        
        verify_email = DeveloperModel.verify_pattern_email(data['email'])
        
        if not verify_email:
            raise InvalidEmailError(data)

        verify_password = DeveloperModel.verify_pattern_password(data['password'])
        
        if not verify_password:
            raise InvalidPasswordError(data)
        
        technologies = []
        
        if data.get('technologies'):
            
            technologies = data.pop('technologies')
        
        password_input = data.pop('password')
        
        new_dev = DeveloperModel(**data)
        new_dev.password = password_input

        db.session.add(new_dev)
        db.session.commit()
        
        
        technologies_not_avaliable = []
        avaliable_technologies = []
        developer_techs = []
        
        for tech in technologies:
            found_tech = TechModel.get_tech(tech['name'])
            
            if not found_tech:
                technologies_not_avaliable.append(tech['name'])
                
            else:
                developer_tech = DevelopersTechsModel(tech_id=found_tech.id, developer_id=new_dev.id)        
                developer_techs.append(developer_tech)
                
                avaliable_technologies.append(tech['name'])
                
        for developer_tech in developer_techs:
            DevelopersTechsModel.insert_developer_techs(developer_tech)
            
        new_dev.format_birthdate()

        if technologies_not_avaliable:
            raise TechNotFoundError(avaliable_technologies, technologies_not_avaliable)
        
        else:            
            return jsonify({**asdict(new_dev), 'technologies': [*avaliable_technologies]}), 201
 
    except InvalidEmailError as e:
        return jsonify(e.message), 406

    except InvalidPasswordError as e:
        return jsonify(e.message), 406
    
    except TechNotFoundError as e:        
        return jsonify({**asdict(new_dev), 'technologies': e.message}), 201
    
    except (KeyError, TypeError):
        e = FieldCreateDeveloperError()
        return jsonify(e.message), 406
    
    except sqlalchemy.exc.IntegrityError as e :
        
        if type(e.orig) == psycopg2.errors.NotNullViolation:
            return {'Message': 'Developer must be created with name, email, password and birthdate'}, 406
        
        if type(e.orig) ==  psycopg2.errors.UniqueViolation:
            return {'Message': 'Please use another email'}, 409     
    
    
@jwt_required()
def get_profile_info():
    user = get_jwt_identity()
    user["birthdate"] = user["birthdate"][6:16].split()

    if int(user["birthdate"][0]) < 10:
        user["birthdate"][0] = "0" + user["birthdate"][0]

    mounths = [
        ("Jan", "01"),
        ("Feb", "02"),
        ("Mar", "03"),
        ("Apr", "04"),
        ("May", "05"),
        ("Jun", "06"),
        ("Jul", "07"),
        ("Aug", "08"),
        ("Sep", "09"),
        ("Oct", "10"),
        ("Nov", "11"),
        ("Dec", "12"),
    ]

    for match in mounths:
        if match[0] == user["birthdate"][1]:
            user["birthdate"][1] = match[1]

    user["birthdate"] = "/".join(user["birthdate"])

    return user, 200



@jwt_required()
def update_profile_info():
     
    try:
        
        data = request.json
        
        technologies_not_avaliable = []
        avaliable_technologies = []
        developer_techs = []
        
        if 'birthdate' in data.keys():
            
            if not DeveloperModel.verify_birthdate_pattern(data['birthdate']):
                raise InvalidFormatToBirthdateError
            else : 
                data['birthdate'] = datetime.strptime(data['birthdate'], "%d/%m/%Y")

        if 'email' in data.keys():
        
            found_email = ContractorModel.query.filter_by(email=data['email']).first()
            
            if found_email:
                raise EmailAlreadyRegisteredError
            
            else: 
            
                if not DeveloperModel.verify_pattern_email(data['email']):
                    raise InvalidEmailError
                
        current_developer = get_jwt_identity()
        
        found_developer = DeveloperModel.query.filter_by(email=current_developer['email']).first()
        
        if 'password' in data.keys():
            
            if not ContractorModel.verify_pattern_password(data['password']):
                raise InvalidPasswordError(data)
            
            developer = DeveloperModel(password=data.pop('password'))
            
            data['password_hash'] = developer.password_hash
            
        if data.get('technologies'):
            DevelopersTechsModel.delete_developer_techs(found_developer.id)
            
            technologies = data.pop('technologies')
            
            for tech in technologies:
                found_tech = TechModel.get_tech(tech['name'])
                
                if not found_tech:
                    technologies_not_avaliable.append(tech['name'])
                
                else:                    
                    developer_tech = DevelopersTechsModel(tech_id=found_tech.id, developer_id=found_developer.id)
                                        
                    developer_techs.append(developer_tech)
                    
                    avaliable_technologies.append(tech['name'])
                
                
            for developer_tech in developer_techs:
                DevelopersTechsModel.insert_developer_techs(developer_tech)
                
        if data:
            DeveloperModel.query.filter_by(id=found_developer.id).update(data)
                
            db.session.commit()
                    
        rows = current_app.db.session.query(DeveloperModel, TechModel)\
                            .filter(DeveloperModel.id==DevelopersTechsModel.developer_id)\
                            .filter(TechModel.id==DevelopersTechsModel.tech_id)\
                            .where(DeveloperModel.id==found_developer.id)\
                            .all()
         
        if not rows:
            
            row = DeveloperModel.query.get(found_developer.id)
            
            developer = {**asdict(row), 'technologies': []}
            
        else: 
            developer = {**asdict(rows[0][0]), 'technologies': []}
            
        
            
        for row in rows:
            tech = asdict(row[1])
            developer['technologies'] = [*developer['technologies'], tech]
            
        developer['birthdate'] = datetime.strftime(developer['birthdate'], "%d/%m/%Y")
        
        if technologies_not_avaliable:
                raise TechNotFoundError(avaliable_technologies, technologies_not_avaliable)
            
        return jsonify(developer), 200
    

    except sqlalchemy.exc.IntegrityError as e:
        
        if type(e.orig) ==  psycopg2.errors.UniqueViolation:
            return {'Message': 'Please use another email'}, 400   

    except sqlalchemy.exc.StatementError as e:
        return {'message': 'You cannot send an empty list of the technologies'}, 400
    
    except InvalidEmailError as e:
        return jsonify(e.__dict__), 406
    
    except InvalidFormatToBirthdateError as e:
        return jsonify(e.__dict__), 406
    
    except TechNotFoundError as e:
        return jsonify({**developer, 'technologies': e.message}), 201
    
    except sqlalchemy.exc.InvalidRequestError as e:
        e = FieldUpdateDeveloperError()
        return jsonify(e.message), 406
    
    except EmailAlreadyRegisteredError as e:
        return {'message': str(e)}, 409
    
@jwt_required()
def delete_profile():
    current_developer = get_jwt_identity()
    
    try:
        found_developer = DeveloperModel.query.filter_by(email=current_developer['email']).first()
        if not found_developer:
            raise UserNotFoundError
        session = current_app.db.session

        session.delete(found_developer)
        session.commit()

        return '', 204
    
    except UserNotFoundError as e:
        return {'message': str(e)}, 404

def get_all_developers():
    rows = current_app.db.session.query(DeveloperModel, TechModel)\
                            .filter(DeveloperModel.id==DevelopersTechsModel.developer_id)\
                            .filter(TechModel.id==DevelopersTechsModel.tech_id)\
                            .all()
                       
    rows_with_devs_without_tech = current_app.db.session.query(DeveloperModel)\
                            .all()
    found_developers = []
    
    
    
    
    for index in range(len(rows)):
        
        developer = asdict(rows[index][0])
        
        developer['birthdate'] = datetime.strftime(developer['birthdate'], '%d/%m/%Y')
        
        tech = asdict(rows[index][1])

        if [found_developer for found_developer in found_developers if found_developer['email'] == developer['email']]:
            
            
            for found_developer in found_developers:
                
                if found_developer['email'] == developer['email']:
                    
                    found_developer['technologies'] = [*found_developer['technologies'],
                                                       { 'name': tech['name']}]
                    
        else:
            serialized_data = {**developer, 'technologies': [tech]}
    
            found_developers.append(serialized_data)
    
    
    for developer in rows_with_devs_without_tech:
        
        developer = asdict(developer)
        
        if not [found_developer for found_developer in found_developers if found_developer['email'] == developer['email']]:
            
            developer['birthdate'] = datetime.strftime(developer['birthdate'], '%d/%m/%Y')
            
            found_developers.append({**developer, 'technologies': []})
    
    return jsonify(found_developers), 200
