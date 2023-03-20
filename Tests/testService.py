from Domain.cardClient import CardClient
from Domain.medValidator import MedValidator
from Domain.medicament import Medicament
from Repository.RepositoryInMemory import RepositoryInMemory
from Service.UndoRedoService import UndoRedoService
from Service.cardService import CardClientService
from Service.medicamentService import MedicamentService


def test_get_all():
    repository_med = RepositoryInMemory()
    validare_med = MedValidator()
    undoRedoService = UndoRedoService()
    service_med = MedicamentService(repository_med, validare_med,
                                    undoRedoService)

    test1 = Medicament("1", "colebil", "a", 15, "da")
    test2 = Medicament("2", "ACC", "a", 10, "da")
    service_med.add("1", "colebil", "a", 15, "da")
    service_med.add("2", "ACC", "a", 10, "da")

    medicamente = service_med.getAll()
    assert len(medicamente) == 2
    assert medicamente[0] == test1
    assert medicamente[1] == test2

    repository_card = RepositoryInMemory()
    service_card = CardClientService(repository_card, undoRedoService)

    test3 = CardClient("1", "vlad", "ana", "12.12.2000",
                       "6029282726252", "12.12.2020")
    test4 = CardClient("2", "popa", "anca", "12.10.2000",
                       "6029282706765", "17.12.2020")
    service_card.add("1", "vlad", "ana", "12.12.2000",
                     "6029282726252", "12.12.2020")
    service_card.add("2", "popa", "anca", "12.10.2000",
                     "6029282706765", "17.12.2020")

    carduri = service_card.getAll()
    assert len(carduri) == 2
    assert carduri[0] == test3
    assert carduri[1] == test4
