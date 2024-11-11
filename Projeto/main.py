from database.database import Database
from crud.crud import FilmesCRUD
from cli.cli import FilmesCLI

db = Database("bolt://98.80.167.84", "neo4j", "occurrences-incentive-kites")
filmes_crud = FilmesCRUD(db)
filmes_cli = FilmesCLI(filmes_crud)

if __name__ == "__main__":
    filmes_cli.menu()