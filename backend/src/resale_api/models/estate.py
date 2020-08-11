from flask import current_app

from resale_api import db


class Estate(db.Model):
    """Estate Model."""

    __tablename__ = "estate"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum('Active', 'Inactive'), nullable=False)
    # Características (Número de quartos, salas, banheiros, vagas de garagem, etc...)
    # characteristics = db.Column(db.JSON, nullable=True)
    characteristics = db.Column(db.String(255), nullable=True)
    kind = db.Column(db.Enum('Apartment', 'House'), nullable=False)
    finality = db.Column(db.Enum('Residencial', 'Office'), nullable=True)
    estate_agency_id = db.Column(db.Integer, db.ForeignKey(
        'estate_agency.id'), nullable=False)
