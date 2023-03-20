from Domain.UndoRedoOperation import UndoRedoOperation
from Repository.Repo import Repository


class MultiUpdateOperation(UndoRedoOperation):
    def __init__(self, repository: Repository, obiecte_noi_modificate,
                 obiecte_vechi_modificate):
        self.repository = repository
        self.obiecte_noi_modificate = obiecte_noi_modificate
        self.obiecte_vechi_modificate = obiecte_vechi_modificate

    def doUndo(self):
        for entitate in self.obiecte_vechi_modificate:
            self.repository.update(entitate)

    def doRedo(self):
        for entitate in self.obiecte_noi_modificate:
            self.repository.update(entitate)
