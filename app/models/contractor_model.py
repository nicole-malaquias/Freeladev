from app.configs.database import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash
import re
@dataclass
class ContractorModel(db.Model):
    name: str
    email: str
    cnpj: str
    

    __tablename__ = 'contractors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    cnpj = db.Column(db.String, nullable=True, unique=True)


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
        else:
            return False
    @staticmethod
    def verify_pattern_password(password):
        pattern_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        if(re.search( pattern_password, password)):
            return True
        return False
    @staticmethod
    def verify_cnpj(cnpj):
        pattern_cnpj = r'(^\d{2}.\d{3}.\d{3}/\d{4}-\d{2}$)'
        if(re.fullmatch(pattern_cnpj, cnpj)):
            return True
        else:
            return False
