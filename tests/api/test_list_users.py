import requests


def test_endpoint_smoke(base_url, list_users_endpoint):
    response = requests.get(f"{base_url}{list_users_endpoint}", params={"page": 1})
    assert response.status_code == 200


def test_that_page_has_six_users(base_url, list_users_endpoint):
    response = requests.get(f"{base_url}{list_users_endpoint}", params={"page": 1})
    response_body = response.json()
    assert len(response_body["data"]) == 6

