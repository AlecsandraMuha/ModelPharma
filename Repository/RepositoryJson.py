import jsonpickle

from Domain.Entitate import Entitate
from Repository.RepositoryInMemory import RepositoryInMemory


class RepositoryJson(RepositoryInMemory):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __readFile(self):
        try:
            with open(self.filename, "r") as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __writeFile(self):
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.entitati, indent=2))

    def read(self, idEntitate=None):
        self.entitati = self.__readFile()
        return super().read(idEntitate)

    def add(self, entitate: Entitate):
        self.entitati = self.__readFile()
        super().add(entitate)
        self.__writeFile()

    def delete(self, idEntitate):
        self.entitati = self.__readFile()
        super().delete(idEntitate)
        self.__writeFile()

    def update(self, entitate: Entitate):
        self.entitati = self.__readFile()
        super().update(entitate)
        self.__writeFile()
