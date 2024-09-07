import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '5115'

def test_status_code():
    responce = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert responce.status_code == 200

def test_trainer_name():
    responce_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert responce_get.json()['data'][0]['trainer_name'] == 'Руслан'


@pytest.mark.parametrize('key, value', [('trainer_name', 'Руслан'),('city', 'Уфа'),('id', '5115')])
def test_param(key, value):
    responce_param = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert responce_param.json()['data'][0][key] == value