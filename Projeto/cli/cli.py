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

    def create_filme(self): # Perfeito
        titulo = input("\nTitulo: ")
        ano = input("Ano: ")
        genero = input("Genero: ")
        duracao = input("Duracao: ")
        filme = Filme(titulo, ano, genero, duracao)
        self.filmes_crud.create_filme(filme)
        print("Filme criado com sucesso!")
    
    def create_membro(self): # Perfeito
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
    
    def create_relacionamento(self): # Perfeito
        nome_filme = input("Nome do filme: ")
        while True:
            cargo = input("1- Ator\n2- Diretor\nOpcao: ")
            if cargo == "1":
                nome_membro = input("Nome do ator: ")
                relacionamento = "ATUOU"
                break
            elif cargo == "2":
                nome_membro = input("Nome do diretor: ")
                relacionamento = "DIRIGIU"
                break
            else:
                print("Opcao invalida!")
        
        self.filmes_crud.create_relacionamento(nome_filme, nome_membro, relacionamento)
        print("Atribuicao criada com sucesso!")
    
    def read_filme_membro(self): # Perfeito
        name = input("\nNome do filme: ")
        print(f"Retorno de {name}:")
        retorno = self.filmes_crud.read(name)
        if retorno:
            if isinstance(retorno, Filme):
                print(f"Titulo: {retorno.titulo}")
                print(f"Ano: {retorno.ano}")
                print(f"Genero: {retorno.genero}")
                print(f"Duracao: {retorno.duracao}")
                membros = self.filmes_crud.get_membros_por_filme(name)
                if membros["diretores"]:
                    print("Diretores:")
                    for diretor in membros["diretores"]:
                        print(diretor)
                else:
                    print("Diretores:")
                    print("Nenhum diretor encontrado.")
                if membros["atores"]:
                    print("Atores:")
                    for ator in membros["atores"]:
                        print(ator)
                else:
                    print("Atores:")
                    print("Nenhum ator encontrado.")
            elif isinstance(retorno, Membro):
                print(f"Nome: {retorno.nome}")
                print(f"Ano de nascimento: {retorno.ano_nasc}")
                print(f"Nacionalidade: {retorno.nacionalidade}")
                print(f"Anos de carreira: {retorno.anos_carreira}")
                print(f"Tipo: {retorno.tipo}")
                filmes = self.filmes_crud.get_filmes_por_membro(name)
                if filmes:
                    print("Filmes:")
                    for filme in filmes:
                        print(filme)
                else:
                    print("Filmes:")
                    print("Nenhum filme encontrado.")
        else:
            print(f"{name} nao foi encontrado.")


    def update_filme(self): #################
        name = input("\nNome do filme: ")
        novo_ano = input("Novo ano: ")
        novo_genero = input("Novo genero: ")    
        nova_duracao = input("Nova duracao: ")
        novo_filme = Filme(name, novo_ano, novo_genero, nova_duracao)
        self.filmes_crud.update_filme(novo_filme)
        print("Filme atualizado com sucesso!")
    
    def update_membro(self): #################
        name = input("\nNome do ator/diretor: ")
        novo_ano_nasc = input("Novo ano de nascimento: ")
        nova_nacionalidade = input("Nova nacionalidade: ")
        novos_anos_carreira = input("Novos anos de carreira: ")
        while True:
            cargo = input("1- Ator\n2- Diretor\nOpcao: ")
            if cargo == "1":
                novo_tipo = "Ator"
                break
            elif cargo == "2":
                novo_tipo = "Diretor"
                break
            else:
                print("Opcao invalida!")
        novo_membro = Membro(name, novo_ano_nasc, nova_nacionalidade, novos_anos_carreira, novo_tipo)
        self.filmes_crud.update_membro(novo_membro)
        if cargo == "1":
            print("Ator atualizado com sucesso!")
        else:
            print("Diretor atualizado com sucesso!")
    
    def delete_filme_membro(self): #################
        name = input("\nNome do filme/ator/diretor: ")
        self.filmes_crud.delete(name)
        print(f"{name} removido com sucesso!")