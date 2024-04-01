from endpoints.delete_item import DeleteItem
from endpoints.get_item import GetItem


def test_delete_item(item_id):
    delete_item_endpoint = DeleteItem()
    delete_item_endpoint.delete_item_by_id(item_id)
    delete_item_endpoint.check_status_is_200()
    delete_item_endpoint.check_message_about_delete(item_id)
    get_item_endpoint = GetItem()
    get_item_endpoint.get_item_by_id(item_id)
    get_item_endpoint.check_status_is_404()