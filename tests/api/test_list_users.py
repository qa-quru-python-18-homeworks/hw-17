import requests
from jsonschema.validators import validate

LIST_USER_ENDPOINT = "/users"
SCHEMA_NAME = "list_users_schema"


def test_list_users_returns_200_on_valid_page_request(base_url, page_number, load_schema):
    response = requests.get(f"{base_url}{LIST_USER_ENDPOINT}", params={"page": page_number})

    assert response.status_code == 200
    validate(response.json(), load_schema(SCHEMA_NAME))


def test_list_users_returns_six_users_on_first_page(base_url, page_number, load_schema):
    response = requests.get(f"{base_url}{LIST_USER_ENDPOINT}", params={"page": page_number})

    assert response.status_code == 200
    validate(response.json(), load_schema(SCHEMA_NAME))
    assert len(response.json()["data"]) == 6
