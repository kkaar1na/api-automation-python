import requests

class BaseClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.headers = {"Content-Type": "application/json"}

    def get(self, endpoint):
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        return requests.get(url, headers=self.headers)

    def post(self, endpoint, payload):
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        return requests.post(url, json=payload, headers=self.headers)