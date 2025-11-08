import requests
import pytest


@pytest.fixture(scope='session')
def all_tests():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def add_precondition():
    print("before test")
    yield
    print("after test")


@pytest.fixture()
def independent_condition():
    headers = {"Content-Type": "application/json"}
    body = {
        "name": "test_object",
        "data": {"color": "test_color", "size": "test_size"}
    }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    print(response.text)
    obj_id = response.json()["id"]
    yield obj_id
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{obj_id}')
    print(response.text)


def test_get_object(all_tests, add_precondition):
    # print(add_precondition)
    response = requests.get('http://objapi.course.qa-practice.com/object')
    print(response.text)
    assert response.status_code == 200


def test_get_object_id(add_precondition, independent_condition):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{independent_condition}')
    print(response.text)
    assert response.json()["id"] == independent_condition


@pytest.mark.parametrize("name, color, size", [
    ("kola", "blue", "mini"),
    ("oleg", "red", "large"),
    ("viktor", "green", "medium")
])
def test_post_object(all_tests, add_precondition, name, color, size):
    headers = {"Content-Type": "application/json"}
    body = {
        "name": name,
        "data": {"color": color, "size": size}
    }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)

    print(f"Создаём объект: {name}, {color}, {size}")
    print(response.text)

    assert response.status_code in [200, 201]
    response_data = response.json()
    assert response_data["name"] == name
    assert response_data["data"]["color"] == color
    assert response_data["data"]["size"] == size


@pytest.mark.critical
def test_put_object(add_precondition, independent_condition):
    headers = {"Content-Type": "application/json"}
    body = {
        "name": "vova1218",
        "data": {"color": "blue", "size": "mini"}
    }
    response = requests.put(f'http://objapi.course.qa-practice.com/object/{independent_condition}', json=body,
                            headers=headers)
    print(response.text)
    response_data = response.json()
    assert response_data["name"] == "vova1218"
    assert response.status_code == 200


@pytest.mark.medium
def test_patch_object(add_precondition, independent_condition):
    headers = {"Content-Type": "application/json"}
    body = {
        "name": "kola - vova1218",
        "data": {"color": "blue"}
    }

    response = requests.patch(f'http://objapi.course.qa-practice.com/object/{independent_condition}', json=body,
                              headers=headers)
    print(response.text)
    assert body["name"] == "kola - vova1218"
    assert response.status_code == 200


def test_delete_object(add_precondition, independent_condition):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{independent_condition}')
    print(response)
    print(response.status_code)
    assert response.status_code == 200
