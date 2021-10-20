from flask import Blueprint
from app.controllers.developer_controller import create_profile, update_profile_info, delete_profile, get_all_developers, get_profile_info, get_job_by_status

bp = Blueprint('bp_developer', __name__, url_prefix='/developers')

bp.post('/signup')(create_profile)

bp.get('/profile')(get_profile_info)
bp.get('')(get_all_developers)
bp.get('/jobs/progress')(get_job_by_status)
bp.patch('/update')(update_profile_info)

bp.delete('/delete')(delete_profile)




