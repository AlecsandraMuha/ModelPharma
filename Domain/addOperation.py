from Domain.UndoRedoOperation import UndoRedoOperation
from Domain.Entitate import Entitate
from Repository.Repo import Repository


class AddOperation(UndoRedoOperation):
    def __init__(self, repository: Repository, obiectAdaugat: Entitate):
        self.repository = repository
        self.obiectAdaugat = obiectAdaugat

    def doUndo(self):
        self.repository.delete(self.obiectAdaugat.idEntitate)

    def doRedo(self):
        self.repository.add(self.obiectAdaugat)
