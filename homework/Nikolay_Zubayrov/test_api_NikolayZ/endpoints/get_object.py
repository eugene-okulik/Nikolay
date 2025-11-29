import requests
import allure
from .endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step('Get all objects')
    def get_all_objects(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        return self.response

    @allure.step('Get object by ID')
    def get_object_by_id(self, obj_id):
        self.response = requests.get(f'{self.url}/{obj_id}')
        self.json = self.response.json()
        return self.response
