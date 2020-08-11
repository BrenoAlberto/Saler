from http import HTTPStatus

from flask_restx import Namespace, Resource

from resale_api.api.estate_agency.dto import (
    create_estate_agency_reqparser,
    update_estate_agency_reqparser,
    pagination_reqparser,
    estate_agency_model,
    pagination_links_model,
    pagination_model
)
from resale_api.api.estate_agency.business import (
    create_estate_agency,
    retrieve_estate_agency_list,
    retrieve_estate_agency,
    update_estate_agency,
    delete_estate_agency
)

estate_agency_ns = Namespace(name="Estate Agencies", validate=True)
estate_agency_ns.models[estate_agency_model.name] = estate_agency_model
estate_agency_ns.models[pagination_links_model.name] = pagination_links_model
estate_agency_ns.models[pagination_model.name] = pagination_model


@estate_agency_ns.route("", endpoint="estate_agency_list")
@estate_agency_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
class EstateAgencyList(Resource):
    """Handles HTTP requests to URL: /estate_agencies."""

    @estate_agency_ns.response(HTTPStatus.OK, "Retrieved estage agency list.", pagination_model)
    @estate_agency_ns.expect(pagination_reqparser)
    def get(self):
        """Retrieve a list of estate agencies."""
        request_data = pagination_reqparser.parse_args()
        page = request_data.get("page")
        per_page = request_data.get("per_page")
        return retrieve_estate_agency_list(page, per_page)

    @estate_agency_ns.response(int(HTTPStatus.CREATED), "Created a new estate agency.")
    @estate_agency_ns.response(int(HTTPStatus.CONFLICT), "Estate agency name already exists.")
    @estate_agency_ns.expect(create_estate_agency_reqparser)
    def post(self):
        """Create a estate agency."""
        estate_agency_dict = create_estate_agency_reqparser.parse_args()
        return create_estate_agency(estate_agency_dict)


@estate_agency_ns.route("/<id>", endpoint="estate_agency")
@estate_agency_ns.param("id", "Estate agency id")
@estate_agency_ns.response(int(HTTPStatus.NOT_FOUND), "Estate agency not found.")
@estate_agency_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
class EstateAgency(Resource):
    """Handles HTTP requests to URL: /estate_agencies/{id}."""

    @estate_agency_ns.response(int(HTTPStatus.OK), "Retrieved estate agency.", estate_agency_model)
    @estate_agency_ns.marshal_with(estate_agency_model)
    def get(self, id):
        """Retrieve a estate agency."""
        return retrieve_estate_agency(id)

    @estate_agency_ns.response(int(HTTPStatus.OK), "Estate agency was updated.", estate_agency_model)
    @estate_agency_ns.response(int(HTTPStatus.CREATED), "Added new estate agency.")
    @estate_agency_ns.expect(update_estate_agency_reqparser)
    def put(self, id):
        """Update a estate agency."""
        estate_agency_dict = update_estate_agency_reqparser.parse_args()
        return update_estate_agency(id, estate_agency_dict)

    @estate_agency_ns.response(int(HTTPStatus.NO_CONTENT), "Estate agency was deleted.")
    def delete(self, id):
        """Delete a estate agency."""
        return delete_estate_agency(id)
