import requests


def test_successful_user_registration(base_url, register_user_endpoint):
    user_data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(f"{base_url}{register_user_endpoint}", json=user_data)
    assert response.status_code == 200


def test_user_registration_without_password(base_url, register_user_endpoint):
    user_data = {
        "email": "eve.holt@reqres.in"
    }
    response = requests.post(f"{base_url}{register_user_endpoint}", json=user_data)
    assert response.status_code == 400
    response_body = response.json()
    assert response_body["error"] == "Missing password"


def test_user_registration_without_email(base_url, register_user_endpoint):
    user_data = {
        "password": "pistol"
    }
    response = requests.post(f"{base_url}{register_user_endpoint}", json=user_data)
    assert response.status_code == 400
    response_body = response.json()
    assert response_body["error"] == "Missing email or username"


def test_user_registration_without_email_and_password(base_url, register_user_endpoint):
    user_data = {}
    response = requests.post(f"{base_url}{register_user_endpoint}", json=user_data)
    assert response.status_code == 400
    response_body = response.json()
    assert response_body["error"] == "Missing email or username"


def test_user_registration_without_body(base_url, register_user_endpoint):
    response = requests.post(f"{base_url}{register_user_endpoint}")
    assert response.status_code == 400
    response_body = response.json()
    assert response_body["error"] == "Missing email or username"
