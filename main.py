import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'c17d4a5df7f071e9adb50df9c22dcc5e'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "kseniawus@yandex.ru",
    "password": "7Cm-4hh-gLe-FEN"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_change = {
    "pokemon_id": "26621",
    "name": "Helldiver",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_add_pokeball = {
    "pokemon_id": "26621"
}

'''responce = requests.post(url = f'{URL}/trainers/reg', headers= HEADER, json= body_registration)
print(responce.text)'''

'''responce_confirmation = requests.post(url= f'{URL}/trainers/confirm_email', headers= HEADER, json = body_confirmation)
print(responce_confirmation.text)'''


#Создание покемона
'''responce_create = requests.post(url= f'{URL}/pokemons', headers= HEADER, json = body_create)
print(responce_create.text)

message = responce_create.json()['message']
print(message)'''

#Смена имени покемона
'''responce_change = requests.put(url= f'{URL}/pokemons', headers= HEADER, json= body_change)
print(responce_change.text)'''

#Поймать покемона в покебол
responce_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json= body_add_pokeball)
print(responce_add_pokeball.text)
