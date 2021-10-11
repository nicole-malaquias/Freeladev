from flask import Blueprint
from app.controllers.developer_controller import create_profile, update_profile_info, delete_profile, get_all_developers, get_profile_info

bp = Blueprint('bp_developer', __name__, url_prefix='/developer')

bp.post('/signup')(create_profile)


bp.get('/profile')(get_profile_info)
bp.get('')(get_all_developers)

bp.patch('/update')(update_profile_info)

bp.delete('/delete')(delete_profile)




