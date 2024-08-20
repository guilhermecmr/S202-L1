from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self.database = database

    def get_pokemon_by_weakness(self, weakness: str):
        resposta = list(self.database.collection.find({"weaknesses": {"$in": [weakness]}}))
        writeAJson(resposta, "pokemon_by_weakness")
        return resposta

    def get_pokemon_by_candy_count(self, min_candy: int, max_candy: int):
        resposta = list(self.database.collection.find({"candy_count": {"$gte": min_candy, "$lte": max_candy}}))
        writeAJson(resposta, "pokemon_by_candy_count")
        return resposta
    
    def get_pokemon_by_avg_spawns(self, min_avg_spawns: float, max_avg_spawns: float):
        resposta = list(self.database.collection.find({"avg_spawns": {"$gte": min_avg_spawns, "$lte": max_avg_spawns}}))
        writeAJson(resposta, "pokemon_by_avg_spawns")
        return resposta

    def get_pokemon_by_candy(self, candy_name: str):
        resposta = list(self.database.collection.find({"candy": candy_name}))
        writeAJson(resposta, "pokemon_by_candy")
        return resposta

    def get_pokemon_by_minimum_multiplier(self, min_multiplier: float):
        resposta = list(self.database.collection.find({"multipliers": {"$elemMatch": {"$gte": min_multiplier}}}))
        writeAJson(resposta, "pokemon_by_minimum_multiplier")
        return resposta