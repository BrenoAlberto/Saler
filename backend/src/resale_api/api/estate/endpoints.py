from http import HTTPStatus

from flask_restx import Namespace, Resource

from resale_api.api.estate.dto import (
    create_estate_reqparser,
    update_estate_reqparser,
    pagination_reqparser,
    estate_model,
    pagination_links_model,
    pagination_model
)
from resale_api.api.estate.business import (
    create_estate,
    retrieve_estate_list,
    retrieve_estate,
    update_estate,
    delete_estate
)

estate_ns = Namespace(name="Estates", validate=True)
estate_ns.models[estate_model.name] = estate_model
estate_ns.models[pagination_links_model.name] = pagination_links_model
estate_ns.models[pagination_model.name] = pagination_model


@estate_ns.route("", endpoint="estate_list")
@estate_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
class EstateList(Resource):
    """Handles HTTP requests to URL: /estates."""

    @estate_ns.response(HTTPStatus.OK, "Retrieved estage agency list.", pagination_model)
    @estate_ns.expect(pagination_reqparser)
    def get(self):
        """Retrieve a list of estates."""
        request_data = pagination_reqparser.parse_args()
        page = request_data.get("page")
        per_page = request_data.get("per_page")
        return retrieve_estate_list(page, per_page)

    @estate_ns.response(int(HTTPStatus.CREATED), "Created a new estate.")
    @estate_ns.response(int(HTTPStatus.CONFLICT), "Estate name already exists.")
    @estate_ns.expect(create_estate_reqparser)
    def post(self):
        """Create a estate."""
        estate_dict = create_estate_reqparser.parse_args()
        return create_estate(estate_dict)


@estate_ns.route("/<id>", endpoint="estate")
@estate_ns.param("id", "Estate id")
@estate_ns.response(int(HTTPStatus.NOT_FOUND), "Estate not found.")
@estate_ns.response(int(HTTPStatus.INTERNAL_SERVER_ERROR), "Internal server error.")
class Estate(Resource):
    """Handles HTTP requests to URL: /estates/{id}."""

    @estate_ns.response(int(HTTPStatus.OK), "Retrieved estate.", estate_model)
    @estate_ns.marshal_with(estate_model)
    def get(self, id):
        """Retrieve a estate."""
        return retrieve_estate(id)

    @estate_ns.response(int(HTTPStatus.OK), "Estate was updated.", estate_model)
    @estate_ns.response(int(HTTPStatus.CREATED), "Added new estate.")
    @estate_ns.expect(update_estate_reqparser)
    def put(self, id):
        """Update a estate."""
        estate_dict = update_estate_reqparser.parse_args()
        return update_estate(id, estate_dict)

    @estate_ns.response(int(HTTPStatus.NO_CONTENT), "Estate was deleted.")
    def delete(self, id):
        """Delete a estate."""
        return delete_estate(id)
