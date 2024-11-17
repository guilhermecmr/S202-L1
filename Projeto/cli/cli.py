from crud.crud import FilmesCRUD
from entidades.filme import Filme
from entidades.membro import Membro

class FilmesCLI:
    def __init__(self, filmes_crud: FilmesCRUD):
        self.filmes_crud = filmes_crud
    
    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Adicionar filme")
            print("2. Adicionar ator/diretor")
            print("3. Atribuir filme a ator/diretor")
            print("4. Pesquisar")
            print("5. Estatisticas")
            print("6. Atualizar filme")
            print("7. Atualizar ator/diretor")
            print("8. Deletar")
            print("9. Sair")
            
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
                self.estatisticas()
            elif option == "6":
                self.update_filme()
            elif option == "7":
                self.update_membro()
            elif option == "8":
                self.delete_filme_membro()
            elif option == "9":
                print(f"\nSaindo...")
                break
            else:
                print(f"\nOpcao invalida!")

    def create_filme(self):
        titulo = input("\nTitulo: ")
        existe = self.filmes_crud.filme_existe(titulo)
        if existe:
            print("Filme ja cadastrado!")
            return
        ano = input("Ano: ")
        genero = input("Genero: ")
        duracao = input("Duracao: ")
        filme = Filme(titulo, ano, genero, duracao)
        self.filmes_crud.create_filme(filme)
        print("Filme criado com sucesso!")
    
    def create_membro(self):
        nome = input("\nNome: ")
        existe = self.filmes_crud.membro_existe(nome)
        if existe:
            print("Ator/diretor ja cadastrado!")
            return
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
        existe = self.filmes_crud.filme_existe(nome_filme)
        if not existe:
            print("Filme nao encontrado!")
            return
        while True:
            cargo = input("1- Ator\n2- Diretor\nOpcao: ")
            if cargo == "1":
                nome_membro = input("Nome do ator: ")
                existe = self.filmes_crud.membro_existe(nome_membro)
                if not existe:
                    print("Ator nao encontrado!")
                    return
                relacionamento = "ATUOU"
                break
            elif cargo == "2":
                nome_membro = input("Nome do diretor: ")
                existe = self.filmes_crud.membro_existe(nome_membro)
                if not existe:
                    print("Diretor nao encontrado!")
                    return
                relacionamento = "DIRIGIU"
                break
            else:
                print("Opcao invalida!")
        
        self.filmes_crud.create_relacionamento(nome_filme, nome_membro, relacionamento)
        print("Atribuicao criada com sucesso!")
    
    def read_filme_membro(self):
        name = input("\nFilme, ator ou diretor: ")
        existe_filme = self.filmes_crud.filme_existe(name)
        existe_membro = self.filmes_crud.membro_existe(name)
        if not existe_filme and not existe_membro:
            print(f"{name} nao foi encontrado.")
            return
        print(f"Retorno de {name}:")
        retorno = self.filmes_crud.read(name)
        if isinstance(retorno, Filme):
                print(f"Titulo: {retorno.nome}")
                print(f"Ano: {retorno.ano}")
                print(f"Genero: {retorno.genero}")
                print(f"Duracao: {retorno.duracao}")
                membros = self.filmes_crud.get_membros_por_filme(name)
                if membros["diretores"]:
                    print("Diretores:")
                    for diretor in membros["diretores"]:
                        print(f" -{diretor}")
                else:
                    print(f"{retorno.nome} nao possui diretores cadastrados.")
                if membros["atores"]:
                    print("Atores:")
                    for ator in membros["atores"]:
                        print(f" -{ator}")
                else:
                    print(f"{retorno.nome} nao possui atores cadastrados.")
        elif isinstance(retorno, Membro):
                print(f"Nome: {retorno.nome}")
                print(f"Ano de nascimento: {retorno.ano_nasc}")
                print(f"Nacionalidade: {retorno.nacionalidade}")
                print(f"Anos de carreira: {retorno.anos_carreira}")
                print(f"Cargo: {retorno.tipo}")
                filmes = self.filmes_crud.get_filmes_por_membro(name)
                if filmes:
                    print("Filmes:")
                    for filme in filmes:
                        print(f" -{filme}")
                else:
                    print(f"{retorno.nome} nao possui filmes cadastrados.")
            
    def update_filme(self): 
        name = input("\nNome do filme: ")
        existe = self.filmes_crud.filme_existe(name)
        if not existe:
            print("Filme nao encontrado!")
            return
        novo_ano = input("Novo ano: ")
        novo_genero = input("Novo genero: ")    
        nova_duracao = input("Nova duracao: ")
        novo_filme = Filme(name, novo_ano, novo_genero, nova_duracao)
        self.filmes_crud.update_filme(novo_filme)
        print("Filme atualizado com sucesso!")
    
    def update_membro(self):
        name = input("\nNome do ator/diretor: ")
        existe = self.filmes_crud.membro_existe(name)
        if not existe:
            print("Ator/diretor nao encontrado!")
            return
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
    
    def delete_filme_membro(self):
        name = input("\nNome do filme/ator/diretor: ")
        existe_filme = self.filmes_crud.filme_existe(name)
        existe_membro = self.filmes_crud.membro_existe(name)
        if not existe_filme and not existe_membro:
            print(f"{name} nao foi encontrado.")
            return
        self.filmes_crud.delete(name)
        print(f"{name} removido com sucesso!")
        
    def estatisticas(self):
        print("\nEstatisticas:")
        print(" Numero de filmes: ", self.filmes_crud.numero_filmes())
        print(" Numero de atores: ", self.filmes_crud.numero_atores())
        print(" Numero de diretores: ", self.filmes_crud.numero_diretores())
        print(" Media de anos de carreira: ", int(self.filmes_crud.media_anos_carreira()))
        print(" Menor duracao: ", self.filmes_crud.menor_duracao())        
        print(" Maior duracao: ", self.filmes_crud.maior_duracao())  
        print(" Duracao media: ", int(self.filmes_crud.media_duracao()))
        print(" Filmes por genero:")
        generos = self.filmes_crud.filmes_por_genero()
        for record in generos:  
            print(f"  -{record['genero']}: {record['numero']}")
