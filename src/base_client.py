import requests
import json
import allure

class BaseClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.headers = {"Content-Type": "application/json"}

    def get(self, endpoint):
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        return requests.get(url, headers=self.headers)

    def post(self, endpoint, payload):
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        response = requests.post(url, json=payload, headers=self.headers)

        allure.attach(
            json.dumps(payload, indent=4),
            name="Request Body",
            attachment_type=allure.attachment_type.JSON
        )
        allure.attach(
            json.dumps(response.json(), indent=4),
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
        )
        return response