import requests

from endpoints.basa_endpoint import BaseEndpoint


class DeleteItem(BaseEndpoint):
    def delete_item_by_id(self, item_id):
        self.res = requests.delete(f"https://api.restful-api.dev/objects/{item_id}")
        self.res_json = self.res.json()

    def check_message_about_delete(self, item_id):
        assert self.res_json['message'] == f"Object with id = {item_id} has been deleted."