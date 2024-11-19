from entidades.filme import Filme
from entidades.membro import Membro

class FilmesCRUD:
    def __init__(self, db):
        self.db = db

    # Funcao que verifica se um filme já existe no banco de dados
    def filme_existe(self, nome: str) -> bool:
        query = """
        MATCH (f:Filme {nome: $nome})
        RETURN COUNT(f) > 0 AS existe
        """
        parameters = {"nome": nome}
        result = self.db.query(query, parameters)
        if result:
            return result[0]["existe"]
        return False

    # Funcao que cria um filme no banco de dados
    def create_filme(self, filme: Filme): 
        query = """
        CREATE (f:Filme {nome: $nome, ano: $ano, genero: $genero, duracao: $duracao})
        """
        parameters = {"nome": filme.nome, "ano": filme.ano, "genero": filme.genero, "duracao": filme.duracao}
        self.db.query(query, parameters)

    # Funcao que cria um relacionamento entre um membro e um filme
    def membro_existe(self, nome: str) -> bool:
        query = """
        MATCH (m:Membro {nome: $nome})
        RETURN COUNT(m) > 0 AS existe
        """
        parameters = {"nome": nome}
        result = self.db.query(query, parameters)
        if result:
            return result[0]["existe"]
        return False

    # Funcao que cria um membro no banco de dados
    def create_membro(self, membro: Membro):
        query = """
        CREATE (m:Membro {nome: $nome, ano_nasc: $ano_nasc, nacionalidade: $nacionalidade, 
                          anos_carreira: $anos_carreira, tipo: $tipo})
        """
        parameters = {"nome": membro.nome, "ano_nasc": membro.ano_nasc, "nacionalidade": membro.nacionalidade, 
                      "anos_carreira": membro.anos_carreira, "tipo": membro.tipo}
        self.db.query(query, parameters)

    # Funcao que cria um relacionamento entre um membro e um filme
    def create_relacionamento(self, nome_filme: str, nome_membro: str, relacao: str): 
        query = f"""
        MATCH (f:Filme {{nome: $nome_filme}})
        MATCH (m:Membro {{nome: $nome_membro}})
        CREATE (m)-[:{relacao}]->(f)
        """
        parameters = {"nome_filme": nome_filme, "nome_membro": nome_membro}
        self.db.query(query, parameters)

    # Funcao que le um filme ou membro do banco de dados
    def read(self, name: str):
        query = """
        MATCH (n {nome: $name}) 
        RETURN n, labels(n) AS labels
        """
        parameters = {"name": name}
        result = list(self.db.query(query, parameters)) # Converte o resultado para uma lista
        labels = result[0]["labels"] # Pega as labels do nó
        node = result[0]["n"] # Pega o nó
        # Verifica se o nó é um filme ou membro e retorna o objeto correspondente
        if "Filme" in labels:
            return Filme(
                nome=node["nome"],
                ano=node["ano"],
                genero=node["genero"],
                duracao=node["duracao"]
            )
        # Verifica se o nó é um membro e retorna o objeto correspondente
        if "Membro" in labels:
            return Membro(
                nome=node["nome"],
                ano_nasc=node["ano_nasc"],
                nacionalidade=node["nacionalidade"],
                anos_carreira=node["anos_carreira"],
                tipo=node["tipo"]
            )
        else:
            return None
        
    # Funcao que pesquisa todos os atores/diretores de um filme
    def get_membros_do_filme(self, nome: str): 
        query = """
        MATCH (m:Membro)-[r]->(f:Filme {nome: $nome})
        RETURN m.nome AS nome, type(r) AS relacao
        """
        parameters = {"nome": nome}
        result = self.db.query(query, parameters)
        diretores = [] # Lista de diretores
        atores = [] # Lista de atores
        for record in result:
            nome = record["nome"]
            relacao = record["relacao"]
            if relacao == "DIRIGIU": # Se a relacao for "DIRIGIU" adiciona o nome na lista de diretores
                diretores.append(nome)
            elif relacao == "ATUOU": # Se a relacao for "ATUOU" adiciona o nome na lista de atores
                atores.append(nome)
        return {"diretores": diretores, "atores": atores}    
    
    # Funcao que pesquisa todos os filmes de um membro
    def get_filmes_por_membro(self, nome: str): 
            query = """
            MATCH (m:Membro {nome: $nome})
            OPTIONAL MATCH (m)-[r]->(f:Filme)
            RETURN type(r) AS relacao, f.nome AS nome
            """
            parameters = {"nome": nome}
            result = self.db.query(query, parameters)
            filmes = [] # Lista de filmes
            for record in result:
                relacao = record["relacao"]
                nome = record["nome"]
                # Se a relacao for "ATUOU" ou "DIRIGIU" adiciona o nome na lista de filmes
                if relacao == "ATUOU": 
                    filmes.append(nome)
                elif relacao == "DIRIGIU": 
                    filmes.append(nome)
            return filmes

    # Funcao que retorna o numero de filmes no banco de dados
    def numero_filmes(self):
        query = """
        MATCH (f:Filme)
        RETURN COUNT(f) AS numero
        """
        result = self.db.query(query)
        return result[0]["numero"]

    # Funcao que retorna o numero de atores no banco de dados
    def numero_atores(self):
        query = """
        MATCH (m:Membro {tipo: "Ator"})
        RETURN COUNT(m) AS numero
        """
        result = self.db.query(query)
        return result[0]["numero"]

    # Funcao que retorna o numero de diretores no banco de dados
    def numero_diretores(self):
        query = """
        MATCH (m:Membro {tipo: "Diretor"})
        RETURN COUNT(m) AS numero
        """
        result = self.db.query(query)
        return result[0]["numero"]

    # Funcao que retorna a media de anos de carreira dos membros
    def media_anos_carreira(self):
            query = """
            MATCH (m:Membro)
            RETURN CEIL(AVG(m.anos_carreira)) AS media
            """
            result = self.db.query(query)
            return result[0]["media"]
    
    # Funcao que retorna a duracao do filme mais curto
    def menor_duracao(self):
        query = """
        MATCH (f:Filme)
        RETURN MIN(f.duracao) AS menor
        """
        result = self.db.query(query)
        return result[0]["menor"]
    
    # Funcao que retorna a duracao do filme mais longo
    def maior_duracao(self):
        query = """
        MATCH (f:Filme)
        RETURN MAX(f.duracao) AS maior
        """
        result = self.db.query(query)
        return result[0]["maior"]
    
    # Funcao que retorna a media de duracao dos filmes
    def media_duracao(self):
        query = """
        MATCH (f:Filme)
        RETURN AVG(f.duracao) AS media
        """
        result = self.db.query(query)
        return result[0]["media"]
    
    # Funcao que retorna o numero de filmes por genero
    def filmes_por_genero(self):
        query = """
        MATCH (f:Filme)
        RETURN f.genero AS genero, COUNT(f) AS numero
        """
        result = self.db.query(query)
        return [record for record in result]  

    # Funcao que atualiza um filme no banco de dados
    def update_filme(self, filme: Filme):
        query = """
        MATCH (f:Filme {nome: $nome})
        SET f.ano = $ano, f.genero = $genero, f.duracao = $duracao
        """
        parameters = {"nome": filme.nome, "ano": filme.ano, "genero": filme.genero, "duracao": filme.duracao}
        self.db.query(query, parameters)

    # Funcao que atualiza um membro no banco de dados
    def update_membro(self, membro: Membro):
        query = """
        MATCH (m:Membro {nome: $nome})
        SET m.ano_nasc = $ano_nasc, m.nacionalidade = $nacionalidade, 
            m.anos_carreira = $anos_carreira, m.tipo = $tipo
        """
        parameters = {"nome": membro.nome, "ano_nasc": membro.ano_nasc, "nacionalidade": membro.nacionalidade, 
                      "anos_carreira": membro.anos_carreira, "tipo": membro.tipo}
        self.db.query(query, parameters)

    # Funcao que deleta um filme ou membro do banco de dados
    def delete(self, name: str):
        query = """
        MATCH (n {nome: $name}) DETACH DELETE n
        """
        parameters = {"name": name}
        self.db.query(query, parameters)