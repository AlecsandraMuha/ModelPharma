from Domain.Entitate import Entitate
from Repository.Repo import Repository
from Domain.UndoRedoOperation import UndoRedoOperation


class ModifyOperation(UndoRedoOperation):
    def __init__(self, repository: Repository,
                 obiectModificat: Entitate,
                 obiectInitial: Entitate):
        self.repository = repository
        self.obiectModificat = obiectModificat
        self.obiectInitial = obiectInitial

    def doUndo(self):
        self.repository.update(self.obiectInitial)

    def doRedo(self):
        self.repository.update(self.obiectModificat)
