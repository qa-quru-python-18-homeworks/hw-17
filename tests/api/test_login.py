import pytest
import requests
from jsonschema.validators import validate

LOGIN_ENDPOINT = "/login"


@pytest.mark.parametrize("auth_user_data", ["email_and_password"], indirect=True)
def test_successful_login(base_url, auth_user_data, load_schema):
    response = requests.post(f"{base_url}{LOGIN_ENDPOINT}", json=auth_user_data)

    assert response.status_code == 200
    validate(response.json(), load_schema("login_schema"))
    assert response.json()["token"] is not None


@pytest.mark.parametrize("auth_user_data", ["only_email"], indirect=True)
def test_unsuccessful_login_with_missing_password(base_url, auth_user_data, load_schema):
    response = requests.post(f"{base_url}{LOGIN_ENDPOINT}", json=auth_user_data)

    assert response.status_code == 400
    validate(response.json(), load_schema("error_schema"))
    assert response.json()["error"] == "Missing password"


@pytest.mark.parametrize("auth_user_data", ["only_password", "empty", "none"], indirect=True)
def test_unsuccessful_login_with_missing_password(base_url, auth_user_data, load_schema):
    response = requests.post(f"{base_url}{LOGIN_ENDPOINT}", json=auth_user_data)

    assert response.status_code == 400
    validate(response.json(), load_schema("error_schema"))
    assert response.json()["error"] == "Missing email or username"
