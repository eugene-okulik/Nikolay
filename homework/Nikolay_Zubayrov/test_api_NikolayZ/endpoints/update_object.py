import requests
import allure
from .endpoint import Endpoint


class UpdateObject(Endpoint):

    @allure.step('Update object using PUT')
    def update_object_put(self, obj_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{obj_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Update object using PATCH')
    def update_object_patch(self, obj_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{obj_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
