import json
import string
import random
from os import path

import requests
from jsonschema.validators import validate


def test_update_user_job(base_url, update_delete_user_endpoint):
    random_string = ''.join(random.choices(string.ascii_letters, k=random.randint(1, 10)))
    user_data = {
        "name": "morpheus",
        "job": f"{random_string}"
    }
    response = requests.put(f"{base_url}{update_delete_user_endpoint}", json=user_data)
    assert response.json()["job"] == random_string


def test_update_user_schema(base_url, update_delete_user_endpoint):
    user_data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put(f"{base_url}{update_delete_user_endpoint}", json=user_data)
    with open(path.join(path.dirname(__file__), "resources", "schemas", "update_user_schema.json")) as f:
        validate(response.json(), json.load(f))
