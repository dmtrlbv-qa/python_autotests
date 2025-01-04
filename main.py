import requests

host = 'https://api.pokemonbattle.ru'
api_version = 'v2'
token = 'YOUR_TRAINER_TOKEN'

headers = {
    "Content-Type": "application/json",
    "trainer_token": token
}

create_pokemon = requests.post(url = f"{host}/{api_version}/pokemons", headers = headers, json={ "name": "Бульбазавр", "photo_id": -1})
pokemon_id = str(create_pokemon.json()['id'])
print(create_pokemon.json())
change_pokemons_name = requests.put(url = f"{host}/{api_version}/pokemons", headers = headers, json={ "pokemon_id": pokemon_id, "name": "Пупс", "photo_id": -1})
print(change_pokemons_name.json())
catch_pokemon = requests.post(url = f"{host}/{api_version}/trainers/add_pokeball", headers = headers, json={ "pokemon_id": pokemon_id })
print(catch_pokemon.json())
knockout_pokemon = requests.post(url = f"{host}/{api_version}/pokemons/knockout", headers = headers, json={ "pokemon_id": pokemon_id })
print(knockout_pokemon.json())