from flask import Blueprint
from app.controllers.job_controller import get_job_by_tech ,create_job, update_job_by_id, delete_job_by_id, get_all_jobs,  get_job_by_id

bp = Blueprint('bp_job', __name__, url_prefix='/job')

bp.get('')(get_job_by_tech) 

bp.post('/create')(create_job)

bp.get('/info/<int:job_id>')(get_job_by_id)
bp.get('/info/aut/<int:job_id>')(get_job_by_id_authenticated)

bp.patch('/update/<int:job_id>')(update_job_by_id)

bp.delete('/delete/<int:job_id>')(delete_job_by_id)
