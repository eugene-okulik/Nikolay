import pytest
import allure

TEST_DATA = [
    {"name": "kola", "data": {"color": "blue", "size": "mini"}},
    {"name": "oleg", "data": {"color": "red", "size": "large"}},
    {"name": "viktor", "data": {"color": "green", "size": "medium"}}
]

PUT_DATA = {
    "name": "vova1218",
    "data": {"color": "blue", "size": "mini"}

}

PATCH_DATA = {
    "name": "kola - vova1218",
    "data": {"color": "blue"}
}


@allure.story('Create new object')
@allure.tag('post')
@pytest.mark.parametrize('data', TEST_DATA)
def test_create_new_object(all_tests, add_precondition, create_object_endpoint, data):
    create_object_endpoint.create_new_object(payload=data)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_name_is_correct(data['name'])
    create_object_endpoint.check_response_color_is_correct(data['data']['color'])
    create_object_endpoint.check_response_size_is_correct(data['data']['size'])
    create_object_endpoint.check_response_id_is_not_none()


@allure.story('Get object')
@allure.title('Get list of all objects')
@allure.tag('get')
def test_get_all_objects(get_object_endpoint, add_precondition):
    get_object_endpoint.get_all_objects()
    get_object_endpoint.check_that_status_is_200()


@allure.story('Get object id')
@allure.title('Get object by id')
@allure.tag('get')
def test_get_object_by_id(add_precondition, get_object_endpoint, object_id):
    get_object_endpoint.get_object_by_id(object_id)
    get_object_endpoint.check_that_status_is_200()
    get_object_endpoint.check_object_id_matches(object_id)
    assert len(get_object_endpoint.json) > 0


@allure.story('Change object')
@allure.tag('put')
@pytest.mark.critical
def test_put_object(add_precondition, update_object_endpoint, object_id):
    update_object_endpoint.update_object_put(object_id, PUT_DATA)
    update_object_endpoint.check_that_status_is_200()
    update_object_endpoint.check_response_name_is_correct(PUT_DATA['name'])
    update_object_endpoint.check_response_color_is_correct(PUT_DATA['data']['color'])
    update_object_endpoint.check_response_size_is_correct(PUT_DATA['data']['size'])


@allure.story('Change object')
@allure.tag('patch')
@pytest.mark.medium
def test_patch_object(add_precondition, update_object_endpoint, object_id):
    update_object_endpoint.update_object_patch(object_id, PATCH_DATA)
    update_object_endpoint.check_that_status_is_200()
    update_object_endpoint.check_response_name_is_correct(PATCH_DATA['name'])
    update_object_endpoint.check_response_color_is_correct(PATCH_DATA['data']['color'])


@allure.story('Delete object')
@allure.tag('delete')
def test_delete_object(add_precondition, delete_object_endpoint, object_id):
    delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_that_status_is_200()
