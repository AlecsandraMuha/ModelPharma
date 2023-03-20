import datetime
from functools import reduce

from Domain.CascadaDeleteOperation import CascadeDeleteOperation
from Domain.ModyObject import ModifyOperation
from Domain.addOperation import AddOperation
from Domain.deleteOperation import DeleteOperation
from Domain.multideleteOp import MultiDeleteOperation
from Repository.Repo import Repository
from Domain.tranzactie import Tranzactie
from Service.UndoRedoService import UndoRedoService
from ViewModel.MedVanzariViewModel import MedicamentVanzariViewModel


class TranzactieService:
    def __init__(self,
                 tranzactieRepository: Repository,
                 cardClientRepository: Repository,
                 medicamentRepository: Repository,
                 undoRedoService: UndoRedoService,
                 ):
        self.__tranzactieRepository = tranzactieRepository
        self.__medicamentRepository = medicamentRepository
        self.__cardClientRepository = cardClientRepository
        self.__undoRedoService = undoRedoService

    def getAll(self):
        return self.__tranzactieRepository.read()

    def add(self,
            idTr,
            idMedicament,
            idCard,
            nr_bucati,
            datasiora):
        if self.__medicamentRepository.read(idMedicament) is None:
            raise KeyError("Nu exista niciun medicament cu id-ul dat!")
        if idCard != "":
            list = self.__medicamentRepository.read()
            reteta = ''
            for index in list:
                if getattr(index, 'idEntitate') == idMedicament:
                    reteta = getattr(index, 'reteta')
            pret = 0
            for index in list:
                if getattr(index, 'idEntitate') == idMedicament:
                    pret = float(getattr(index, 'pret'))
            pret_final = 0
            if reteta == 'nu':
                pret_final = pret - 0.10 * pret
                print("s-a aplicat o reducere de 10% si pretul"
                      " devine:" + str(pret_final))
            elif reteta == 'da':
                pret_final = pret - 0.15 * pret
                print("s-a aplicat o reducere de 15% si "
                      "pretul devine:" + str(pret_final))
        else:
            print("nu se face reducere!")

        tranzactie = Tranzactie(
            idTr,
            idMedicament,
            idCard,
            nr_bucati,
            datasiora)
        self.__tranzactieRepository.add(tranzactie)
        self.__undoRedoService.addUndoRedoOperation(
            AddOperation(self.__tranzactieRepository, tranzactie))

    def delete(self, idTr):
        tranzactiestearsa = self.__tranzactieRepository.read(idTr)
        self.__tranzactieRepository.delete(idTr)
        self.__undoRedoService. \
            addUndoRedoOperation(DeleteOperation
                                 (self.__tranzactieRepository,
                                  tranzactiestearsa))

    def update(self, idTr, idMedicament, idCard, nr_bucati, datasiora):
        if self.__medicamentRepository.read(idMedicament) is None:
            raise KeyError("Nu exista niciun medicament cu id-ul dat!")
        tranzactie = Tranzactie(
            idTr,
            idMedicament,
            idCard,
            nr_bucati,
            datasiora,
        )
        trveche = self.__tranzactieRepository.read(idTr)
        self.__tranzactieRepository.update(tranzactie)
        self.__undoRedoService.addUndoRedoOperation(ModifyOperation
                                                    (self.
                                                     __tranzactieRepository,
                                                     trveche,
                                                     tranzactie))

    def Cautare_Full_Text(self, string: str):
        """
        Functia cauta un cuvant in lista de medicamente
        :param string: Cuvantul sau portiunea de cuvant pe care o cautam
        :return: Returneaza lista obiectelor care contin cuvantul cautat cu
        list comp + filter
        """
        lista1 = self.__medicamentRepository.read()
        b = list(filter(lambda x: string in x.numeMedicament or
                        string in x.producator or
                        string in x.reteta or
                        string in str(x.pret), lista1))

        lista = self.__cardClientRepository.read()
        a = list(filter(lambda x: string in x.nume or
                        string in x.prenume or
                        string in str(x.CNP) or
                        string in str(x.datanasterii) or
                        string in str(x.datainreg), lista))
        res_list = [y for x in [a, b] for y in x]
        return res_list

    def AfisareTranzactiiInterval(self, data1: datetime.datetime,
                                  data2: datetime.datetime):
        '''
        afiseaza tranzactiile dintr-un interval de zile dat
        :param data1: prima data
        :param data2: cea de-a doua data
        :return: afiseaza tranzactiile
        '''
        if data2 < data1:
            raise KeyError("Cea de-a doua data trebuie sa fie"
                           "mai mare decat prima")
        lista = []
        lista1 = self.__tranzactieRepository.read()
        for i in lista1:
            data_noua = getattr(i, 'datasiora')
            if data_noua >= data1 and data_noua <= data2:
                lista.append(i)
        return lista

    def suma4(self, lista):
        if lista == []:
            return 0
        return int(lista[-1]) + self.suma4(lista[:-1])

    def OrdoneazaDupaNrVanzari(self):
        '''
        ordoneaza descrescator medicamentele dupa nr lor de vanzari
        :return: lista ordonata descrescator
        '''
        nrdevanzari = {}
        rezultat = []
        for medicament in self.__medicamentRepository.read():
            nrdevanzari[medicament.idEntitate] = []
        for tranzactie in self.__tranzactieRepository.read():
            nrdevanzari[tranzactie.idMedicament].append(tranzactie.nr_bucati)
        for idMedicament in nrdevanzari:
            vanzari = nrdevanzari[idMedicament]
            suma = self.suma4(vanzari)
            if suma > 0:
                rezultat.append(MedicamentVanzariViewModel(
                    self.__medicamentRepository.read(idMedicament),
                    suma if suma else 0))
        return self.Sorted(rezultat, key=lambda nrvanz: nrvanz.nrvanzare,
                           reverse=True)

    def Stergere(self, idEntitate):
        '''

        :param med:
        :return:
        '''
        cascada = []
        for tranzactie in self.__tranzactieRepository.read():
            if tranzactie.idMedicament == idEntitate:
                cascada.append(tranzactie)
                self.__tranzactieRepository.delete(tranzactie.idEntitate)
        medicam = self.__medicamentRepository.read(idEntitate)
        cascada.append(medicam)

        self.__medicamentRepository.delete(idEntitate)

        self.__undoRedoService.addUndoRedoOperation(CascadeDeleteOperation(
            self.__medicamentRepository,
            self.__tranzactieRepository,
            cascada
        ))

    def Sorted(self, list, key=None, reverse=False):
        if reverse is False:
            for i in range(len(list) - 1):
                for j in range(i + 1, len(list)):
                    if key(list[i]) > key(list[j]):
                        list[i], list[j] = list[j], list[i]
        else:
            for i in range(len(list) - 1):
                for j in range(i + 1, len(list)):
                    if key(list[i]) < key(list[j]):
                        list[i], list[j] = list[j], list[i]
        return list

    def Ordonare_Descrescator_ValReduceri(self):
        '''
        Ordoneaza descrescator cardurile dupa valoarea reducerilor efectuate
        '''
        valoareReduceri = {}
        rezultat = []
        for card in self.__cardClientRepository.read():
            valoareReduceri[card.idEntitate] = []
        for tranzactie in self.__tranzactieRepository.read():
            if self.__medicamentRepository.read(
                    tranzactie.idMedicament).reteta == "da":
                valoareReduceri[tranzactie.idCard].append(
                    float(15 / 100) * self.__medicamentRepository.read(
                        tranzactie.idMedicament).pret *
                    float(tranzactie.nr_bucati))
            else:
                valoareReduceri[tranzactie.idCard].append(
                    float(10 / 100) * self.__medicamentRepository.read(
                        tranzactie.idMedicament).pret *
                    float(tranzactie.nr_bucati))

        for idCard in valoareReduceri:
            reduceri = valoareReduceri[idCard]
            rezultat.append({
                "cardClient": self.__cardClientRepository.read(
                    idCard),
                "valoarereducere": reduce(lambda x, y: x + y, reduceri)
            })

        return self.Sorted(rezultat,
                           key=lambda valoare: valoare["valoarereducere"],
                           reverse=True)

    def StergeTranzactiiInterval(self, data1: datetime.datetime,
                                 data2: datetime.datetime):
        '''
    sterge tranzactiile dintr-un interval de zile dat
    :param data1: prima data
    :param data2: a doua data
    :return: stergerea tranzactiilor
    '''
        if data2 < data1:
            raise KeyError("Cea de-a doua data trebuie sa fie"
                           "mai mare decat prima")

        exista = False
        tranzactii_sterse = []
        for tranzactie in self.__tranzactieRepository.read():
            if data1 <= tranzactie.datasiora <= data2:
                exista = True
                tranzactii_sterse.append(tranzactie)
                self.delete(tranzactie.idEntitate)
        self.__undoRedoService.addUndoRedoOperation(
            MultiDeleteOperation(self.__tranzactieRepository,
                                 tranzactii_sterse))

        if exista is False:
            raise KeyError(f'Nu exista nicio tranzactie intre '
                           f'{data1} si {data2}!')
