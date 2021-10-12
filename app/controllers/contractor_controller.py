from flask_jwt_extended import (create_access_token, get_jwt_identity, jwt_required)
from flask import request, current_app, jsonify
import psycopg2
from app.models.contractor_model import ContractorModel
from app.exceptions.field_create_contractor_exception import FieldCreateContractorError
from sqlalchemy import exc

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
                
        session = current_app.db.session
        password_to_hash = data.pop("password")
        new_user = ContractorModel(**data)
        new_user.password = password_to_hash
        session.add(new_user)
        session.commit()
        found_user = ContractorModel.query.filter_by(email=data["email"]).first()
        return jsonify(found_user), 200
        
    except exc.IntegrityError as e:
        if type(e.orig) == psycopg2.errors.UniqueViolation:  
            return {"message": "User already exists"}, 409

    except (KeyError, TypeError):
        err = FieldCreateContractorError()
        return jsonify(err.message)




@jwt_required()
def get_profile_info():
    ...

@jwt_required()
def update_profile_info():
    ...

@jwt_required()
def delete_profile():
    ...
    
def get_all_contractors():
    session = current_app.db.session
    contractors = session.query(ContractorModel)\
                  .all()
    return jsonify(contractors)



