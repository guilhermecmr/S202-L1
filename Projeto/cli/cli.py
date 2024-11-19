from crud.crud import FilmesCRUD
from entidades.filme import Filme
from entidades.membro import Membro

# Classe que implementa a interface de linha de comando
class FilmesCLI:
    def __init__(self, filmes_crud: FilmesCRUD):
        self.filmes_crud = filmes_crud
    
    # Funcao que exibe o menu principal
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

    # Funcao que cria um filme
    def create_filme(self):
        titulo = input("\nTitulo: ")
        existe = self.filmes_crud.filme_existe(titulo) # Verifica se o filme ja existe
        if existe: # Se o filme ja existe, exibe uma mensagem de erro e retorna
            print("Filme ja cadastrado!")
            return
        ano = input("Ano: ")
        if ano.isnumeric() == False: # Verifica se o ano e um numero, caso contrario exibe uma mensagem de erro e retorna
            print("Ano invalido!")
            return
        genero = input("Genero: ")
        if genero.isnumeric() == True: # Verifica se o genero e uma string, caso contrario exibe uma mensagem de erro e retorna
            print("Genero invalido!")
            return
        duracao = input("Duracao: ")
        if duracao.isnumeric() == False: # Verifica se a duracao e um numero, caso contrario exibe uma mensagem de erro e retorna
            print("Duracao invalida!")
            return
        filme = Filme(titulo, int(ano), genero, int(duracao)) # Cria um objeto do tipo Filme
        self.filmes_crud.create_filme(filme) # Cria o filme no banco de dados
        print("Filme criado com sucesso!")
    
    # Funcao que cria um membro
    def create_membro(self):
        nome = input("\nNome: ")
        if nome.isnumeric() == True: # Verifica se o nome e uma string, caso contrario exibe uma mensagem de erro e retorna
            print("Nome invalido!")
            return
        existe = self.filmes_crud.membro_existe(nome) # Verifica se o ator/diretor ja existe
        if existe: # Se o ator/diretor ja existe, exibe uma mensagem de erro e retorna
            print("Ator/diretor ja cadastrado!")
            return
        ano_nasc = input("Ano de nascimento: ")
        if ano_nasc.isnumeric() == False: # Verifica se o ano de nascimento e um numero, caso contrario exibe uma mensagem de erro e retorna
            print("Ano de nascimento invalido!")
            return
        nacionalidade = input("Nacionalidade: ")
        if nacionalidade.isnumeric() == True: # Verifica se a nacionalidade e uma string, caso contrario exibe uma mensagem de erro e retorna
            print("Nacionalidade invalida!")
            return
        anos_carreira = input("Anos de carreira: ")
        if anos_carreira.isnumeric() == False: # Verifica se os anos de carreira e um numero, caso contrario exibe uma mensagem de erro e retorna
            print("Anos de carreira invalidos!")
            return
        # Define o cargo do membro como ator ou diretor
        while True:
            cargo = input(" 1- Ator\n 2- Diretor\n Opcao: ")
            if cargo == "1":
                tipo = "Ator"
                break
            elif cargo == "2":
                tipo = "Diretor"
                break
            else:
                print(" Opcao invalida!")
        membro = Membro(nome, int(ano_nasc), nacionalidade, int(anos_carreira), tipo) # Cria um objeto do tipo Membro
        self.filmes_crud.create_membro(membro) # Cria o ator/diretor no banco de dados
        if cargo == "1":
            print("Ator criado com sucesso!")
        else:
            print("Diretor criado com sucesso!")
    
    # Funcao que cria um relacionamento entre um filme e um ator/diretor
    def create_relacionamento(self): 
        nome_filme = input("\nNome do filme: ")
        existe = self.filmes_crud.filme_existe(nome_filme) # Verifica se o filme existe
        if not existe: # Se o filme nao existe, exibe uma mensagem de erro e retorna    
            print("Filme nao encontrado!")
            return
        while True:
            cargo = input(" 1- Atribuir ator\n 2- Atribuir diretor\n Opcao: ")
            if cargo == "1":
                nome_membro = input("Nome do ator: ")
                existe = self.filmes_crud.membro_existe(nome_membro) # Verifica se o ator existe
                if not existe: # Se o ator nao existe, exibe uma mensagem de erro e retorna
                    print("Ator nao encontrado!") 
                    return
                relacionamento = "ATUOU" # Define o tipo de relacionamento como "ATUOU"
                break
            elif cargo == "2":
                nome_membro = input("Nome do diretor: ")
                existe = self.filmes_crud.membro_existe(nome_membro) # Verifica se o diretor existe
                if not existe: # Se o diretor nao existe, exibe uma mensagem de erro e retorna
                    print("Diretor nao encontrado!")
                    return
                relacionamento = "DIRIGIU" # Define o tipo de relacionamento como "DIRIGIU"
                break
            else:
                print("Opcao invalida!")
        
        self.filmes_crud.create_relacionamento(nome_filme, nome_membro, relacionamento) # Cria o relacionamento no banco de dados
        print("Atribuicao criada com sucesso!")
    
    # Funcao que le um filme ou um ator/diretor
    def read_filme_membro(self):
        name = input("\nFilme, ator ou diretor: ")
        existe_filme = self.filmes_crud.filme_existe(name) # Verifica se o filme existe
        existe_membro = self.filmes_crud.membro_existe(name) # Verifica se o ator/diretor existe
        if not existe_filme and not existe_membro: # Se o filme/ator/diretor nao existe, exibe uma mensagem de erro e retorna
            print(f"{name} nao foi encontrado.")
            return
        print(f"Retorno de {name}:")
        retorno = self.filmes_crud.read(name) 
        if isinstance(retorno, Filme): # Se o retorno for um objeto do tipo Filme, exibe as informacoes do filme
                print(f" Titulo: {retorno.nome}")
                print(f" Ano: {retorno.ano}")
                print(f" Genero: {retorno.genero}")
                print(f" Duracao: {retorno.duracao}")
                membros = self.filmes_crud.get_membros_do_filme(name) # Obtem os atores/diretores que atuaram/dirigiram o filme
                print(" Diretores:")
                if membros["diretores"]:
                    for diretor in membros["diretores"]:
                        print(f"  -{diretor}")
                else:
                    print(f"  {retorno.nome} nao possui diretores cadastrados.")
                print(" Atores:")
                if membros["atores"]:
                    for ator in membros["atores"]:
                        print(f"  -{ator}")
                else:
                    print(f"  {retorno.nome} nao possui atores cadastrados.")
        elif isinstance(retorno, Membro): # Se o retorno for um objeto do tipo Membro, exibe as informacoes do ator/diretor
                print(f" Nome: {retorno.nome}")
                print(f" Ano de nascimento: {retorno.ano_nasc}")
                print(f" Nacionalidade: {retorno.nacionalidade}")
                print(f" Anos de carreira: {retorno.anos_carreira}")
                print(f" Cargo: {retorno.tipo}")
                filmes = self.filmes_crud.get_filmes_por_membro(name) # Obtem os filmes em que o membro atuou/dirigiu
                print(" Filmes:")
                if filmes:
                    for filme in filmes:
                        print(f"  -{filme}")
                else:
                    print(f"  {retorno.nome} nao possui filmes cadastrados.")
            
    # Funcao que exibe as estatisticas
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

    # Funcao que atualiza um filme
    def update_filme(self): 
        name = input("\nNome do filme: ")
        existe = self.filmes_crud.filme_existe(name) # Verifica se o filme existe
        if not existe: # Se o filme nao existe, exibe uma mensagem de erro e retorna
            print("Filme nao encontrado!")
            return
        novo_ano = input("Novo ano: ")
        if novo_ano.isnumeric() == False: # Verifica se o ano e um numero, caso contrario exibe uma mensagem de erro e retorna
            print("Ano invalido!")
            return
        novo_genero = input("Novo genero: ")    
        if novo_genero.isnumeric() == True: # Verifica se o genero e uma string, caso contrario exibe uma mensagem de erro e retorna
            print("Genero invalido!")
            return
        nova_duracao = input("Nova duracao: ")
        if nova_duracao.isnumeric() == False: # Verifica se a duracao e um numero, caso contrario exibe uma mensagem de erro e retorna
            print("Duracao invalida!")
            return
        novo_filme = Filme(name, int(novo_ano), novo_genero, int(nova_duracao)) # Cria um objeto do tipo Filme
        self.filmes_crud.update_filme(novo_filme) # Atualiza o filme no banco de dados
        print("Filme atualizado com sucesso!")
    
    # Funcao que atualiza um ator/diretor
    def update_membro(self):
        name = input("\nNome do ator/diretor: ")
        existe = self.filmes_crud.membro_existe(name) # Verifica se o ator/diretor existe
        if not existe: # Se o ator/diretor nao existe, exibe uma mensagem de erro e retorna
            print("Ator/diretor nao encontrado!")
            return
        novo_ano_nasc = input("Novo ano de nascimento: ")
        if novo_ano_nasc.isnumeric() == False: # Verifica se o ano de nascimento e um numero, caso contrario exibe uma mensagem de erro e retorna
            print("Ano de nascimento invalido!")
            return
        nova_nacionalidade = input("Nova nacionalidade: ")
        if nova_nacionalidade.isnumeric() == True: # Verifica se a nacionalidade e uma string, caso contrario exibe uma mensagem de erro e retorna
            print("Nacionalidade invalida!")
            return
        novos_anos_carreira = input("Novos anos de carreira: ")
        if novos_anos_carreira.isnumeric() == False: # Verifica se os anos de carreira e um numero, caso contrario exibe uma mensagem de erro e retorna
            print("Anos de carreira invalidos!")
            return
        while True:
            cargo = input(" 1- Ator\n 2- Diretor\n Opcao: ")
            if cargo == "1":
                novo_tipo = "Ator"
                break
            elif cargo == "2":
                novo_tipo = "Diretor"
                break
            else:
                print("Opcao invalida!")
        novo_membro = Membro(name, int(novo_ano_nasc), nova_nacionalidade, int(novos_anos_carreira), novo_tipo) # Cria um objeto do tipo Membro
        self.filmes_crud.update_membro(novo_membro) # Atualiza o ator/diretor no banco de dados
        if cargo == "1":
            print("Ator atualizado com sucesso!")
        else:
            print("Diretor atualizado com sucesso!")
    
    def delete_filme_membro(self):
        name = input("\nNome do filme/ator/diretor: ")
        existe_filme = self.filmes_crud.filme_existe(name) # Verifica se o filme existe
        existe_membro = self.filmes_crud.membro_existe(name) # Verifica se o ator/diretor existe
        if not existe_filme and not existe_membro: # Se o filme/ator/diretor nao existe, exibe uma mensagem de erro e retorna
            print(f"{name} nao foi encontrado.")
            return
        self.filmes_crud.delete(name) # Deleta o filme/ator/diretor do banco de dados
        print(f"{name} removido com sucesso!")