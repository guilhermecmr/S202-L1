from database.database import Database
from game_database.game_database import GameDatabase

db = Database("bolt://54.205.26.222", "neo4j", "barrel-distributions-correspondence")
db.drop_all()
game_db = GameDatabase(db.driver)

game_db.create_player("1", "Jorge")
game_db.create_player("2", "Marcelo")
game_db.create_player("3", "Augusto")

game_db.update_player("1", "Jorge Lafond")

game_db.create_match("64", ["1", "2"], {"1": 10, "2": 5})

game_db.delete_player("3")

print(game_db.get_player_by_id("1"))

print(game_db.get_match_by_id("64"))

print(game_db.get_player_matches("1"))

db.close()