from http import HTTPStatus

import psycopg2
import sqlalchemy
from app.configs.database import db
from app.exceptions.invalid_email_exceptions import InvalidEmailError
from app.exceptions.invalid_field_create_developer_exceptions import \
    FieldCreateDeveloperError
from app.exceptions.invalid_password_exceptions import InvalidPasswordError
from app.exceptions.users_exceptions import UserNotFoundError
from app.models.developer_model import DeveloperModel
from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required


def create_profile():

    try:

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

        return jsonify(new_dev), HTTPStatus.CREATED

    except InvalidEmailError as err:
        return jsonify(err.message)

    except InvalidPasswordError as err:
        return jsonify(err.message)

    except (KeyError, TypeError):
        err = FieldCreateDeveloperError()
        return jsonify(err.message)

    except sqlalchemy.exc.IntegrityError as e:

        if type(e.orig) == psycopg2.errors.NotNullViolation:
            return {'Message': str(e.orig).split('\n')[0]}, 400

        if type(e.orig) == psycopg2.errors.UniqueViolation:
            return {'Message': str(e.orig).split('\n')[0]}, 400


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
    ...


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
