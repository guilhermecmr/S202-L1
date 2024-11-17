from neo4j import GraphDatabase

class Neo4jHandler:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()
    
    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            return session.run(query, parameters)
    
    def clear_database(self):
        query = "MATCH (n) DETACH DELETE n"
        self.execute_query(query)

def dados_teste():
    uri = "bolt://44.200.118.211"  
    user = "neo4j"  
    password = "expenditures-patch-distances"  
    db = Neo4jHandler(uri, user, password)
    
    try:
        print("Limpando a base de dados...")
        db.clear_database()
        print("Base de dados limpa com sucesso.")
        
        print("Inserindo filmes...")
        filmes_query = """
        CREATE (:Filme {nome: 'Nosferatu', ano: 1979, genero: 'Horror', duracao: 107}),
               (:Filme {nome: 'Deep Red', ano: 1975, genero: 'Horror', duracao: 127}),
               (:Filme {nome: 'Blue Velvet', ano: 1986, genero: 'Drama', duracao: 120}),
               (:Filme {nome: 'Chungking Express', ano: 1994, genero: 'Romance', duracao: 103}),
               (:Filme {nome: 'The Godfather', ano: 1972, genero: 'Drama', duracao: 175}),
               (:Filme {nome: 'The Big Lebowski', ano: 1998, genero: 'Comedy', duracao: 117}),
               (:Filme {nome: 'The Thing', ano: 1982, genero: 'Horror', duracao: 109}),
               (:Filme {nome: 'Blade Runner', ano: 118, genero: 'Sci-Fi', duracao: 118}),
               (:Filme {nome: 'Joint Security Area', ano: 2000, genero: 'Drama', duracao: 108})
        """
        db.execute_query(filmes_query)
        
        print("Inserindo membros...")
        membros_query = """
        CREATE (:Membro {nome: 'Werner Herzog', ano_nasc: 1942, nacionalidade: 'Alemanha', anos_carreira: 62, tipo: 'Diretor'}),
               (:Membro {nome: 'Dario Argento', ano_nasc: 1940, nacionalidade: 'Italia', anos_carreira: 58, tipo: 'Diretor'}),
               (:Membro {nome: 'David Hemmings', ano_nasc: 1941, nacionalidade: 'Inglaterra', anos_carreira: 49, tipo: 'Ator'}),
               (:Membro {nome: 'David Lynch', ano_nasc: 1946, nacionalidade: 'Americano', anos_carreira: 58, tipo: 'Diretor'}),
               (:Membro {nome: 'Faye Wong', ano_nasc: 1969, nacionalidade: 'China', anos_carreira: 35, tipo: 'Ator'}),
               (:Membro {nome: 'Joel Coen', ano_nasc: 1954, nacionalidade: 'EUA', anos_carreira: 40, tipo: 'Diretor'}),
               (:Membro {nome: 'Ethan Coen', ano_nasc: 1957, nacionalidade: 'EUA', anos_carreira: 40, tipo: 'Diretor'}),
               (:Membro {nome: 'Kurt Russell', ano_nasc: 1951, nacionalidade: 'EUA', anos_carreira: 61, tipo: 'Ator'}),
               (:Membro {nome: 'Keith David', ano_nasc: 1956, nacionalidade: 'EUA', anos_carreira: 45, tipo: 'Ator'})
        """
        db.execute_query(membros_query)
        
        print("Criando relacionamentos...")
        relacionamentos_query = """
        MATCH 
            (f1:Filme {nome: 'Nosferatu'}),
            (f2:Filme {nome: 'Deep Red'}),
            (f3:Filme {nome: 'Blue Velvet'}),
            (f4:Filme {nome: 'Chungking Express'}),
            (f5:Filme {nome: 'The Big Lebowski'}),
            (herzog:Membro {nome: 'Werner Herzog'}),
            (argento:Membro {nome: 'Dario Argento'}),
            (hemmings:Membro {nome: 'David Hemmings'}),
            (lynch:Membro {nome: 'David Lynch'}),
            (faye:Membro {nome: 'Faye Wong'}),
            (joel:Membro {nome: 'Joel Coen'}),
            (ethan:Membro {nome: 'Ethan Coen'})
        CREATE 
            (herzog)-[:DIRIGIU]->(f1),
            (argento)-[:DIRIGIU]->(f2),
            (hemmings)-[:ATUOU]->(f2),
            (lynch)-[:DIRIGIU]->(f3),
            (faye)-[:ATUOU]->(f4),
            (joel)-[:DIRIGIU]->(f5),
            (ethan)-[:DIRIGIU]->(f5)
        """
        db.execute_query(relacionamentos_query)
        
        print("Dados inseridos com sucesso!")
    
    finally:
        db.close()
        print("Conexão fechada.")