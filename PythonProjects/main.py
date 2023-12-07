import requests

token = '44ccaa56153fd2c62129292c49d24acb'
host = 'https://api.pokemonbattle.me:9104'

response = requests.post(f'{host}/pokemons', json = {
    "name": "Iliana",
    "photo": "https://dolnikov.ru/pokemons/albums/095.png"
},headers = {'Content-Type'  :  'application/json',
               'trainer_token' : token } ) 

response_activation = requests.put ( f'{host}/pokemons', json = {
    "pokemon_id": "21351",
    "name": "Gus",
    "photo": "https://dolnikov.ru/pokemons/albums/095.png"
}, headers = {'Content-Type'  :  'application/json',
               'trainer_token' : token } )

response_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "21351"
},headers = {'Content-Type'  :  'application/json',
               'trainer_token' : token })

print(response_pokeball.text)