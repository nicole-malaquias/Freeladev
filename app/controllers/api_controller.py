from app.exceptions.users_exceptions import UserNotFoundError
from app.models.contractor_model import ContractorModel
from app.models.developer_model import DeveloperModel
from flask import jsonify, request
from flask_jwt_extended import create_access_token

def login():
    data = request.json
    
    found_contractor = ContractorModel.query.filter_by(email=data['email']).first()
    found_developer = DeveloperModel.query.filter_by(email=data['email']).first()
    
    try:
        if not found_contractor and not found_developer:
            raise UserNotFoundError
        
        if found_developer:
            is_valid_password = found_developer.verify_password(data['password'])
            
            if is_valid_password:
                access_token = create_access_token(identity=found_developer)
                return jsonify(access_token=access_token), 200
        
        elif found_contractor:
            is_valid_password = found_contractor.verify_password(data['password'])
            
            if is_valid_password:
                access_token = create_access_token(identity=found_contractor)
                return jsonify(access_token=access_token), 200

    except UserNotFoundError as e:
        return {'message': str(e)}, 404
