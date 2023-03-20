from typing import List

from Domain.UndoRedoOperation import UndoRedoOperation
from Repository.Repo import Repository


class CascadeDeleteOperation(UndoRedoOperation):
    def __init__(self,
                 repository: Repository,
                 tranzactieRepository: Repository,
                 cascadeList: List):
        self.__repository = repository
        self.__tranzactieRepository = tranzactieRepository
        self.__cascadeList = cascadeList

    def doUndo(self):
        for i in range(len(self.__cascadeList) - 1):
            self.__tranzactieRepository.add(self.__cascadeList[i])
        self.__repository.add(
            self.__cascadeList[len(self.__cascadeList)-1])

    def doRedo(self):
        for i in range(len(self.__cascadeList) - 1):
            self.__tranzactieRepository.delete(
                self.__cascadeList[0].idEntitate)
        self.__repository.delete(
            self.__cascadeList[len(self.__cascadeList) - 1].idEntitate)
