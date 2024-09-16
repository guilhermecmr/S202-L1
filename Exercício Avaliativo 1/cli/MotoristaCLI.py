from model.Motorista import Motorista
from model.Corrida import Corrida
from model.Passageiro import Passageiro
from dao.MotoristaDAO import MotoristaDAO

class MotoristaCLI:
    def __init__(self, motorista_dao: MotoristaDAO):
        self.motorista_dao = motorista_dao

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Criar Motorista")
            print("2. Ler Motorista")
            print("3. Atualizar Motorista")
            print("4. Remover Motorista")
            print("5. Sair")

            opcao = input("Selecione uma opcao: ")

            if opcao == "1":
                self.criar_motorista()
            elif opcao == "2":
                self.ler_motorista()
            elif opcao == "3":
                self.atualizar_motorista()
            elif opcao == "4":
                self.remover_motorista()
            elif opcao == "5":
                print("\nEncerrando o programa...")
                break
            else:
                print("Opcao invalida!")

    def criar_motorista(self):
        nota_motorista = int(input("\nNota do motorista: "))
        corridas = []
        
        while True:
            nota_corrida = int(input("Nota da corrida: "))
            distancia = float(input("Distância da corrida: "))
            valor = float(input("Valor da corrida: "))
            nome_passageiro = input("Nome do passageiro: ")
            documento_passageiro = input("Documento do passageiro: ")
            
            passageiro = Passageiro(nome_passageiro, documento_passageiro)
            corrida = Corrida(nota_corrida, distancia, valor, passageiro)
            corridas.append(corrida)
            
            continuar = input("Adicionar outra corrida? (s/n): ")
            if continuar != 's':
                break
        
        motorista = Motorista(nota_motorista, corridas)
        id = self.motorista_dao.create_motorista(motorista)
        print(f"Motorista criado com ID: {id}")

    def ler_motorista(self):
        id = input("ID do motorista: ")
        motorista = self.motorista_dao.read_motorista_by_id(id)
        return motorista

    def atualizar_motorista(self):
        id_motorista = input("ID do motorista: ")

        nova_nota = int(input("\nNova nota do motorista: "))
        result_motorista = self.motorista_dao.update_motorista(id_motorista, {"nota": nova_nota})

        atualizar_corrida = input("Deseja atualizar uma corrida? (s/n): ")

        if atualizar_corrida == 's':
            corrida_index = int(input("Indice da corrida: "))
            corrida_nota = int(input("Nova nota da corrida: "))
            corrida_distancia = float(input("Nova distancia da corrida: "))
            corrida_valor = float(input("Novo valor da corrida: "))
            nome_passageiro = input("Novo nome do passageiro: ")
            documento_passageiro = input("Novo documento do passageiro: ")

            corrida_update = {
                f"corridas.{corrida_index}.nota": corrida_nota,
                f"corridas.{corrida_index}.distancia": corrida_distancia,
                f"corridas.{corrida_index}.valor": corrida_valor,
                f"corridas.{corrida_index}.passageiro.nome": nome_passageiro,
                f"corridas.{corrida_index}.passageiro.documento": documento_passageiro
            }
            result_corrida = self.motorista_dao.update_motorista(id_motorista, corrida_update)
            if result_corrida:
                print("Corrida atualizada com sucesso!")
            else:
                print("Erro ao atualizar corrida.")    

    def remover_motorista(self):
        id = input("ID do motorista: ")
        result = self.motorista_dao.delete_motorista(id)