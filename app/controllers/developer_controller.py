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
        
        
        new_dev.format_birthdate()
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

        if technologies_not_avaliable:
            raise TechNotFoundError(avaliable_technologies, technologies_not_avaliable)
        
        else:            
            new_dev.format_birthdate()
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
        
        

        if 'birthdate' in data.keys():
            
            if not DeveloperModel.verify_birthdate_pattern(data['birthdate']):
                raise InvalidFormatToBirthdateError

        if 'email' in data.keys():
        
            found_email = ContractorModel.query.filter_by(email=data['email']).first()
            
            if found_email:
                raise EmailAlreadyRegisteredError
            
            else: 
                
                if not DeveloperModel.verify_pattern_email(data['email']):
                    raise InvalidEmailError(data)
                
        current_developer = get_jwt_identity()
        
        found_developer = DeveloperModel.query.filter_by(email=current_developer['email']).first()
        
        if 'password' in data.keys():
            
            if not ContractorModel.verify_pattern_password(data['password']):
                raise InvalidPasswordError(data)
            
            developer = DeveloperModel(password=data.pop('password'))
            
            data['password_hash'] = developer.password_hash
        
        if data.get('technologies'):
            
            technologies = data.pop('technologies')
            
            technologies_not_avaliable = []
            avaliable_technologies = []
            developer_techs = []
            
            
            
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

        if technologies_not_avaliable:
            raise TechNotFoundError(avaliable_technologies, technologies_not_avaliable)
        
        DeveloperModel.query.filter_by(id=found_developer.id).update(data)
            
        db.session.commit()
    
        updated_data = asdict(DeveloperModel.query.get(found_developer.id))

        updated_data['birthdate'] = datetime.strftime(updated_data['birthdate'], "%d/%m/%y")
        
        return jsonify(updated_data), 200
    

    except sqlalchemy.exc.IntegrityError as e:
        
        if type(e.orig) ==  psycopg2.errors.UniqueViolation:
            return {'Message': 'Please use another email'}, 400   


    except sqlalchemy.exc.ProgrammingError:
        
         return {'Message': "fields are empty"}, 409
     
    except InvalidEmailError as e:
        return jsonify(e.__dict__), 406
    
    except InvalidFormatToBirthdateError as e:
        return jsonify(e.__dict__), 406
    
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
    user_list = DeveloperModel.query.all()
    return jsonify(user_list), 200
