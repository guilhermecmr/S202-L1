from database.database import Database
from crud.crud import FilmesCRUD
from cli.cli import FilmesCLI

db = Database("bolt://35.173.231.119", "neo4j", "crusts-knock-oscillators") # Conexão com o banco de dados
filmes_crud = FilmesCRUD(db) # CRUD de filmes
filmes_cli = FilmesCLI(filmes_crud) # CLI de filmes

if __name__ == "__main__":
    filmes_cli.menu() # Inicia o menu