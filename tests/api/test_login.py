import json
from os import path

import requests
from jsonschema.validators import validate


def test_successful_login(base_url, login_endpoint):
    user_data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(f"{base_url}{login_endpoint}", json=user_data)
    assert response.json()["token"] is not None


def test_unsuccessful_login(base_url, login_endpoint):
    user_data = {
        "email": "peter@klaven"
    }
    response = requests.post(f"{base_url}{login_endpoint}", json=user_data)
    assert response.status_code == 400
    response_body = response.json()
    assert response_body["error"] == "Missing password"


def test_successful_login_schema(base_url, login_endpoint):
    user_data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(f"{base_url}{login_endpoint}", json=user_data)
    with open(path.join(path.dirname(__file__), "resources", "schemas", "login_schema.json")) as f:
        validate(response.json(), json.load(f))
