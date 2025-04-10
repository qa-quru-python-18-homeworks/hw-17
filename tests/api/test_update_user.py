import requests
from jsonschema.validators import validate

UPDATE_USER_ENDPOINT = "/users"


def test_update_user_job(base_url, user_id, update_user_data, load_schema):
    response = requests.put(f"{base_url}{UPDATE_USER_ENDPOINT}/{user_id}", json=update_user_data)

    assert response.status_code == 200
    validate(response.json(), load_schema("update_user_schema"))
    assert response.json()["job"] == update_user_data["job"]
