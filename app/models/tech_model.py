from app.configs.database import db
from dataclasses import dataclass



@dataclass
class TechModel(db.Model):
    name: str


    __tablename__ = 'techs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    @staticmethod
    def get_tech(tech_name):
        found_tech = TechModel.query.filter_by(name=tech_name.capitalize()).first()
        return found_tech
    
         