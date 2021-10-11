from flask_jwt_extended import (create_access_token, get_jwt_identity, jwt_required)
from flask import request, current_app, jsonify
import psycopg2
from app.models.contractor_model import ContractorModel
from sqlalchemy import exc

def create_profile():
    try:
        data = request.json
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
    ...



