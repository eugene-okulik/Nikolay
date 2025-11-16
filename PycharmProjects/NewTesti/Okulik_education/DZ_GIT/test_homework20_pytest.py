import requests
import pytest
import allure


@allure.story('Get object')
@allure.title('Get list of all object')
@allure.tag('get')
def test_get_object(all_tests, add_precondition):
    # print(add_precondition)
    with allure.step('Run get request'):
        response = requests.get('http://objapi.course.qa-practice.com/object')
    with allure.step('Check status code'):
        print(response.text)
        assert response.status_code == 200


@allure.story('Get object id')
@allure.title('Get a list of objects by id')
@allure.tag('get')
def test_get_object_id(add_precondition, independent_condition):
    with allure.step('Run get request id'):
        response = requests.get(f'http://objapi.course.qa-practice.com/object/{independent_condition}')
        print(response.text)
    with allure.step(f'Check id = {independent_condition}'):
        assert response.json()["id"] == independent_condition


@pytest.mark.parametrize("name, color, size", [
    ("kola", "blue", "mini"),
    ("oleg", "red", "large"),
    ("viktor", "green", "medium")
])
@allure.story('Create new object')
@allure.title('Create object with parameters: {name}, {color}, {size}')
@allure.tag('post')
def test_post_object(all_tests, add_precondition, name, color, size):
    headers = {"Content-Type": "application/json"}
    body = {
        "name": name,
        "data": {"color": color, "size": size}
    }
    with allure.step('Create new object'):
        response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)

        print(f"Создаём объект: {name}, {color}, {size}")
        print(response.text)
    with allure.step('Check status code'):
        assert response.status_code in [200, 201]
    with allure.step(f'Check params {name}, {color}, {size}'):
        response_data = response.json()
        assert response_data["name"] == name
        assert response_data["data"]["color"] == color
        assert response_data["data"]["size"] == size


@pytest.mark.critical
@allure.story('Change object')
@allure.tag('put')
def test_put_object(add_precondition, independent_condition):
    headers = {"Content-Type": "application/json"}
    body = {
        "name": "vova1218",
        "data": {"color": "blue", "size": "mini"}
    }
    with allure.step('Change object'):
        response = requests.put(f'http://objapi.course.qa-practice.com/object/{independent_condition}', json=body,
                                headers=headers)
        print(response.text)
    with allure.step('Check params'):
        response_data = response.json()
        assert response_data["name"] == "vova1218"
        assert response.status_code == 200


@pytest.mark.medium
@allure.story('Change object')
@allure.tag('patch')
def test_patch_object(add_precondition, independent_condition):
    headers = {"Content-Type": "application/json"}
    body = {
        "name": "kola - vova1218",
        "data": {"color": "blue"}
    }
    with allure.step('Change object'):
        response = requests.patch(f'http://objapi.course.qa-practice.com/object/{independent_condition}', json=body,
                                  headers=headers)
        print(response.text)
    with allure.step('Check params'):
        assert body["name"] == "kola - vova1218"
        assert response.status_code == 200


@allure.story('Delete object')
@allure.tag('delete')
def test_delete_object(add_precondition, independent_condition):
    with allure.step('Delete object'):
        response = requests.delete(f'http://objapi.course.qa-practice.com/object/{independent_condition}')
        print(response)
        print(response.status_code)
    with allure.step('Check status code'):
        assert response.status_code == 200
