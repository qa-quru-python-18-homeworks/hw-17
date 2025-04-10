import requests

DELETE_USER_ENDPOINT = "/users"


def test_delete_user(base_url, user_id):
    response = requests.delete(f"{base_url}{DELETE_USER_ENDPOINT}/{user_id}")
    assert response.status_code == 204
