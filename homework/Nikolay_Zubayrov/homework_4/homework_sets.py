my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [4, 'text', 7, 3.5, 'world'],
    'dict': {'name': 'Ivan', 'age': 20, 'city': 'Moskow', 'car': 'Volvo', 'gender': 'man'},
    'set': {2, 8, 'hello', 3.7, 11}

}

my_dict['tuple'][-1]
print(my_dict['tuple'][-1])

my_dict['list'].append('Hello')
print(my_dict['list'])
my_dict['list'].pop(1)
print(my_dict['list'])

my_dict['dict'][('i am a tuple',)] = 'yes'
print(my_dict['dict'])
my_dict['dict'].pop('name')
print(my_dict['dict'])

my_dict['set'].add(0)
print(my_dict['set'])
my_dict['set'].remove(11)
print(my_dict['set'])
