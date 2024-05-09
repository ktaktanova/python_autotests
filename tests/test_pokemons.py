import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'c17d4a5df7f071e9adb50df9c22dcc5e'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '4013'

def test_status_code():
    responce = requests.get(url= f'{URL}/pokemons', params= {'trainer_id': TRAINER_ID})
    assert responce.status_code == 200

def test_part_of_response():
    responce_get = requests.get(url= f'{URL}/pokemons', params= {'trainer_id': TRAINER_ID})
    assert responce_get.json()['data'][0]["name"] == 'Бульбазавр'


@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', TRAINER_ID), ('id', '26624')])
def test_parametrize(key, value): 
    responce_parametrize = requests.get(url= f'{URL}/pokemons', params= {'trainer_id': TRAINER_ID})
    assert responce_parametrize.json()["data"][0][key] == value

def test_get_trainers_status_code():
    responce = requests.get(url=f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert responce.status_code == 200

def test_trainer_id():
    responce =  requests.get(url=f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert responce.json()['data'][0]["id"]== '4013'

