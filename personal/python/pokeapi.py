#get pokeapi
import requests
import json
import wget

def get_sprite(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    json = requests.get(url).json()
    sprite = json['sprites']['front_default']
    wget.download(sprite)

pokemonurl = "https://pokeapi.co/api/v2/pokemon/"
pokemonspeciesurl = "https://pokeapi.co/api/v2/pokemon-species/"
fullpokejson = requests.get(pokemonurl).json()
print(fullpokejson['count'])

for i in range(fullpokejson['count']):
    pokeurl = pokemonurl + str(i)
    resp = requests.get(pokeurl)
    if resp.status_code == 404:
        print("not found in ",i)
        continue
    else:
        pokespurl = pokemonspeciesurl + str(i)
        spjson = requests.get(pokespurl).json()
        if spjson['is_legendary'] == True or spjson['is_mythical'] == True:
            get_sprite(str(i))