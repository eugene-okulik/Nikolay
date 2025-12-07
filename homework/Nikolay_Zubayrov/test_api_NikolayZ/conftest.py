import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject


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
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def object_id(create_object_endpoint, delete_object_endpoint):
    payload = {
        "name": "test_object",
        "data": {
            "color": "test_color",
            "size": "test_size"
        }
    }
    create_object_endpoint.create_new_object(payload)
    obj_id = create_object_endpoint.object_id
    yield obj_id
    delete_object_endpoint.delete_object(obj_id)
