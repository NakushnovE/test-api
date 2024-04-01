from endpoints.update_item import UpdateItem


def test_update_item(item_id):
    payload = {
       "name": "Apple MacBook Pro 16",
       "data": {
          "year": 2023,
          "price": 2333.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "3 TB",
          "color": "silver"
       }
    }
    update_item_endpoint = UpdateItem()
    update_item_endpoint.update_item_by_id(item_id, payload=payload)

    update_item_endpoint.check_status_is_200()
    update_item_endpoint.check_response_name(payload['name'])