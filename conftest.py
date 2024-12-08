import datetime
from time import sleep

import petstore_async_api_client
import pytest
import requests
from requests.exceptions import ConnectionError


def pytest_configure(config):
    """Wait for the Application under test to start"""
    timeout_s = 60
    finish_time = datetime.datetime.now() + datetime.timedelta(timeout_s)
    while datetime.datetime.now() < finish_time:
        try:
            requests.get("http://nestjs_test_app:3000")
            return
        except ConnectionError:
            sleep(10)

    raise Exception("Application did not during the timeout")


@pytest.fixture(scope='session', autouse=False)
def async_api_configuration():
    return petstore_async_api_client.Configuration(host="https://petstore3.swagger.io/api/v3")
