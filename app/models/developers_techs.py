from app.configs.database import db
from dataclasses import dataclass


@dataclass
class DevelopersTechsModel(db.Model):

    __tablename__ = 'developers_techs'

    id = db.Column(db.Integer, primary_key=True)
    developer_id = db.Column(db.Integer, db.ForeignKey('developers.id'))
    tech_id = db.Column(db.Integer, db.ForeignKey('techs.id'))

    def insert_developer_techs(self):
        db.session.add(self)
        db.session.commit()