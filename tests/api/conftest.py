import pytest


@pytest.fixture()
def base_url():
    return "https://reqres.in/api"


@pytest.fixture()
def list_users_endpoint():
    return "/users"


@pytest.fixture()
def register_user_endpoint():
    return "/register"


@pytest.fixture()
def update_delete_user_endpoint():
    return f"/users/1"
