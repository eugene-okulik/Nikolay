import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check that response status is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that response status is 201')
    def check_that_status_is_201(self):
        assert self.response.status_code == 201

    @allure.step('Check that name is correct')
    def check_response_name_is_correct(self, name):
        assert self.json['name'] == name

    @allure.step('Check that color is correct')
    def check_response_color_is_correct(self, color):
        assert self.json['data']['color'] == color

    @allure.step('Check that size is correct')
    def check_response_size_is_correct(self, size):
        assert self.json['data']['size'] == size

    @allure.step('Check that object ID exists')
    def check_response_id_is_not_none(self):
        assert self.json['id'] is not None

    @allure.step('Check that object ID matches')
    def check_object_id_matches(self, expected_id):
        assert self.json['id'] == expected_id
