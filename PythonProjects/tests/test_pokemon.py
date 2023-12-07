import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '44ccaa56153fd2c62129292c49d24acb'


def test_status_code():
    respons = requests.get(f'{host}/trainers', params = {"trainer_id": 3805})
    assert  respons.status_code == 200