import requests
import pytest
import allure
from allure_commons.types import Severity


@allure.epic("Object Management API")
@allure.feature("CRUD Operations")
class TestObjectAPI:

    @allure.story("Get all objects")
    @allure.title("Get list of all objects")
    @allure.severity(Severity.BLOCKER)
    @allure.tag("smoke", "get")
    @allure.description("Test to verify GET /object endpoint returns all objects with status 200")
    def test_get_object(self, all_tests, add_precondition):
        with allure.step("Send GET request to /object endpoint"):
            response = requests.get('http://objapi.course.qa-practice.com/object')

        with allure.step("Verify response status code and structure"):
            allure.attach(f"Response: {response.text}", name="API Response",
                          attachment_type=allure.attachment_type.TEXT)
            assert response.status_code == 200

    @allure.story("Get object by ID")
    @allure.title("Get specific object by ID")
    @allure.severity(Severity.CRITICAL)
    @allure.tag("get", "by_id")
    @allure.description("Test to verify GET /object/{id} endpoint returns correct object")
    def test_get_object_id(self, add_precondition, independent_condition):
        with allure.step(f"Send GET request to /object/{independent_condition}"):
            response = requests.get(f'http://objapi.course.qa-practice.com/object/{independent_condition}')

        with allure.step("Verify object ID in response matches requested ID"):
            allure.attach(f"Requested ID: {independent_condition}\nResponse: {response.text}",
                          name="Request/Response Data", attachment_type=allure.attachment_type.TEXT)
            assert response.json()["id"] == independent_condition

    @allure.story("Create new object")
    @allure.title("Create object with parameters: {name}, {color}, {size}")
    @allure.severity(Severity.CRITICAL)
    @allure.tag("post", "create")
    @allure.description("Test to verify POST /object endpoint creates new object with provided data")
    @pytest.mark.parametrize("name, color, size", [
        ("kola", "blue", "mini"),
        ("oleg", "red", "large"),
        ("viktor", "green", "medium")
    ])
    def test_post_object(self, all_tests, add_precondition, name, color, size):
        headers = {"Content-Type": "application/json"}
        body = {
            "name": name,
            "data": {"color": color, "size": size}
        }

        with allure.step(f"Prepare request body for {name}"):
            allure.attach(str(body), name="Request Body", attachment_type=allure.attachment_type.JSON)

        with allure.step("Send POST request to create object"):
            response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)

        with allure.step("Verify object creation response"):
            print(f"Создаём объект: {name}, {color}, {size}")
            allure.attach(f"Response: {response.text}", name="Creation Response",
                          attachment_type=allure.attachment_type.TEXT)


            assert response.status_code in [200, 201]
            response_data = response.json()
            assert response_data["name"] == name
            assert response_data["data"]["color"] == color
            assert response_data["data"]["size"] == size

    @allure.story("Update object")
    @allure.title("Full update of object using PUT")
    @allure.severity(Severity.CRITICAL)
    @allure.tag("put", "update")
    @allure.description("Test to verify PUT /object/{id} endpoint fully updates object data")
    @pytest.mark.critical
    def test_put_object(self, add_precondition, independent_condition):
        headers = {"Content-Type": "application/json"}
        body = {
            "name": "vova1218",
            "data": {"color": "blue", "size": "mini"}
        }

        with allure.step(f"Prepare PUT request for object {independent_condition}"):
            allure.attach(str(body), name="PUT Request Body", attachment_type=allure.attachment_type.JSON)

        with allure.step(f"Send PUT request to /object/{independent_condition}"):
            response = requests.put(f'http://objapi.course.qa-practice.com/object/{independent_condition}', json=body,
                                    headers=headers)

        with allure.step("Verify update was successful"):
            allure.attach(f"Response: {response.text}", name="PUT Response",
                          attachment_type=allure.attachment_type.TEXT)
            response_data = response.json()
            assert response_data["name"] == "vova1218"
            assert response.status_code == 200

    @allure.story("Partial update object")
    @allure.title("Partial update of object using PATCH")
    @allure.severity(Severity.NORMAL)
    @allure.tag("patch", "partial_update")
    @allure.description("Test to verify PATCH /object/{id} endpoint partially updates object data")
    @pytest.mark.medium
    def test_patch_object(self, add_precondition, independent_condition):
        headers = {"Content-Type": "application/json"}
        body = {
            "name": "kola - vova1218",
            "data": {"color": "blue"}
        }

        with allure.step(f"Prepare PATCH request for object {independent_condition}"):
            allure.attach(str(body), name="PATCH Request Body", attachment_type=allure.attachment_type.JSON)

        with allure.step(f"Send PATCH request to /object/{independent_condition}"):
            response = requests.patch(f'http://objapi.course.qa-practice.com/object/{independent_condition}', json=body,
                                      headers=headers)

        with allure.step("Verify partial update was successful"):
            allure.attach(f"Response: {response.text}", name="PATCH Response",
                          attachment_type=allure.attachment_type.TEXT)
            assert body["name"] == "kola - vova1218"
            assert response.status_code == 200

    @allure.story("Delete object")
    @allure.title("Delete object by ID")
    @allure.severity(Severity.CRITICAL)
    @allure.tag("delete", "cleanup")
    @allure.description("Test to verify DELETE /object/{id} endpoint removes object")
    def test_delete_object(self, add_precondition, independent_condition):
        with allure.step(f"Send DELETE request to /object/{independent_condition}"):
            response = requests.delete(f'http://objapi.course.qa-practice.com/object/{independent_condition}')

        with allure.step("Verify deletion was successful"):
            allure.attach(f"Status Code: {response.status_code}", name="Delete Response",
                          attachment_type=allure.attachment_type.TEXT)
            print(response)
            print(response.status_code)
            assert response.status_code == 200