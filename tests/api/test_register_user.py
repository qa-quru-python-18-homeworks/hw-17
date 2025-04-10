import pytest
import requests
from jsonschema.validators import validate

REGISTER_USER_ENDPOINT = "/register"


@pytest.mark.parametrize("auth_user_data", ["email_and_password"], indirect=True)
def test_user_registration_success(base_url, auth_user_data, load_schema):
    response = requests.post(f"{base_url}{REGISTER_USER_ENDPOINT}", json=auth_user_data)

    assert response.status_code == 200
    validate(response.json(), load_schema("register_user_schema"))


@pytest.mark.parametrize("auth_user_data", ["only_email"], indirect=True)
def test_user_registration_fails_with_missing_password(base_url, auth_user_data, load_schema):
    response = requests.post(f"{base_url}{REGISTER_USER_ENDPOINT}", json=auth_user_data)

    assert response.status_code == 400
    validate(response.json(), load_schema("error_schema"))
    assert response.json()["error"] == "Missing password"


@pytest.mark.parametrize("auth_user_data", ["only_password", "empty", "none"], indirect=True)
def test_register_user_fails_with_missing_email_or_username(base_url, auth_user_data, load_schema):
    response = requests.post(f"{base_url}{REGISTER_USER_ENDPOINT}", json=auth_user_data)

    assert response.status_code == 400
    validate(response.json(), load_schema("error_schema"))
    assert response.json()["error"] == "Missing email or username"
