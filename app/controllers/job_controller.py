from flask_jwt_extended import (create_access_token, get_jwt_identity, jwt_required)


@jwt_required()
def create_job():
    ...

@jwt_required()
def get_job_by_id(job_id: int):
    ...

@jwt_required()
def update_job_by_id(job_id: int):
    ...

@jwt_required()
def delete_job_by_id(job_id: int):
    ...


def get_all_jobs():
    ...