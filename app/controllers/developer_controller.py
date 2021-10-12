<<<<<<< HEAD
from app.configs.database import db
from app.exceptions.invalid_email_exceptions import InvalidEmailError
from app.exceptions.invalid_password_exceptions import InvalidPasswordError
from app.exceptions.invalid_field_create_developer_exceptions import FieldCreateDeveloperError
from app.models.developer_model import DeveloperModel

from flask import jsonify, request

from http import HTTPStatus
from flask_jwt_extended import (create_access_token, get_jwt_identity,
                                jwt_required)

=======
from flask_jwt_extended import (create_access_token, get_jwt_identity, jwt_required)
>>>>>>> 5945dfd675c19b3901aaa80c855b3d92d2c29586

def create_profile():
    ...


<<<<<<< HEAD
    except (KeyError,TypeError) :
        err = FieldCreateDeveloperError()
        return jsonify(err.message)
    
    
=======
>>>>>>> 5945dfd675c19b3901aaa80c855b3d92d2c29586
@jwt_required()
def get_profile_info():
    ...

@jwt_required()
def update_profile_info():
    ...

@jwt_required()
def delete_profile():
    ...


def get_all_developers():
    ...


    

