import psycopg2
from app.exceptions.contractor_exceptions import FieldCreateContractorError
from app.exceptions.field_upgrade_exeptions import FieldUpdateContractorError

from app.exceptions.invalid_password_exceptions import InvalidPasswordError
from app.models.contractor_model import ContractorModel
from app.models.developer_model import DeveloperModel
from app.configs.database import db
from flask import current_app, jsonify, request
from flask_jwt_extended import (create_access_token, get_jwt_identity,
                                jwt_required)
from sqlalchemy import exc
import sqlalchemy

def create_profile():
    try:
        data = request.json
        if not ContractorModel.verify_pattern_password(data['password']):
            return "Password must contain from 6 to maximum 20 characters, at least one number, upper and lower case and one special character"
        if not ContractorModel.verify_pattern_email(data['email']):
            return "Email must contain @ and ."
        if "cnpj" in data:
            if not ContractorModel.verify_cnpj(data['cnpj']):
                return "cnpj must be in this format: 00.000.000/0000-00"
                
        email_already_used_as_developer = DeveloperModel.query.filter_by(email=data['email']).first()
        if email_already_used_as_developer:
            return {'message': 'Email is already used as developer, please use another one for your contractor account.'}, 409

        session = current_app.db.session
        password_to_hash = data.pop("password")
        new_user = ContractorModel(**data)
        new_user.password = password_to_hash
        session.add(new_user)
        session.commit()
        found_user = ContractorModel.query.filter_by(email=data["email"]).first()
        return jsonify(found_user), 200
    
    except sqlalchemy.exc.IntegrityError as e :
        if type(e.orig) == psycopg2.errors.NotNullViolation:
            return {'Message': 'contractor must be created with name, email and password. CNPJ is optional'}, 400
        
    except exc.IntegrityError as e:
        if type(e.orig) == psycopg2.errors.UniqueViolation:  
            return {"message": "User already exists"}, 409

    except (KeyError, TypeError):
        err = FieldCreateContractorError()
        return jsonify(err.message)

@jwt_required()
def get_profile_info():
    profile_info = get_jwt_identity()
    
    return jsonify(profile_info), 200

@jwt_required()
def update_profile_info():
    
    try:
        
        data = request.json
        current_user = get_jwt_identity()
        user = ContractorModel.query.filter(ContractorModel.email == current_user['email']).one()
        
        if 'email' in data:
            query = DeveloperModel.query.filter(DeveloperModel.email == data['email']).all()
            if len(query) > 0 :
                return {"Message":"This email is already being used"},400
            
        if 'password' in data :
            
            if ContractorModel.verify_pattern_password(data['password']) :
                
                user.password = data['password']
                db.session.add(user)
                db.session.commit()
                del data['password']
                
            else:
                return "Password must contain from 6 to maximum 20 characters, at least one number, upper and lower case and one special character"
        
        if len(data) > 0 :
            
            user = ContractorModel.query.filter(ContractorModel.email == current_user['email']).update(data)
            db.session.commit()
            
         
        user = ContractorModel.query.filter(ContractorModel.email == current_user['email']).one()   
       
        return jsonify(user)
    
    except sqlalchemy.exc.IntegrityError as e :

        if type(e.orig) == psycopg2.errors.NotNullViolation:
            return {'Message': str(e.orig).split('\n')[0]}, 400

        if type(e.orig) ==  psycopg2.errors.UniqueViolation:
            return {'Message': str(e.orig).split('\n')[0]}, 400 


    except (FieldUpdateContractorError, sqlalchemy.exc.InvalidRequestError):
        
        err = FieldUpdateContractorError()
        return jsonify(err.message),409

    except sqlalchemy.exc.ProgrammingError:
        
         return {'Message': "fields are empty"}


@jwt_required()
def delete_profile():
    contractor = get_jwt_identity()
    found_contractor = ContractorModel.query.filter_by(email=contractor["email"]).first()
    if found_contractor is None:
        return {"message": "Contractor not found!"}, 404
    if contractor['email'] == found_contractor.email:
        current_app.db.session.delete(found_contractor)
        current_app.db.session.commit()
    return "", 204

    
def get_all_contractors():
    session = current_app.db.session
    contractors = session.query(ContractorModel)\
                  .all()
    return jsonify(contractors)


def get_all_contractor_jobs():
    ... 