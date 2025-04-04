import requests


def test_delete_user(base_url, update_delete_user_endpoint):
    response = requests.delete(f"{base_url}{update_delete_user_endpoint}")
    assert response.status_code == 204
