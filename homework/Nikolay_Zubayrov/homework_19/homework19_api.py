import requests


def get_posts():
    response = requests.get('http://objapi.course.qa-practice.com/object')
    print(response.text)


get_posts()


def get_posts_id():
    response = requests.get('http://objapi.course.qa-practice.com/object/3249')
    print(response.text)


get_posts_id()


#
#
def post_object():
    headers = {"Content-Type": "application/json"}
    body = {
        "name": "kola",
        "data": {"color": "blue", "size": "mini"}
    }
    response = requests.post('http://objapi.course.qa-practice.com/object', json=body, headers=headers)
    print(response.text)


post_object()


#
#
def put_object():
    headers = {"Content-Type": "application/json"}
    body = {
        "name": "kola - vova",
        "data": {"color": "blue", "size": "mini"}
    }
    response = requests.put('http://objapi.course.qa-practice.com/object/3249', json=body, headers=headers)
    print(response.text)


put_object()


#
#
def patch_object():
    headers = {"Content-Type": "application/json"}
    body = {

        "name": "kola - vova1218",
        "data": {"color": "blue", "size": "mini"}
    }
    response = requests.patch('http://objapi.course.qa-practice.com/object/3249', json=body, headers=headers)
    print(response.text)


patch_object()


def delete_object():
    response = requests.delete('http://objapi.course.qa-practice.com/object/1')
    print(response)
    print(response.status_code)


delete_object()
