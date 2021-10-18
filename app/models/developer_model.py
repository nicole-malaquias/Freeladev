import re
from dataclasses import dataclass
from datetime import datetime

from app.configs.database import db
from werkzeug.security import check_password_hash, generate_password_hash


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

    technologies = db.relationship(
        'TechModel',
        secondary='developers_techs',
        backref=db.backref('developers', lazy='dynamic'),
    )

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
    
    
    @staticmethod
    def verify_pattern_email(email):
        
        pattern_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if(re.fullmatch(pattern_email, email)):
            
            return True
        
        return False

    @staticmethod
    def verify_pattern_password(password):
        
        pattern_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        
        if(re.search( pattern_password, password)):
            
            return True
        
        return False 

    @staticmethod                
    def verify_birthdate_pattern(user_birthdate):
        birthdate_pattern = "^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d$"
        
        if(re.search( birthdate_pattern, user_birthdate)):
            
            return True
        
        return False 
                
    def format_birthdate(self):
        self.birthdate = datetime.strftime(self.birthdate, "%d/%m/%y")
