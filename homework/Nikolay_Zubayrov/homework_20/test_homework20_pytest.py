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


def test_get_object(add_precondition, all_tests):
    # print(add_precondition)
    response = requests.get('http://objapi.course.qa-practice.com/object')
    print(response.text)
    assert response.status_code == 200


def test_get_object_id(add_precondition, independent_condition):
    response = requests.get('http://objapi.course.qa-practice.com/object/4079')
    print(response.text)
    assert response.json()["id"] == "4079"


@pytest.mark.parametrize("name, color, size", [
    ("kola", "blue", "mini"),
    ("oleg", "red", "large"),
    ("viktor", "green", "medium")
])
def test_post_object(add_precondition, all_tests, name, color, size):
    headers = {"Content-Type": "application/json"}
    body = {
        "name": name,
        "data": {"color": color, "size": size}
    }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)

    print(f"Создаём объект: {name}, {color}, {size}")
    print(response.text)

    assert response.status_code in [200, 201]
    assert body["name"] == name
    assert body["data"]["color"] == color
    assert body["data"]["size"] == size


@pytest.mark.critical
def test_put_object(add_precondition, independent_condition):
    headers = {"Content-Type": "application/json"}
    body = {
        "name": "vova1218",
        "data": {"color": "blue", "size": "mini"}
    }
    response = requests.put('http://objapi.course.qa-practice.com/object/4079', json=body, headers=headers)
    print(response.text)
    assert body["name"] == "vova1218"


@pytest.mark.medium
def test_patch_object(add_precondition, independent_condition):
    headers = {"Content-Type": "application/json"}
    body = {
        "name": "kola - vova1218",
        "data": {"color": "blue"}
    }

    response = requests.patch('http://objapi.course.qa-practice.com/object/4079', json=body, headers=headers)
    print(response.text)

# def test_delete_object():
#     response = requests.delete('http://objapi.course.qa-practice.com/object/1')
#     print(response)
#     print(response.status_code)
