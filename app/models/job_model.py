from sqlalchemy.orm import backref, relationship
from app.configs.database import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app.models.developer_model import DeveloperModel
from app.models.contractor_model import ContractorModel

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


