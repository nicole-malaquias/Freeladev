from app.configs.database import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@dataclass
class JobModel(db.Model):
    name: str
    description: str
    price: float
    difficulty_level: str
    expiration_date: datetime
    progress: str
    

    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    difficulty_level = db.Column(db.String, nullable=False)
    expiration_date = db.Column(db.DateTime(timezone=True), nullable=False)
    progress = db.Column(db.String)
    password_hash = db.Column(db.String, nullable=False)


    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")


    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)


    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)