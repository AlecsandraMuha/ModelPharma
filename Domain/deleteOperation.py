from Domain.Entitate import Entitate
from Domain.UndoRedoOperation import UndoRedoOperation
from Repository.Repo import Repository


class DeleteOperation(UndoRedoOperation):
    def __init__(self, repository: Repository,
                 obiectSters: Entitate):
        self.repository = repository
        self.obiectSters = obiectSters

    def doUndo(self):
        self.repository.add(self.obiectSters)

    def doRedo(self):
        self.repository.delete(self.obiectSters.idEntitate)
