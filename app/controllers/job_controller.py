from dataclasses import asdict

from app.configs.database import db
from app.exceptions.job_exceptions import FieldCreateJobError
from app.exceptions.users_exceptions import UserNotFoundError
from app.models.contractor_model import ContractorModel
from app.models.developer_model import DeveloperModel
from app.models.job_model import JobModel
from flask import current_app, jsonify, request
import sqlalchemy
from flask_jwt_extended import get_jwt_identity, jwt_required, verify_jwt_in_request
import psycopg2
from sqlalchemy import exc
from datetime import datetime


@jwt_required()
def create_job():
    
    try :

        current_contractor = get_jwt_identity()
        
        found_contractor = ContractorModel.query.filter_by(email=current_contractor['email']).first()

        if not found_contractor:
            raise UserNotFoundError

        data = request.json

        data['contractor_id'] = found_contractor.id
        
        
        new_job = JobModel(**data)
                
        db.session.add(new_job)
        
        db.session.commit()
        
        new_job.format_expiration_date()
        
        serialized_data = asdict(new_job)
        
        del serialized_data['contractor']
        
        del serialized_data['developer']
        
        return jsonify(serialized_data), 200
    
    except UserNotFoundError as e:
        return {'message': str(e)}, 404
    
    except sqlalchemy.exc.IntegrityError as e:
        
        if type(e.orig) == psycopg2.errors.NotNullViolation:
            return {'Message': 'Job must be created with name, description, price, difficulty_level and expiration_date'}, 406
    
    except (TypeError, KeyError):
        e = FieldCreateJobError()
        return jsonify(e.message), 406


def get_job_by_id(job_id: int):

        job = JobModel.query.filter_by(id=job_id).first()
        if job is None:
            return {"message": "This job does not exist"}, 404
        if job.developer_id:
            return {"message": "This specific job already has a developer assigned to it."}, 409
           
        else:
            return jsonify(job)


@jwt_required()
def update_job_by_id(job_id: int):
    try:
        data = request.json
        
        contractor = get_jwt_identity()
        found_contractor = ContractorModel.query.filter_by(email=contractor["email"]).first()
        job = JobModel.query.filter_by(id=job_id).first()
        if job is None:
            return {"message": "Job not found!"}, 404
      
        if 'developer' in data:
            developer_email = data.pop('developer')
            developer = DeveloperModel.query.filter_by(email=developer_email).first()
            data['developer_id'] = developer.id
            
        if job.contractor_id == found_contractor.id:
            JobModel.query.filter_by(id=job_id).update(data)
            current_app.db.session.commit()
        else:
            return jsonify({"message": "Only the contractor of this specific job can update it"}), 409
            
        job_expiration_date = datetime.strftime(job.expiration_date, "%d/%m/%y %H:%M")
        developer = DeveloperModel.query.filter_by(id=job.developer_id).first()
        
        if 'developer_id' in data:
            job.progress = "ongoing"
            developer_birthdate = datetime.strftime(developer.birthdate, "%d/%m/%y %H:%M")
            return jsonify({"name": job.name,  "description": job.description, "price": job.price, "difficulty_level": job.difficulty_level, "expiration_date": job_expiration_date, "progress": job.progress, "developer": [{"name": developer.name, "email": developer.email, "birthdate": developer_birthdate}]})
        elif job.developer_id:  
            developer_birthdate = datetime.strftime(developer.birthdate, "%d/%m/%y %H:%M")          
            return jsonify({"name": job.name,  "description": job.description, "price": job.price, "difficulty_level": job.difficulty_level, "expiration_date": job_expiration_date, "progress": job.progress, "developer": [{"name": developer.name, "email": developer.email, "birthdate": developer_birthdate}]})
        else:
            return jsonify({"name": job.name,  "description": job.description, "price": job.price, "difficulty_level": job.difficulty_level, "expiration_date": job_expiration_date, "progress": job.progress})
            
    except exc.InvalidRequestError as e: 
        return {"message": "The available keys for job update are: name, description, price, difficulty_level, expiration_date, progress and developer"}, 409

    except sqlalchemy.exc.InvalidRequestError:
        return {'message': 'Job must be created with name, description, price, difficulty_level and expiration_date'}, 406
    
    except  sqlalchemy.exc.ProgrammingError:
        return {'message': "You need to send one of these keys to update a job: name, description, price, difficulty_level, expiration_date, progress and develope"}

        
@jwt_required()
def delete_job_by_id(job_id: int):
    
    session = current_app.db.session
    current_user = get_jwt_identity()
    
    found_contractor = ContractorModel.query.filter_by(email=current_user['email']).first()
    
    try:
        job = JobModel.query.get(job_id)
        
        if job.contractor_id == found_contractor.id:
            session.delete(job)
            session.commit()
            return '', 204
        
        else:
            return {'message': "You don't have permission to delete this job"}, 403
        
    except AttributeError:
        return {'message': 'job not found'}, 404

def get_all_jobs():
    session = current_app.db.session
    jobs = session.query(JobModel)\
                  .all()
    return jsonify(jobs)
