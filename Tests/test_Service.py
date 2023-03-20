from Domain.cardClient import CardClient
from Domain.medValidator import MedValidator
from Domain.medicament import Medicament
from Domain.tranzactie import Tranzactie
from Repository.RepositoryJson import RepositoryJson
from Service.UndoRedoService import UndoRedoService
from Service.cardService import CardClientService
from Service.medicamentService import MedicamentService
from Service.tranzactieService import TranzactieService
from Tests.clear_f import clear_filename
from datetime import datetime


def test_tr():
    filename1 = "testtranzactie.json"
    filename3 = "testcard.json"
    filename2 = "testmedicament.json"
    clear_filename(filename1)
    clear_filename(filename2)
    clear_filename(filename3)
    repository_tranzactie = RepositoryJson(filename1)
    repository_medicament = RepositoryJson(filename2)
    repository_card = RepositoryJson(filename3)
    undoRedoService = UndoRedoService()
    medicament_validator = MedValidator()
    medicament_service = MedicamentService(repository_medicament,
                                           medicament_validator,
                                           undoRedoService)
    medicament_service.add('1', 'Paracetamol', 'a', 8.0, 'nu')
    card_service = CardClientService(repository_card, undoRedoService)
    card_service.add('1', 'Popa', 'Ana',
                     '2341242143876', '26.12.2000', '13.11.2020')
    tranzactie_service = TranzactieService(repository_tranzactie,
                                           repository_medicament,
                                           repository_card,
                                           undoRedoService)
    tranzactie_service.add('1', '1', '1', '123', '11.12.2020 20:40')
    assert len(tranzactie_service.getAll()) == 1
    tranzactie_service.update('1', '1', 'nul', '123', '11.12.2020 20:40')
    for index in tranzactie_service.getAll():
        id = getattr(index, 'idEntitate')
        if id == '1':
            idCard = getattr(index, 'idCard')
    assert idCard == 'nul'
    tranzactie_service.delete('1')
    assert len(tranzactie_service.getAll()) == 0
