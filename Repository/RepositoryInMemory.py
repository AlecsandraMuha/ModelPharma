from Domain.Entitate import Entitate
from Repository.Repo import Repository


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entitati = {}

    def read(self, idEntitate=None):
        if idEntitate is None:
            return list(self.entitati.values())

        if idEntitate in self.entitati:
            return self.entitati[idEntitate]
        else:
            return None

    def add(self, entitate: Entitate):
        if self.read(entitate.idEntitate) is not None:
            raise KeyError("Exista deja o entitate cu id-ul dat!")
        self.entitati[entitate.idEntitate] = entitate

    def delete(self, idEntitate: str):
        if self.read(idEntitate) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        del self.entitati[idEntitate]

    def update(self, entitate: Entitate):
        if self.read(entitate.idEntitate) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        self.entitati[entitate.idEntitate] = entitate
