import pytest
import requests

from endpoints.create_item import CreateItem
from endpoints.delete_item import DeleteItem


@pytest.fixture()
def item_id():
    create_item = CreateItem()
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_item.new_item(payload)
    yield create_item.res_json['id']
    delete_item = DeleteItem()
    delete_item.delete_item_by_id(create_item.res_json['id'])