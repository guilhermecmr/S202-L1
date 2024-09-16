from .Corrida import Corrida

class Motorista:
    def __init__(self, nota: int, corridas: list[Corrida]):
        self.nota = nota
        self.corridas = corridas