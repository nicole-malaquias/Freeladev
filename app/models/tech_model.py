from app.configs.database import db
from dataclasses import dataclass


@dataclass
class TechModel(db.Model):
    name: str


    __tablename__ = 'techs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    