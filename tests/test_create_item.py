from endpoints.create_item import CreateItem


def test_create_item():
    create_item_endpoint = CreateItem()
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_item_endpoint.new_item(payload=payload)
    create_item_endpoint.check_status_is_200()
    create_item_endpoint.check_name(payload['name'])










