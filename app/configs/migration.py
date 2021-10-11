from flask_migrate import Migrate
from flask import Flask

def init_app(app: Flask):
  from app.models.contractor_model import ContractorModel
  from app.models.developer_model import DeveloperModel
  from app.models.job_model import JobModel
  from app.models.tech_model import TechModel

  Migrate(app, app.db)