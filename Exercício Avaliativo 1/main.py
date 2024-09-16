from database.database import Database
from cli.MotoristaCLI import MotoristaCLI
from dao.MotoristaDAO import MotoristaDAO 

db = Database(database="Aplicativo", collection="Motoristas")
db.resetDatabase()

motorista_dao = MotoristaDAO(database=db)

motoristaCLI = MotoristaCLI(motorista_dao)
motoristaCLI.menu()