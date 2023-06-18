import time
import data_management as dm
import json
from random import randint
# str_json = """
# {
#   "squadName": "Super hero squad",
#   "homeTown": "Metro City",
#   "formed": 2016,
#   "secretBase": "Super tower",
#   "active": true,
#   "members": [
#     {
#       "name": "петя Molecule Man",
#       "age": 29,
#       "secretIdentity": "Dan Jukes"
#     },
#     {
#       "name": "Madame Uppercut",
#       "age": 39,
#       "secretIdentity": "Jane Wilson"
#     }
#   ]
# }
#
# """
#
# print(type(str_json))
# data = json.loads(str_json)
# print(data['members'])
#
# for i in data['members']:
#     del i['secretIdentity']
#     i['likes'] = randint(0, 10)
#
#
# print(data['members'])

# new_json = json.dumps(data, indent=2)
# print(new_json)

with open('data.json', 'r') as file:
    data = json.load(file)

print(type(data['notes'][-1]['id']))
# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=2)
