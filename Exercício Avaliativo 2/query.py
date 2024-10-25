from database.database import Database

db = Database("bolt://98.80.167.84", "neo4j", "occurrences-incentive-kites")

# Questão 1
# a)
def get_renzo():
    query = """
    MATCH (t:Teacher {name: 'Renzo'})
    RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf
    """
    return db.query(query)

# b)
def get_professores_m():
    query = """
    MATCH (t:Teacher)
    WHERE t.name STARTS WITH 'M'
    RETURN t.name AS name, t.cpf AS cpf
    """
    return db.query(query)

# c)
def get_cidades():
    query = """
    MATCH (c:City)
    RETURN c.name AS name
    """
    return db.query(query)

# d)
def get_escolas():
    query = """
    MATCH (s:School)
    WHERE s.number >= 150 AND s.number <= 550
    RETURN s.name AS name, s.address AS address, s.number AS number
    """
    return db.query(query)

# Questão 2
# a)
def get_velho_novo():
    query = """
    MATCH (t:Teacher)
    RETURN MAX(t.ano_nasc) AS mais_jovem, MIN(t.ano_nasc) AS mais_velho
    """
    return db.query(query)

# b)
def get_media_populacao():
    query = """
    MATCH (c:City)
    RETURN AVG(c.population) AS media
    """
    return db.query(query)

# c) 
def get_cidade_cep():
    query = """
    MATCH (c:City {cep: '37540-000'})
    RETURN REPLACE(c.name, 'a', 'A') AS name
    """
    return db.query(query)

# d)
def get_professor_char():
    query = """
    MATCH (t:Teacher)
    RETURN SUBSTRING(t.name, 2, 1) AS char
    """
    return db.query(query)

print(f"Questao 1:")
print(f"a)\n{get_renzo()}")
print(f"b)\n{get_professores_m()}")
print(f"c)\n{get_cidades()}")
print(f"d)\n{get_escolas()}")
print(f"\nQuestao 2:")
print(f"a)\n{get_velho_novo()}")
print(f"b)\n{get_media_populacao()}")
print(f"c)\n{get_cidade_cep()}")
print(f"d)\n{get_professor_char()}")