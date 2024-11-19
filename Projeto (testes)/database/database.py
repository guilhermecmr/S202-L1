from neo4j import GraphDatabase

class Database:
    # Construtor
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    # Funcao que fecha a conexao com o banco de dados
    def close(self):
        self.driver.close()

    # Funcao que executa uma query no banco de dados
    def query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]