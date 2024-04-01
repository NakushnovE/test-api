import requests

from endpoints.basa_endpoint import BaseEndpoint


class UpdateItem(BaseEndpoint):
    def update_item_by_id(self, item_id, payload):
        self.res = requests.put(
            f"https://api.restful-api.dev/objects/{item_id}",
            json=payload
        )
        self.res_json = self.res.json()

    def check_response_name(self, name):
        assert self.res_json['name'] == name