from endpoints.get_item import GetItem


def test_get_item(item_id):
    get_item_endpoint = GetItem()
    get_item_endpoint.get_item_by_id(item_id)
    get_item_endpoint.check_status_is_200()