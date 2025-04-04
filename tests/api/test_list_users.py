import json
from os import path

import requests
from jsonschema.validators import validate


def test_list_users_returns_200_on_valid_page_request(base_url, list_users_endpoint):
    response = requests.get(f"{base_url}{list_users_endpoint}", params={"page": 1})
    assert response.status_code == 200


def test_list_users_returns_six_users_on_first_page(base_url, list_users_endpoint):
    response = requests.get(f"{base_url}{list_users_endpoint}", params={"page": 1})
    response_body = response.json()
    assert len(response_body["data"]) == 6


def test_list_users_returns_first_page_by_default_without_params(base_url, list_users_endpoint):
    response = requests.get(f"{base_url}{list_users_endpoint}")
    response_body = response.json()
    assert response_body["page"] == 1


def test_list_users_returns_same_users_as_first_page_when_page_is_negative(base_url, list_users_endpoint):
    response_page_one = requests.get(f"{base_url}{list_users_endpoint}", params={"page": 1})
    response_body_page_one = response_page_one.json()

    response_page_minus_one = requests.get(f"{base_url}{list_users_endpoint}", params={"page": -1})
    response_body_page_minus_one = response_page_minus_one.json()

    assert response_body_page_one["data"] == response_body_page_minus_one["data"]


def test_list_users_response_schema_is_valid(base_url, list_users_endpoint):
    response = requests.get(f"{base_url}{list_users_endpoint}", params={"page": 1})
    with open(path.join(path.dirname(__file__), "resources", "schemas", "list_users_schema.json")) as f:
        validate(response.json(), json.load(f))
