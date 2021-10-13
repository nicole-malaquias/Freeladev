from flask_jwt_extended import (create_access_token, get_jwt_identity, jwt_required)
from app.models.job_model import JobModel
from app.models.contractor_model import ContractorModel
from app.models.developer_model import DeveloperModel
from flask import current_app, jsonify, request

@jwt_required()
def create_job():
    ...


def get_job_by_id(job_id: int):
    job = JobModel.query.filter_by(id=job_id).first()
    if job is None:
        return {"message": "This job does not exist"}, 404
    return jsonify(job)

@jwt_required()
def update_job_by_id(job_id: int):
    data = request.json
    print(data['developer'])
    contractor = get_jwt_identity()
    found_contractor = ContractorModel.query.filter_by(email=contractor["email"]).first()
    job = JobModel.query.filter_by(id=job_id).first()
    if job is None:
        return {"message": "Job not found!"}, 404
    if 'developer' in data:
        developer_email = data.pop('developer')
        developer = DeveloperModel.query.filter_by(email=developer_email).first()
        
        data['developer_id'] = developer.id
        print(data)
    if job.contractor_id == found_contractor.id:
        JobModel.query.filter_by(id=job_id).update(data)
        current_app.db.session.commit()
        updated_job = JobModel.query.filter_by(id=job_id).first()
        developer = DeveloperModel.query.filter_by(email=developer_email).first()
        updated_job['developer'] = developer.name
    # check key errors
    return jsonify(updated_job)

@jwt_required()
def delete_job_by_id(job_id: int):
    ...


def get_all_jobs():
    session = current_app.db.session
    jobs = session.query(JobModel)\
                  .all()
    return jsonify(jobs)