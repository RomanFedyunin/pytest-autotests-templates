import petstore_async_api_client
import pytest


@pytest.fixture(scope='session', autouse=False)
def async_api_configuration():
    return petstore_async_api_client.Configuration(host="https://petstore3.swagger.io/api/v3")
