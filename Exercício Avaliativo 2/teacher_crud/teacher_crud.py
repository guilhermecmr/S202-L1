class TeacherCRUD:
    def __init__(self, db):
        self.db = db

    def create(self, name, ano_nasc, cpf):
        query = """
        CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
        """
        self.db.query(query, parameters={"name": name, "ano_nasc": ano_nasc, "cpf": cpf})

    def read(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        RETURN t
        """
        return self.db.query(query, parameters={"name": name})

    def update(self, name, newCpf):
        query = """
        MATCH (t:Teacher {name: $name})
        SET t.cpf = $newCpf
        """
        self.db.query(query, parameters={"name": name, "newCpf": newCpf})

    def delete(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        DELETE t
        """
        self.db.query(query, parameters={"name": name})