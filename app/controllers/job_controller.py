from flask_jwt_extended import (create_access_token, get_jwt_identity, jwt_required)
from app.models.job_model import JobModel
from app.models.contractor_model import ContractorModel
from app.models.developer_model import DeveloperModel
from flask import current_app, jsonify

@jwt_required()
def create_job():
    ...

@jwt_required()
def get_job_by_id(job_id: int):
        user = get_jwt_identity()
        found_contractor = ContractorModel.query.filter_by(email=user["email"]).first()
        found_developer = DeveloperModel.query.filter_by(email=user["email"]).first()
        job = JobModel.query.filter_by(id=job_id).first()
        if job is None:
            return {"message": "Job does not exist"}, 404
        if found_developer == None:
                if found_contractor.id == job.contractor_id:
                    return jsonify(job)
        else:
            if found_developer.id == job.developer_id:
                return jsonify(job)
        return {"message": "Only the contractor that created the job and the developer that was assigned to the job can see its info"}

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