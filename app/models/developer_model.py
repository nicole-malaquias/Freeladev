from app.configs.database import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

@dataclass
class DeveloperModel(db.Model):
    name: str
    email: str
    birthdate: datetime
    

    __tablename__ = 'developers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    birthdate = db.Column(db.DateTime(timezone=True), nullable=False)


    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")


    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)


    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)