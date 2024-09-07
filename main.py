import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Свин",
    "photo_id": 915
}

responce_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(responce_create.text)
pokemon_id = responce_create.json()['id']

body_change = {
    "pokemon_id": pokemon_id,
    "name": "Мистер Свин",
    "photo_id": 916
}

responce_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(responce_change.text)

body_pokeball = {
    "pokemon_id": pokemon_id
}

responce_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(responce_pokeball.text)