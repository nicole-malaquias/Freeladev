from dataclasses import asdict
from datetime import datetime

import psycopg2
import sqlalchemy
from app.configs.database import db
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

        if not DeveloperModel.verify_pattern_email(data['email']):
            return {"message": "Email must contain @ and ."}, 409

        if not DeveloperModel.verify_birthdate_pattern(data['birthdate']):
            return {"message": "Birthdate must be in this format: mm/dd/yyyy"}, 409
        
        if 'email' in data :
        
            query = ContractorModel.query.filter(ContractorModel.email == data['email']).all()
            
            if len(query)  > 0 :
                return {'message': 'Email is already used as contractor, please use another one for your developer account.'}, 409
            
        current_user = get_jwt_identity()
        user = DeveloperModel.query.filter(DeveloperModel.email == current_user['email']).one()
        
        if 'password' in data :
            
            if DeveloperModel.verify_pattern_password(data['password']) :
                
                user.password = data['password']
                db.session.add(user)
                db.session.commit()
                del data['password']
                
            else:
                return "Password must contain from 6 to maximum 20 characters, at least one number, upper and lower case and one special character", 409
            
        if len(data) > 0 :
            
            user = DeveloperModel.query.filter(DeveloperModel.email == current_user['email']).update(data)
            db.session.commit()
            
        user = DeveloperModel.query.filter(DeveloperModel.email == current_user['email']).one()   
        user.birthdate = datetime.strftime(user.birthdate, "%d/%m/%y %H:%M")
        return jsonify(user)
    

    except sqlalchemy.exc.IntegrityError as e :

        if type(e.orig) == psycopg2.errors.NotNullViolation:
            return {'Message': 'Developer must be created with name, email, password and birthdate'}, 400

        if type(e.orig) ==  psycopg2.errors.UniqueViolation:
            return {'Message': 'Please use another email'}, 400   


    except (FieldUpdateDeveloperError, sqlalchemy.exc.InvalidRequestError, KeyError):
        
        err = FieldUpdateDeveloperError()
        return jsonify(err.message),409

    except sqlalchemy.exc.ProgrammingError:
        
         return {'Message': "fields are empty"}, 409

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
