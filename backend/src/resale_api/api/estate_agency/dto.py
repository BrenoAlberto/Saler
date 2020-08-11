from flask_restx import Model
from flask_restx.fields import Boolean, String, Nested, Integer, List
from flask_restx.inputs import positive
from flask_restx.reqparse import RequestParser

create_estate_agency_reqparser = RequestParser(bundle_errors=True)
create_estate_agency_reqparser.add_argument(
    "name", location="form", required=True, nullable=False
)
create_estate_agency_reqparser.add_argument(
    "address", location="form", required=True, nullable=False
)

update_estate_agency_reqparser = create_estate_agency_reqparser.copy()

estate_agency_model = Model(
    "Estate Agency",
    {
        "id": Integer,
        "name": String,
        "address": String
    }
)

pagination_reqparser = RequestParser(bundle_errors=True)
pagination_reqparser.add_argument(
    "page", type=positive, required=False, default=1)
pagination_reqparser.add_argument(
    "per_page", type=positive, required=False, choices=[5, 10, 25, 50, 100], default=10
)

pagination_links_model = Model(
    "Nav Links",
    {"self": String, "prev": String, "next": String,
        "first": String, "last": String},
)

pagination_model = Model(
    "Pagination",
    {
        "links": Nested(pagination_links_model, skip_none=True),
        "has_prev": Boolean,
        "has_next": Boolean,
        "page": Integer,
        "total_pages": Integer(attribute="pages"),
        "items_per_page": Integer(attribute="per_page"),
        "total_items": Integer(attribute="total"),
        "items": List(Nested(estate_agency_model)),
    },
)
