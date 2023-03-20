from Domain.cardClient import CardClient
from Domain.medValidator import MedValidator
from Domain.medicament import Medicament
from Repository.RepositoryInMemory import RepositoryInMemory
from Service.UndoRedoService import UndoRedoService
from Service.cardService import CardClientService
from Service.medicamentService import MedicamentService


def test_undo():
    medicamentRepository = RepositoryInMemory()
    medicament_validator = MedValidator()
    undoRedoService = UndoRedoService()
    medicamentService = MedicamentService(medicamentRepository,
                                          medicament_validator,
                                          undoRedoService)

    medicament1 = Medicament("1", "colebil", "a", 15, "da")
    medicament2 = Medicament("2", "ACC", "a", 15, "da")

    medicamentService.add("1", "colebil", "a", 15, "da")
    undoRedoService.undo()

    assert len(medicamentRepository.read()) == 0

    medicamentService.add("1", "colebil", "a", 15, "da")
    medicamentService.add("2", "ACC", "a", 15, "da")
    undoRedoService.undo()

    assert medicamentRepository.read() == [medicament2]

    undoRedoService.undo()
    assert medicamentRepository.read() == []


def test_redo():
    cardClientRepository = RepositoryInMemory()
    undoRedoService = UndoRedoService()
    cardClientService = CardClientService(cardClientRepository,
                                          undoRedoService)

    card1 = CardClient("1", "C", "M", "123", "12.05.2002",
                       "12.12.2002")
    card2 = CardClient("2", "A", "V", "111",
                       "12.05.2002", "12.12.2002")
    card3 = CardClient("3", "L", "B", "333",
                       "12.05.2002", "12.12.2002")

    cardClientService.add(
        "1", "C", "M", "123", "12.05.2002", "12.12.2002"
    )
    cardClientService.add(
        "2", "A", "V", "111", "12.05.2002", "12.12.2002"
    )
    cardClientService.add(
        "3", "L", "B", "333", "12.05.2002", "12.12.2002"
    )

    undoRedoService.undo()
    assert cardClientRepository.read() == [card1, card2]
    undoRedoService.redo()
    assert cardClientRepository.read() == [card1, card2, card3]

    undoRedoService.undo()
    undoRedoService.undo()
    assert cardClientRepository.read() == [card1]
    undoRedoService.redo()
    assert cardClientRepository.read() == [card1, card2]
