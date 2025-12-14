from locust import task, HttpUser
import random


class MemeUser(HttpUser):
    host = 'http://objapi.course.qa-practice.com'
    users_data = [
        {'name': 'Kola', 'data': {'color': 'blue', 'size': 'mini'}},
        {'name': 'Vova', 'data': {'color': 'red', 'size': 'big'}},
        {'name': 'Oleg', 'data': {'color': 'green', 'size': 'average'}}
    ]

    meme_ids = [1, 2, 3, 4, 5]

    @task(1)
    def get_all_memes(self):
        self.client.get('/object')

    @task(1)
    def get_memes_id(self):
        meme_id = random.choice(self.meme_ids)
        self.client.get(f'/object/{meme_id}')

    @task(3)
    def post_memes(self):
        user = random.choice(self.users_data)
        body = {
            'name': user['name'],
            'data': {'color': user['data']['color'], 'size': user['data']['size']}
        }
        headers = {"Content-Type": 'application/json'}
        self.client.post(
            '/object', json=body,
            headers=headers)

    @task(1)
    def put_memes(self):
        meme_id = random.choice(self.meme_ids)
        body = {
            'name': 'Vovan1218',
            'data': {'color': 'black', 'size': 'huge'}
        }
        headers = {"Content-Type": 'application/json'}
        self.client.put(f'/object/{meme_id}', json=body, headers=headers)

    @task(1)
    def patch_memes(self):
        meme_id = random.choice(self.meme_ids)
        body = {
            'name': 'Vovan1218',
            'data': {'color': 'gold', 'size': 'huge'}
        }
        headers = {"Content-Type": 'application/json'}
        self.client.patch(f'/object/{meme_id}', json=body, headers=headers)

    @task(1)
    def delete_memes(self):
        meme_id = random.choice(self.meme_ids)
        self.client.delete(f'/object/{meme_id}')
