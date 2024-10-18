class GameDatabase:
    def __init__(self, driver):
        self.driver = driver
    
    def create_player(self, player_id, nome):
        with self.driver.session() as session:
            session.run(
                "CREATE (p:Player {id: $player_id, nome: $nome})",
                player_id=player_id, nome=nome
            )

    def update_player(self, player_id, novo_nome):
        with self.driver.session() as session:
            session.run(
                "MATCH (p:Player {id: $player_id}) "
                "SET p.nome = $novo_nome",
                player_id=player_id, novo_nome=novo_nome
            )

    def delete_player(self, player_id):
        with self.driver.session() as session:
            session.run(
                "MATCH (p:Player {id: $player_id}) "
                "DETACH DELETE p",
                player_id=player_id
            )

    def create_match(self, match_id, player_id, results):
        with self.driver.session() as session:
            session.run(
                "CREATE (m:Match {id: $match_id})",
                match_id=match_id
            )
            
            for player_id, pontuacao in results.items():
                session.run(
                    "MATCH (p:Player {id: $player_id}), (m:Match {id: $match_id}) "
                    "CREATE (p)-[:JOGOU_PARTIDA {pontuacao: $pontuacao}]->(m)",
                    player_id=player_id, match_id=match_id, pontuacao=pontuacao
                )

    def get_player_by_id(self, player_id):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (p:Player {id: $player_id}) RETURN p.id AS id, p.nome AS nome",
                player_id=player_id
            )
            player = result.single()
            if player:
                return {"id": player["id"], "nome": player["nome"]}
            return None

    def get_match_by_id(self, match_id):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (m:Match {id: $match_id}) "
                "MATCH (p:Player)-[r:JOGOU_PARTIDA]->(m) "
                "RETURN m.id AS match_id, p.id AS player_id, r.pontuacao AS pontuacao",
                match_id=match_id
            )
            match = {}
            for record in result:
                if "match_id" not in match:
                    match["match_id"] = record["match_id"]
                if "players" not in match:
                    match["players"] = []
                match["players"].append({
                    "player_id": record["player_id"],
                    "pontuacao": record["pontuacao"]
                })
            return match if match else None

    def get_player_matches(self, player_id):
        with self.driver.session() as session:
            result = session.run(
                "MATCH (p:Player {id: $player_id})-[:JOGOU_PARTIDA]->(m:Match) "
                "RETURN m.id AS match_id",
                player_id=player_id
            )
            matches = [record["match_id"] for record in result]
            return matches