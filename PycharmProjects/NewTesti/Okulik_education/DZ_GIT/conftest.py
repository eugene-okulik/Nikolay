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
