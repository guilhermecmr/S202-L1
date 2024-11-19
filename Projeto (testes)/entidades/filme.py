# Classe da entidade Filme
class Filme:
    def __init__(self, nome: str, ano: int, genero: str, duracao: int):
        self.nome = nome # Titulo do filme (string)
        self.ano = ano # Ano de lançamento do filme (inteiro)
        self.genero = genero # Gênero do filme (string)
        self.duracao = duracao # Duração do filme em minutos (inteiro)