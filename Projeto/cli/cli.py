from crud.crud import FilmesCRUD
from entidades.filme import Filme
from entidades.membro import Membro

class FilmesCLI:
    def __init__(self, filmes_crud: FilmesCRUD):
        self.filmes_crud = filmes_crud
    
    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Adicionar Filme")
            print("2. Adicionar Ator/Diretor")
            print("3. Atribuir Ator/Diretor à um filme")
            print("4. Pesquisar Filme/Ator/Diretor")
            print("5. Atualizar Filme")
            print("6. Atualizar Ator/Diretor")
            print("7. Remover Filme/Ator/Diretor")
            print("8. Sair")
            
            option = input("Opcao: ")
            
            if option == "1":
                self.create_filme()
            elif option == "2":
                self.create_membro()
            elif option == "3":
                self.create_relacionamento()
            elif option == "4":
                self.read_filme_membro()
            elif option == "5":
                self.update_filme()
            elif option == "6":
                self.update_membro()
            elif option == "7":
                self.delete_filme_membro()
            elif option == "8":
                print("Saindo...")
                break
            else:
                print("Opcao invalida!")

    def create_filme(self):
        titulo = input("\nTitulo: ")
        ano = input("Ano: ")
        genero = input("Genero: ")
        duracao = input("Duracao: ")
        filme = Filme(titulo, ano, genero, duracao)
        self.filmes_crud.create_filme(filme)
        print("Filme criado com sucesso!")
    
    def create_membro(self):
        nome = input("\nNome: ")
        ano_nasc = input("Ano de nascimento: ")
        nacionalidade = input("Nacionalidade: ")
        anos_carreira = input("Anos de carreira: ")
        while True:
            cargo = input("1- Ator\n2- Diretor\nOpcao: ")
            if cargo == "1":
                tipo = "Ator"
                break
            elif cargo == "2":
                tipo = "Diretor"
                break
            else:
                print("Opcao invalida!")
        membro = Membro(nome, ano_nasc, nacionalidade, anos_carreira, tipo)
        self.filmes_crud.create_membro(membro)
        if cargo == "1":
            print("Ator criado com sucesso!")
        else:
            print("Diretor criado com sucesso!")
    
    def create_relacionamento(self):
        nome_filme = input("Nome do filme: ")
        nome_membro = input("Nome do ator/diretor: ")
        self.filmes_crud.create_relacionamento(nome_filme, nome_membro)
        print("Atribuicao criada com sucesso!")
    
    def read_filme_membro(self): #################
        name = input("\nNome do filme: ")
        print(f"Retorno de {name}:")
        filme = self.filme_crud.read(name)
        return filme
    
    def read_ator_diretor(self): #################
        name = input("\nNome do ator/diretor: ")
        print(f"Retorno de {name}:")
        ator_diretor = self.ator_diretor_crud.read(name)
        return ator_diretor
    
    def update_filme(self): #################
        name = input("\nNome do filme: ")
        newAno = input("Ano: ")
        filme = self.filme_crud.update(name, newAno)
        print("Filme atualizado com sucesso!")
        return filme
    
    def update_membro(self): #################
        name = input("\nNome do ator/diretor: ")
        newCpf = input("CPF: ")
        ator_diretor = self.ator_diretor_crud.update(name, newCpf)
        print("Ator/Diretor atualizado com sucesso!")
        return ator_diretor
    
    def delete_filme_membro(self): #################
        name = input("\nNome do filme/ator/diretor: ")
        filme_ator_diretor = self.filme_ator_diretor_crud.delete(name)
        print("Filme/Ator/Diretor removido com sucesso!")
        return filme_ator_diretor