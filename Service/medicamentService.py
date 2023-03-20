from Domain.ModyObject import ModifyOperation
from Domain.addOperation import AddOperation
from Domain.deleteOperation import DeleteOperation
from Domain.medValidator import MedValidator
from Domain.medicament import Medicament
from Domain.multiupdateOp import MultiUpdateOperation
from Repository.Repo import Repository
from Service.UndoRedoService import UndoRedoService


class MedicamentService:
    def __init__(self, medicamentRepository: Repository,
                 medicamentValidator: MedValidator,
                 undoRedoService: UndoRedoService):

        self.__medicamentRepository = medicamentRepository
        self.__medicamentValidator = medicamentValidator
        self.__undoRedoService = undoRedoService

    def getAll(self):
        return self.__medicamentRepository.read()

    def add(self, idMedicament, numeMedicament, producator, pret, reteta):
        def functie(x): return self.__medicamentRepository.add(x)
        medicament = Medicament(idMedicament,
                                numeMedicament,
                                producator,
                                pret,
                                reteta)
        self.__medicamentValidator.valideaza(medicament)
        functie(medicament)
        self.__undoRedoService.addUndoRedoOperation(
            AddOperation(self.__medicamentRepository, medicament))

    def delete(self, idMedicament):
        def functie(x): return self.__medicamentRepository.delete(x)
        medsters = self.__medicamentRepository.read(idMedicament)
        functie(idMedicament)
        self.__undoRedoService.addUndoRedoOperation(DeleteOperation
                                                    (self.
                                                     __medicamentRepository,
                                                        medsters))

    def update(self, idMedicament, numeMedicament, producator,
               pret, reteta):
        def functie(x): return self.__medicamentRepository.update(x)
        medsters = self.__medicamentRepository.read(idMedicament)
        medicament = Medicament(idMedicament, numeMedicament,
                                producator, pret, reteta)
        self.__medicamentValidator.valideaza(medicament)
        functie(medicament)
        self.__undoRedoService.addUndoRedoOperation(ModifyOperation
                                                    (self.
                                                     __medicamentRepository,
                                                        medicament,
                                                        medsters))

    def ScumpireCuProcentaj(self, procent: float, pretdat: float):
        '''
        se scumpeste medicamentul cu pretul mai mic
        decat pretul dat cu un anumit procentaj
        :param procent: procent dat
        :param pretdat: pret dat
        :return: medicamentul scumpit
        '''
        medicamentemodificate = []
        list = self.__medicamentRepository.read()
        for i in list:
            pret = getattr(i, "pret")
            pret = float(pret)
            if pret < pretdat:
                medicamentemodificate.append(i)
                pret_final = pret + procent / 100 * pret
                medicament = Medicament(getattr(i, "idEntitate"),
                                        getattr(i, "numeMedicament"),
                                        getattr(i, "producator"),
                                        pret_final,
                                        getattr(i, "reteta"))
                self.__medicamentRepository.update(medicament)
                self.__undoRedoService.addUndoRedoOperation(
                    MultiUpdateOperation(self.__medicamentRepository,
                                         self.__medicamentRepository.read(),
                                         medicamentemodificate))
