from sqlalchemy.orm import backref, relationship
from app.configs.database import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app.models.developer_model import DeveloperModel
from app.models.contractor_model import ContractorModel
from flask import current_app, jsonify

@dataclass
class JobModel(db.Model):
    name: str
    description: str
    price: float
    difficulty_level: str
    expiration_date: datetime
    progress: str
    developer: 'DeveloperModel'
    contractor: 'ContractorModel'

    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    difficulty_level = db.Column(db.String, nullable=False)
    expiration_date = db.Column(db.DateTime(timezone=True), nullable=False)
    progress = db.Column(db.String)
        
    contractor_id = db.Column(db.Integer, db.ForeignKey('contractors.id'))
    developer_id = db.Column(db.Integer, db.ForeignKey('developers.id'))
    
    developer = relationship('DeveloperModel', backref=backref('jobs'))
    contractor = relationship('ContractorModel', backref=backref('jobs'))
    
    def format_expiration_date(self):
        self.expiration_date = datetime.strftime(self.expiration_date, "%d/%m/%y %H:%M")


    def update_job_if_developer_or_progress_is_null(job):
        session = current_app.db.session   
        new_job = JobModel( 
        id = job.id,
        name = job.name,
        expiration_date= job.expiration_date,
        contractor_id= job.contractor_id,
        description =    job.description,
        difficulty_level = job.difficulty_level,
        price = job.price         
    )   
        session.delete(job)
        session.commit()
        session.add(new_job)
        session.commit()

        return jsonify({"name": new_job.name,  "description": new_job.description, "price": new_job.price, "difficulty_level": new_job.difficulty_level, "expiration_date": new_job.format_expiration_date(), "progress": new_job.progress}), 200

    def update_job_if_developer_in_data(data, job_id, job):
        developer_email = data.pop('developer')
        developer = DeveloperModel.query.filter_by(email=developer_email).first()
        data['developer_id'] = developer.id
        JobModel.query.filter_by(id=job_id).update(data)
        current_app.db.session.commit()
        job.progress = "ongoing"
        developer_birthdate = datetime.strftime(developer.birthdate, "%d/%m/%y %H:%M")
        return jsonify({"name": job.name,  "description": job.description, "price": job.price, "difficulty_level": job.difficulty_level, "expiration_date": job.format_expiration_date(), "progress": job.progress, "developer": [{"name": developer.name, "email": developer.email, "birthdate": developer_birthdate}]})


