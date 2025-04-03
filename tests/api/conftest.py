import pytest


@pytest.fixture()
def base_url():
    return "https://reqres.in/api"


@pytest.fixture()
def list_users_endpoint():
    return "/users"
