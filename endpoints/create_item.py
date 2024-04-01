import requests

from endpoints.basa_endpoint import BaseEndpoint


class CreateItem(BaseEndpoint):
    def new_item(self, payload):
        self.res = requests.post("https://api.restful-api.dev/objects", json=payload)
        self.res_json = self.res.json()

    def check_name(self, name):
        assert self.res_json['name'] == name
