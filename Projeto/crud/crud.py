from entidades.filme import Filme
from entidades.membro import Membro

class FilmesCRUD:
    def __init__(self, db):
        self.db = db

    def create_filme(self, filme: Filme): # Perfeito
        query = """
        CREATE (f:Filme {titulo: $titulo, ano: $ano, genero: $genero, duracao: $duracao})
        """
        parameters = {"titulo": filme.titulo, "ano": filme.ano, "genero": filme.genero, "duracao": filme.duracao}
        self.db.query(query, parameters)

    def create_membro(self, membro: Membro): # Perfeito
        query = """
        CREATE (m:Membro {nome: $nome, ano_nasc: $ano_nasc, nacionalidade: $nacionalidade, 
                          anos_carreira: $anos_carreira, tipo: $tipo})
        """
        parameters = {"nome": membro.nome, "ano_nasc": membro.ano_nasc, "nacionalidade": membro.nacionalidade, 
                      "anos_carreira": membro.anos_carreira, "tipo": membro.tipo}
        self.db.query(query, parameters)

    def create_relacionamento(self, nome_filme: str, nome_membro: str, relacao: str): # Perfeito
        query = f"""
        MATCH (f:Filme {{nome: $titulo}})
        MATCH (m:Membro {{nome: $nome}})
        CREATE (m)-[:{relacao}]->(f)
        """
        parameters = {"titulo": nome_filme, "nome": nome_membro}
        self.db.query(query, parameters)

    def read(self, name: str): # Perfeito
        query = """
        MATCH (n {nome: $name}) 
        RETURN n, labels(n) AS labels
        """
        parameters = {"name": name}
        result = self.db.query(query, parameters)
        records = list(result)
        labels = records[0]["labels"]
        if not records:
            return None
        node = records[0]["n"]
        if "Filme" in labels:
            return Filme(
                nome=node["titulo"],
                ano=node["ano"],
                genero=node["genero"],
                duracao=node["duracao"]
            )
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

    def get_filmes_por_membro(self, nome: str): # Perfeito
            query = """
            MATCH (m:Membro {nome: $nome})
            OPTIONAL MATCH (m)-[r]->(f:Filme)
            RETURN type(r) AS relacao, f.nome AS titulo, m.tipo AS tipo
            """
            parameters = {"nome": nome}
            result = self.db.query(query, parameters)

            filmes = []
            for record in result:
                tipo_membro = record["tipo"]
                relacao = record["relacao"]
                titulo = record["titulo"]

                if tipo_membro == "Ator" and relacao == "ATUOU":
                    filmes.append(titulo)
                elif tipo_membro == "Diretor" and relacao == "DIRIGIU":
                    filmes.append(titulo)

            return filmes

    def get_membros_por_filme(self, titulo: str): # Perfeito
        query = """
        MATCH (m:Membro)-[r]->(f:Filme {titulo: $titulo})
        RETURN m.nome AS nome, m.tipo AS tipo, type(r) AS relacao
        """
        parameters = {"titulo": titulo}
        result = self.db.query(query, parameters)

        diretores = []
        atores = []

        for record in result:
            nome = record["nome"]
            tipo = record["tipo"]
            relacao = record["relacao"]

            if relacao == "DIRIGIU" and tipo == "Diretor":
                diretores.append(nome)
            elif relacao == "ATUOU" and tipo == "Ator":
                atores.append(nome)

        return {"diretores": diretores, "atores": atores}

    def update_filme(self, filme: Filme):
        query = """
        MATCH (f:Filme {titulo: $titulo})
        SET f.ano = $ano, f.genero = $genero, f.duracao = $duracao
        """
        parameters = {"titulo": filme.titulo, "ano": filme.ano, "genero": filme.genero, "duracao": filme.duracao}
        self.db.query(query, parameters)

    def update_membro(self, membro: Membro):
        query = """
        MATCH (m:Membro {nome: $nome})
        SET m.ano_nasc = $ano_nasc, m.nacionalidade = $nacionalidade, 
            m.anos_carreira = $anos_carreira, m.tipo = $tipo
        """
        parameters = {"nome": membro.nome, "ano_nasc": membro.ano_nasc, "nacionalidade": membro.nacionalidade, 
                      "anos_carreira": membro.anos_carreira, "tipo": membro.tipo}
        self.db.query(query, parameters)

    def delete(self, name: str):
        query = """
        MATCH (n {nome: $name}) DETACH DELETE n
        """
        parameters = {"name": name}
        self.db.query(query, parameters)
