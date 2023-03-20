from Domain.medValidator import MedValidator
from Repository.RepositoryJson import RepositoryJson
from Service.UndoRedoService import UndoRedoService
from Service.cardService import CardClientService
from Service.medicamentService import MedicamentService
from Service.tranzactieService import TranzactieService
from Tests.test_all import test_all
from UserInterface.console import Consola


def main():
    undoRedoService = UndoRedoService()

    medicamentRepositoryJson = RepositoryJson("medicament.json")
    medicamentValidator = MedValidator()
    medicamentService = MedicamentService(medicamentRepositoryJson,
                                          medicamentValidator,
                                          undoRedoService)

    cardRepositoryJson = RepositoryJson("card.json")
    cardService = CardClientService(cardRepositoryJson,
                                    undoRedoService)

    tranzactieRepositoryJson = RepositoryJson("tranzactie.json")
    tranzactieService = TranzactieService(
        tranzactieRepositoryJson,
        cardRepositoryJson,
        medicamentRepositoryJson,
        undoRedoService)

    consola = Consola(medicamentService, cardService,
                      tranzactieService, undoRedoService)

    consola.runMenu()


main()
