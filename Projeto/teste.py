import os
import time
from neo4j import GraphDatabase
from unittest.mock import patch
from database.database import Database
from crud.crud import FilmesCRUD
from cli.cli import FilmesCLI

class Neo4jHandler:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()
    
    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]
    
    def clear_database(self):
        query = "MATCH (n) DETACH DELETE n"
        self.execute_query(query)


def dados_teste():
    os.system("cls" if os.name == "nt" else "clear")
    uri = "bolt://35.173.231.119"  
    user = "neo4j"  
    password = "crusts-knock-oscillators"  
    try:
        db = Neo4jHandler(uri, user, password)
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return
    
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
        os.system("cls" if os.name == "nt" else "clear")

def input_teste(filmes_cli):
    with open("input_teste.txt", 'r') as file:
        lines = file.readlines()
    inputs = iter(line.rstrip("\n") for line in lines)
    def input_with_delay(prompt):
        time.sleep(0.1)  
        print(prompt, end='') 
        response = next(inputs, "9")  
        print(response) 
        return response 
    with patch('builtins.input', input_with_delay):
        filmes_cli.menu()

db = Database("bolt://35.173.231.119", "neo4j", "crusts-knock-oscillators")
filmes_crud = FilmesCRUD(db)

def main():
    dados_teste()
    filmes_cli = FilmesCLI(filmes_crud)
    opcao = input("Utilizar inputs de teste? (y/n)\n")
    os.system("cls" if os.name == "nt" else "clear")
    if opcao == "y":
        input_teste(filmes_cli)
    else:
        filmes_cli.menu()

if __name__ == "__main__":
    main()