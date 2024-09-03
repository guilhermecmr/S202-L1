from database.database import Database
from helper.writeAJson import writeAJson
from model.livrosModel import LivrosModel
from cli.cli import LivrosCLI

db = Database(database="biblioteca", collection="livros")
db.resetDatabase()
livrosModel = LivrosModel(database=db)

livrosCLI = LivrosCLI(livrosModel)
livrosCLI.run()