import requests
import allure
from .endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete object by ID')
    def delete_object(self, obj_id):
        self.response = requests.delete(f'{self.url}/{obj_id}')
        return self.response
