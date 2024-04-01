import requests

from endpoints.basa_endpoint import BaseEndpoint


class GetItem(BaseEndpoint):
    def get_item_by_id(self, item_id):
        self.res = requests.get(f"https://api.restful-api.dev/objects/{item_id}")
        self.res_json = self.res.json()

    def check_response_id(self, item_id):
        assert self.res_json['id'] == item_id