from Domain.ModyObject import ModifyOperation
from Domain.addOperation import AddOperation
from Domain.cardClient import CardClient
from Domain.deleteOperation import DeleteOperation
from Repository.Exceptii import CNPRepetatError
from Repository.Repo import Repository
from Service import UndoRedoService


class CardClientService:
    def __init__(self, cardClientRepository: Repository,
                 undoRedoService: UndoRedoService):
        self.__cardClientRepository = cardClientRepository
        self.__undoRedoService = undoRedoService

    def getAll(self):
        return self.__cardClientRepository.read()

    def add(self, idCard, nume, prenume, datanasterii, CNP, datainreg):
        list = []
        for i in self.__cardClientRepository.read():
            list.append(getattr(i, 'CNP'))
        if CNP in list:
            raise CNPRepetatError("CNP-ul trebuie sa fie unic!")
        card = CardClient(
            idCard,
            nume,
            prenume,
            datanasterii,
            CNP,
            datainreg)
        self.__cardClientRepository.add(card)
        self.__undoRedoService.addUndoRedoOperation(
          AddOperation(self.__cardClientRepository, card))

    def delete(self, idCard):
        card_sters = self.__cardClientRepository.read(idCard)
        self.__cardClientRepository.delete(idCard)
        self.__undoRedoService.addUndoRedoOperation(DeleteOperation
                                                    (self.
                                                     __cardClientRepository,
                                                     card_sters))

    def update(self, idCard, nume, prenume, datanasterii, CNP, datainreg):
        card = CardClient(
            idCard,
            nume,
            prenume,
            datanasterii,
            CNP,
            datainreg)
        card_vechi = self.__cardClientRepository.read(id)
        self.__cardClientRepository.update(card)
        self.__undoRedoService.addUndoRedoOperation(
           ModifyOperation(self.__cardClientRepository, card_vechi, card))
