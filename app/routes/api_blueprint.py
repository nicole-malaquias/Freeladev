from . import contractor_blueprint, developer_blueprint, job_blueprint
from flask import Blueprint
from app.controllers.api_controller import login

bp = Blueprint('bp_api', __name__, url_prefix='/api')

bp.register_blueprint(contractor_blueprint.bp)
bp.register_blueprint(developer_blueprint.bp)
bp.register_blueprint(job_blueprint.bp)
bp.get('/login')(login)
