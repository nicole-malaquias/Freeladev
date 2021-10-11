from flask import Blueprint
from app.controllers.job_controller import create_job, update_job_by_id, delete_job_by_id, get_all_jobs,  get_job_by_id

bp = Blueprint('bp_job', __name__, url_prefix='/developer')

bp.post('')(create_job)

bp.get('/<int:job_id>')(get_job_by_id)
bp.get('')(get_all_jobs)

bp.patch('/<int:job_id>')(update_job_by_id)

bp.delete('/<int:job_id>')(delete_job_by_id)