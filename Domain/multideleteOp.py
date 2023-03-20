from Domain.Entitate import Entitate
from Domain.UndoRedoOperation import UndoRedoOperation
from Repository.Repo import Repository


class MultiDeleteOperation(UndoRedoOperation):
    def __init__(self, repository: Repository, obiecte_sterse):
        self.repository = repository
        self.obiecte_sterse = obiecte_sterse

    def doUndo(self):
        for entitate in self.obiecte_sterse:
            self.repository.add(entitate)

    def doRedo(self):
        for entitate in self.obiecte_sterse:
            self.repository.delete(entitate.idEntitate)
