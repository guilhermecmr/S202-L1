from pymongo import MongoClient
from database.database import Database
from model.Motorista import Motorista
from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, database: Database):
        self.db = database

    def create_motorista(self, motorista: Motorista):
        try:
            motorista_data = {
                "nota": motorista.nota,
                "corridas": [{
                    "nota": corrida.nota,
                    "distancia": corrida.distancia,
                    "valor": corrida.valor,
                    "passageiro": {
                        "nome": corrida.passageiro.nome,
                        "documento": corrida.passageiro.documento
                    }
                } for corrida in motorista.corridas]
            }
            result = self.db.collection.insert_one(motorista_data)
            return result.inserted_id
        except Exception as e:
            print(f"Erro ao criar motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            result = self.db.collection.find_one({"_id": ObjectId(id)})
            if result:
                # Extraindo e formatando os dados
                nota = result.get('nota', 'N/A')
                corridas = result.get('corridas', [])

                print("\nDados do motorista:")
                print(f"Nota: {nota}")
                print("Corridas:")

                for i, corrida in enumerate(corridas):
                    print(f" Corrida {i}:")
                    corrida_nota = corrida.get('nota', 'N/A')
                    distancia = corrida.get('distancia', 'N/A')
                    valor = corrida.get('valor', 'N/A')
                    passageiro = corrida.get('passageiro', {})
                    nome = passageiro.get('nome', 'N/A')
                    documento = passageiro.get('documento', 'N/A')

                    print(f"  Nota: {corrida_nota}")
                    print(f"  Distância: {distancia}")
                    print(f"  Valor: {valor}")
                    print(f"  Passageiro:")
                    print(f"   Nome: {nome}")
                    print(f"   Documento: {documento}")
            else:
                print("Motorista não encontrado.")
            return result
        except Exception as e:
            print(f"Erro ao ler motorista: {e}")
            return None

    def update_motorista(self, id: str, dado_update: dict):
        try:
            result = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": dado_update})
            if result.modified_count:
                print("Motorista atualizado com sucesso!")
            else:
                print("Motorista não encontrado.")
            return result.modified_count
        except Exception as e:
            print(f"Erro ao atualizar motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            result = self.db.collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count:
                print("\nMotorista deletado com sucesso!")
            else:
                print("\nMotorista não encontrado.")
            return result.deleted_count
        except Exception as e:
            print(f"\nErro ao deletar o motorista: {e}")
            return None