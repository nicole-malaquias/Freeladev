from flask_jwt_extended import (get_jwt_identity, jwt_required)
from werkzeug.wrappers import request
from app.models.job_model import JobModel

from app.models.contractor_model import ContractorModel
from flask import current_app, jsonify

from app.models.contractor_model import ContractorModel
from app.exceptions.invalid_field_create_job_exceptions import FieldCreateJobError
from flask import current_app, jsonify , request
from app.configs.database import db
import psycopg2
import sqlalchemy


@jwt_required()
def create_job():
    try :

        user = get_jwt_identity()
        contractor = ContractorModel.query.filter(ContractorModel.email == user['email']).all()[0]

        if contractor == None:
            return {"message": "Only a contractor can create a job"}

        data = request.json

        new_job = JobModel(**data)

        db.session.add(new_job)
        db.session.commit()

        found_contractor = JobModel.query.filter_by( contractor_id = contractor.id).first()
        return jsonify(found_contractor)

    except TypeError :
        err = FieldCreateJobError()
        return str(err.message),422

    except sqlalchemy.exc.IntegrityError as e :

        if type(e.orig) == psycopg2.errors.NotNullViolation:
            return {'Message': str(e.orig).split('\n')[0]}, 402

def get_job_by_id(job_id: int):
    job = JobModel.query.filter_by(id=job_id).first()
    if job is None:
        return {"message": "Job does not exist"}, 404
    return jsonify(job)

@jwt_required()
def update_job_by_id(job_id: int):
    ...

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
