from entidades.filme import Filme
from entidades.membro import Membro

class FilmesCRUD:
    def __init__(self, db):
        self.db = db

    def create_filme(self, filme: Filme): #################
        query = """
        CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
        """
        self.db.query(query, parameters={"name": name, "ano_nasc": ano_nasc, "cpf": cpf})
        
    def create_membro(self, membro: Membro): #################
        query = """
        CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
        """
        self.db.query(query, parameters={"name": name, "ano_nasc": ano_nasc, "cpf": cpf})
    
    def create_relacionamento(self, filme: Filme, membro: Membro): #################
        query = """
        CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
        """
        self.db.query(query, parameters={"name": name, "ano_nasc": ano_nasc, "cpf": cpf})

    def read(self, name): #################
        query = """
        MATCH (t:Teacher {name: $name})
        RETURN t
        """
        return self.db.query(query, parameters={"name": name})

    def update_filme(self, filme: Filme): #################
        query = """
        MATCH (t:Teacher {name: $name})
        SET t.cpf = $newCpf
        """
        self.db.query(query, parameters={"name": name, "newCpf": newCpf})
        
    def update_membro(self, membro: Membro): #################
        query = """
        MATCH (t:Teacher {name: $name})
        SET t.cpf = $newCpf
        """
        self.db.query(query, parameters={"name": name, "newCpf": new})

    def delete(self, name): #################
        query = """
        MATCH (t:Teacher {name: $name})
        DELETE t
        """
        self.db.query(query, parameters={"name": name})