from flask import Blueprint
from app.controllers.contractor_controller import create_profile, update_profile_info, delete_profile, get_all_contractors, login, get_profile_info

bp = Blueprint('bp_contractor', __name__, url_prefix='/contractor')

bp.post('')(create_profile)
bp.post('')(login)

bp.get('')(get_profile_info)
bp.get('')(get_all_contractors)

bp.patch('')(update_profile_info)

bp.delete('')(delete_profile)




