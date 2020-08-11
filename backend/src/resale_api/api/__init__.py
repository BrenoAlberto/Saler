from flask import Blueprint
from flask_restx import Api

from resale_api.api.estate.endpoints import estate_ns
from resale_api.api.estate_agency.endpoints import estate_agency_ns

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")

api = Api(
    api_bp,
    version="1.0",
    title="Resale API",
    doc="/ui"
)

api.add_namespace(estate_ns, path="/estates")
api.add_namespace(estate_agency_ns, path="/estate_agencies")
