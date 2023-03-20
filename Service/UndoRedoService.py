from Domain.UndoRedoOperation import UndoRedoOperation


class UndoRedoService:
    def __init__(self):
        self.undoOperation = []
        self.redoOperation = []

    def addUndoRedoOperation(self, undoRedoOperation: UndoRedoOperation):
        self.undoOperation.append(undoRedoOperation)
        self.redoOperation.clear()

    def undo(self):
        if self.undoOperation:
            operation = self.undoOperation.pop()
            operation.doUndo()
            self.redoOperation.append(operation)

    def redo(self):
        if self.redoOperation:
            operation = self.redoOperation.pop()
            operation.doRedo()
            self.undoOperation.append(operation)
