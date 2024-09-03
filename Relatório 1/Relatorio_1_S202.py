class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministra_aula(self, assunto):
        return f"O professor {self.nome} esta ministrando uma aula sobre {assunto}."

class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self):
        return f"O aluno {self.nome} esta presente"

class Aula:
    def __init__(self, professor, assunto):
        self.assunto = assunto
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        presencas = [aluno.presenca() for aluno in self.alunos]
        return f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n" + "\n".join(presencas)

professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())