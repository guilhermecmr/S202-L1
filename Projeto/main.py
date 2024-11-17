from database.database import Database
from crud.crud import FilmesCRUD
from cli.cli import FilmesCLI

db = Database("bolt://44.200.118.211", "neo4j", "expenditures-patch-distances")
filmes_crud = FilmesCRUD(db)
filmes_cli = FilmesCLI(filmes_crud)

####################### TESTE #######################
import os                                           #
from dados_teste import dados_teste                 #
os.system("cls" if os.name == "nt" else "clear")    #
dados_teste()                                       #
os.system("cls" if os.name == "nt" else "clear")    #
####################### TESTE #######################

if __name__ == "__main__":
    filmes_cli.menu()