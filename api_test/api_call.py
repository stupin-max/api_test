import requests
from requests import Response


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status_code = status
        self.response = response


class Client():
    def custom_request(method: str, url: str, **kwargs) -> Response:
        response = requests.request(method, url, **kwargs)
        return ResponseModel(status = response.status_code, response = response.json())


class api_get:
    def __init__(self, url, endpoint):
        self.url = url
        self.endpoint = endpoint

    def send_get(self):
        response = Client.custom_request("GET", f"{self.url}{self.endpoint}")
        return response
