import json
import os

import faker
import pytest


@pytest.fixture()
def base_url():
    return "https://reqres.in/api"


@pytest.fixture()
def page_number():
    return 1


@pytest.fixture()
def user_id():
    return 1


@pytest.fixture()
def load_schema():
    def _load(schema_name: str):
        schema_path = os.path.join(
            os.path.dirname(__file__),
            "resources",
            "schemas",
            f"{schema_name}.json"
        )
        with open(schema_path) as f:
            return json.load(f)

    return _load


@pytest.fixture()
def auth_user_data(request):
    data_map = {
        'only_email': {"email": "eve.holt@reqres.in"},
        'only_password': {"password": "pistol"},
        'email_and_password': {"email": "eve.holt@reqres.in", "password": "pistol"},
        'empty': {},
        'none': None
    }
    if request.param not in data_map:
        raise ValueError(f"Unknown user data type: {request.param}")
    return data_map[request.param]


@pytest.fixture()
def update_user_data():
    random_job = faker.Faker().job()
    return {
        "name": "morpheus",
        "job": f"{random_job}"
    }
