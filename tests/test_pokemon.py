import pytest
import requests

host = 'https://api.pokemonbattle.ru'
api_version = 'v2'
trainer_id = 12852

def test_trainer_status_code():
    trainers = requests.get(url = f"{host}/{api_version}/trainers")
    assert trainers.status_code == 200

@pytest.mark.parametrize('key, value', [("trainer_name", "VseYasno")])
def test_parametrize(key, value):
    trainer = requests.get(url = f"{host}/{api_version}/trainers", params= { "trainer_id": trainer_id })
    assert trainer.json()["data"][0][key] == value