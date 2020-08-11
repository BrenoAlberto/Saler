"""Business logic for /estate_agencies API endpoints."""
from http import HTTPStatus
from flask import jsonify, url_for
from flask_restx import marshal

from resale_api import db
from resale_api.api.estate.dto import pagination_model
from resale_api.models.estate import Estate


def create_estate(estate_dict):
    name = estate_dict["name"]
    estate = Estate(**estate_dict)
    db.session.add(estate)
    db.session.commit()
    response = jsonify(
        status="success", message=f"New estate added: {name}")
    response.status_code = HTTPStatus.CREATED
    return response


def retrieve_estate_list(page, per_page):
    pagination = Estate.query.paginate(page, per_page, error_out=False)
    response_data = marshal(pagination, pagination_model)
    response_data["links"] = _pagination_nav_links(pagination)
    response = jsonify(response_data)
    response.headers["Link"] = _pagination_nav_header_links(pagination)
    response.headers["Total-Count"] = pagination.total
    return response


def retrieve_estate(id):
    return Estate.query.filter_by(id=id).first_or_404(
        description=f"Estate {id} not found in database."
    )


def update_estate(id, estate_dict):
    estate = Estate.query.filter_by(id=id).first()
    if estate:
        for k, v in estate_dict.items():
            setattr(estate, k, v)
        db.session.commit()
        message = f"Estate {id} was successfully updated"
        response_dict = dict(status="success", message=message)
        return response_dict, HTTPStatus.OK
    return create_estate(estate_dict)


def delete_estate(id):
    estate = Estate.query.filter_by(id=id).first_or_404(
        description=f"{id} not found in database."
    )
    db.session.delete(estate)
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT


def _pagination_nav_links(pagination):
    nav_links = {}
    per_page = pagination.per_page
    this_page = pagination.page
    last_page = pagination.pages
    nav_links["self"] = url_for(
        "api.estate_list", page=this_page, per_page=per_page)
    nav_links["first"] = url_for(
        "api.estate_list", page=1, per_page=per_page)
    if pagination.has_prev:
        nav_links["prev"] = url_for(
            "api.estate_list", page=this_page - 1, per_page=per_page
        )
    if pagination.has_next:
        nav_links["next"] = url_for(
            "api.estate_list", page=this_page + 1, per_page=per_page
        )
    nav_links["last"] = url_for(
        "api.estate_list", page=last_page, per_page=per_page)
    return nav_links


def _pagination_nav_header_links(pagination):
    url_dict = _pagination_nav_links(pagination)
    link_header = ""
    for rel, url in url_dict.items():
        link_header += f'<{url}>; rel="{rel}", '
    return link_header.strip().strip(",")
