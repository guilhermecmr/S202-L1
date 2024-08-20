from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

pokedex = Pokedex(database=db)

pokedex.get_pokemon_by_avg_spawns(10.0, 50.0)
pokedex.get_pokemon_by_weakness("Fire")
pokedex.get_pokemon_by_candy("Bulbasaur Candy")
pokedex.get_pokemon_by_minimum_multiplier(1.5)
pokedex.get_pokemon_by_candy_count(10, 50)