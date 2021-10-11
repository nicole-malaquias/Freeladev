from flask import Blueprint
from app.controllers.contractor_controller import create_profile, update_profile_info, delete_profile, get_all_contractors, get_profile_info

bp = Blueprint('bp_contractor', __name__, url_prefix='/contractor')

bp.post('/signup')(create_profile)

bp.get('/profile')(get_profile_info)
bp.get('')(get_all_contractors)

bp.patch('/update')(update_profile_info)

bp.delete('/delete')(delete_profile)




