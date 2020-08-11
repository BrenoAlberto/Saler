from resale_api import db


class EstateAgency(db.Model):
    __tablename__ = "estate_agency"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=True)
