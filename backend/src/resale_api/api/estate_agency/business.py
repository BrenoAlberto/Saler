"""Business logic for /estate_agencies API endpoints."""
from http import HTTPStatus
from flask import jsonify, url_for
from flask_restx import marshal

from resale_api import db
from resale_api.api.estate_agency.dto import pagination_model
from resale_api.models.estate_agency import EstateAgency


def create_estate_agency(estate_agency_dict):
    name = estate_agency_dict["name"]
    estate_agency = EstateAgency(**estate_agency_dict)
    db.session.add(estate_agency)
    db.session.commit()
    response = jsonify(
        status="success", message=f"New estate agency added: {name}")
    response.status_code = HTTPStatus.CREATED
    return response


def retrieve_estate_agency_list(page, per_page):
    pagination = EstateAgency.query.paginate(page, per_page, error_out=False)
    response_data = marshal(pagination, pagination_model)
    response_data["links"] = _pagination_nav_links(pagination)
    response = jsonify(response_data)
    response.headers["Link"] = _pagination_nav_header_links(pagination)
    response.headers["Total-Count"] = pagination.total
    return response


def retrieve_estate_agency(id):
    return EstateAgency.query.filter_by(id=id).first_or_404(
        description=f"Estate agency {id} not found in database."
    )


def update_estate_agency(id, estate_agency_dict):
    estate_agency = EstateAgency.query.filter_by(id=id).first()
    if estate_agency:
        for k, v in estate_agency_dict.items():
            setattr(estate_agency, k, v)
        db.session.commit()
        message = f"Estate agency {id} was successfully updated"
        response_dict = dict(status="success", message=message)
        return response_dict, HTTPStatus.OK
    return create_estate_agency(estate_agency_dict)


def delete_estate_agency(id):
    estate_agency = EstateAgency.query.filter_by(id=id).first_or_404(
        description=f"{id} not found in database."
    )
    db.session.delete(estate_agency)
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT


def _pagination_nav_links(pagination):
    nav_links = {}
    per_page = pagination.per_page
    this_page = pagination.page
    last_page = pagination.pages
    nav_links["self"] = url_for(
        "api.estate_agency_list", page=this_page, per_page=per_page)
    nav_links["first"] = url_for(
        "api.estate_agency_list", page=1, per_page=per_page)
    if pagination.has_prev:
        nav_links["prev"] = url_for(
            "api.estate_agency_list", page=this_page - 1, per_page=per_page
        )
    if pagination.has_next:
        nav_links["next"] = url_for(
            "api.estate_agency_list", page=this_page + 1, per_page=per_page
        )
    nav_links["last"] = url_for(
        "api.estate_agency_list", page=last_page, per_page=per_page)
    return nav_links


def _pagination_nav_header_links(pagination):
    url_dict = _pagination_nav_links(pagination)
    link_header = ""
    for rel, url in url_dict.items():
        link_header += f'<{url}>; rel="{rel}", '
    return link_header.strip().strip(",")
