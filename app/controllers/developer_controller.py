from app.configs.database import db
from app.exceptions.invalid_email_exceptions import InvalidEmailError
from app.exceptions.invalid_password_exceptions import InvalidPasswordError
from app.exceptions.invalid_field_create_developer_exceptions import FieldCreateDeveloperError
from app.exceptions.invalid_field_update_developer_exceptions import FieldUpdateDeveloperError
from app.models.developer_model import DeveloperModel
from app.models.contractor_model import ContractorModel
import psycopg2
import sqlalchemy
from flask import jsonify, request

from http import HTTPStatus
from flask_jwt_extended import (create_access_token, get_jwt_identity,
                                jwt_required)


def create_profile():
    
    try :
        
        data = request.json
        
        verify_email = DeveloperModel.verify_pattern_email(data['email'])
        if not verify_email:
            raise InvalidEmailError(data)

        verify_password = DeveloperModel.verify_pattern_password(data['password'])
        if not verify_password:
            raise InvalidPasswordError(data)
        
        password_input = data.pop('password')
        
        new_dev = DeveloperModel(**data)
        new_dev.password = password_input
        
        db.session.add(new_dev)
        db.session.commit()

        return jsonify(new_dev),HTTPStatus.CREATED
        
    except InvalidEmailError as err:
        return  jsonify(err.message)
       
    except InvalidPasswordError as err:
        return jsonify(err.message)

    except (KeyError,TypeError) :
        err = FieldCreateDeveloperError()
        return jsonify(err.message)
    
    except sqlalchemy.exc.IntegrityError as e :
        
        if type(e.orig) == psycopg2.errors.NotNullViolation:
            return {'Message': str(e.orig).split('\n')[0]}, 400
        
        if type(e.orig) ==  psycopg2.errors.UniqueViolation:
            return {'Message': str(e.orig).split('\n')[0]}, 400     
    
    
@jwt_required()
def get_profile_info():
    ...


@jwt_required()
def update_profile_info():
     
    try:
        
        data = request.json
        
        if 'email' in data :
        
            query = ContractorModel.query.filter(ContractorModel.email == data['email']).all()
            
            if len(query)  > 0 :
                return {"Message":"this email is already being used"}
            
        current_user = get_jwt_identity()
        user = DeveloperModel.query.filter(DeveloperModel.email == current_user['email']).one()
        
        if 'password' in data :
            
            if DeveloperModel.verify_pattern_password(data['password']) :
                
                user.password = data['password']
                db.session.add(user)
                db.session.commit()
                del data['password']
                
            else:
                return "Password must contain from 6 to maximum 20 characters, at least one number, upper and lower case and one special character"
            
        if len(data) > 0 :
            
            user = DeveloperModel.query.filter(DeveloperModel.email == current_user['email']).update(data)
            db.session.commit()
            
        user = DeveloperModel.query.filter(DeveloperModel.email == current_user['email']).one()   
        
        return jsonify(user)
    
    except sqlalchemy.exc.IntegrityError as e :

        if type(e.orig) == psycopg2.errors.NotNullViolation:
            return {'Message': str(e.orig).split('\n')[0]}, 400

        if type(e.orig) ==  psycopg2.errors.UniqueViolation:
            return {'Message': str(e.orig).split('\n')[0]}, 400 


    except (FieldUpdateDeveloperError, sqlalchemy.exc.InvalidRequestError):
        
        err = FieldUpdateDeveloperError()
        return jsonify(err.message),409

    except sqlalchemy.exc.ProgrammingError:
        
         return {'Message': "fields are empty"}
     
     
@jwt_required()
def delete_profile():
    ...


def get_all_developers():
    user_list = DeveloperModel.query.all()
    return jsonify(user_list), 200
