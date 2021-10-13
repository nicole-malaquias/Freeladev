from flask_jwt_extended import (create_access_token, get_jwt_identity, jwt_required)
from app.models.job_model import JobModel
from app.models.contractor_model import ContractorModel
from app.models.developer_model import DeveloperModel
from flask import current_app, jsonify

@jwt_required()
def create_job():
    ...


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
    ...


def get_all_jobs():
    session = current_app.db.session
    jobs = session.query(JobModel)\
                  .all()
    return jsonify(jobs)