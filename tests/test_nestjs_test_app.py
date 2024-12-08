import requests


class TestApp:
    def test_hello(self):
        response = requests.get('http://nestjs_test_app:3000/hello')
        assert response.status_code == 200
