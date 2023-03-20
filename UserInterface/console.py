import string

from Repository.Exceptii import DataIncorecta, AddTranzactie
from Service.UndoRedoService import UndoRedoService
from Service.cardService import CardClientService
from Service.medicamentService import MedicamentService
from Service.tranzactieService import TranzactieService
from datetime import datetime
import random


class Consola:
    def __init__(self,
                 medicamentService: MedicamentService,
                 cardService: CardClientService,
                 tranzactieService: TranzactieService,
                 undoRedoService: UndoRedoService):
        self.__medicamentService = medicamentService
        self.__cardService = cardService
        self.__tranzactieService = tranzactieService
        self.__undoRedoService = undoRedoService

    def runMenu(self):
        while True:
            print("1. CRUD medicament")
            print("2. CRUD card")
            print("3. CRUD tranzactii")
            print("4. Cautare full text")
            print("5. Afișarea tuturor tranzacțiilor dintr-un interval"
                  " de zile dat")
            print("6. Afișarea medicamentelor ordonate descrescător "
                  "după numărul de vânzări")
            print("7. Afișarea cardurilor client ordonate descrescător după"
                  " valoarea reducerilor obținute")
            print("8. Ștergerea tuturor tranzacțiilor dintr-un anumit "
                  "interval de zile")
            print("9. Scumpirea cu un procentaj dat a tuturor medicamentelor "
                  "cu prețul mai mic decât o valoare dată.")
            print("s. StergeInCascada")
            print('u. Undo')
            print('r. Redo')
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.runCRUDMedicamentMenu()
            elif optiune == "2":
                self.runCRUDCardMenu()
            elif optiune == "3":
                self.runCRUDTranzactieMenu()
            elif optiune == "4":
                self.UiCautareFullText()
            elif optiune == "5":
                self.UiAfisareTranzactii()
            elif optiune == "6":
                self.UiOrdoneazaDupaNrVanzari()
            elif optiune == "7":
                self.UiOrdonareValReduceri()
            elif optiune == "8":
                self.UiStergereTranzactiiInterval()
            elif optiune == "9":
                self.UiScumpire()
            elif optiune == "s":
                self.StergeInCascada()
            elif optiune == 'u':
                self.__undoRedoService.undo()
            elif optiune == 'r':
                self.__undoRedoService.redo()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def runCRUDMedicamentMenu(self):
        while True:
            print("1. Adauga medicament")
            print("2. Sterge medicament")
            print("3. Modifica medicament")
            print("a. Afiseaza toate medicamentele")
            print("g.Generare random")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaMedicament()
            elif optiune == "2":
                self.uiStergeMedicament()
            elif optiune == "3":
                self.uiModificaMedicament()
            elif optiune == "a":
                self.showAllMedicamente()
            elif optiune == "g":
                self.runGenerareRandom()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def runCRUDCardMenu(self):
        while True:
            print("1. Adauga card")
            print("2. Sterge card")
            print("3. Modifica card")
            print("a. Afiseaza toate cardurile")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaCard()
            elif optiune == "2":
                self.uiStergeCard()
            elif optiune == "3":
                self.uiModificaCard()
            elif optiune == "a":
                self.showAllCard()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAdaugaMedicament(self):
        try:
            idMedicament = input("Dati id-ul medicamentului : ")
            numeMedicament = input("Dati numele medicamentului: ")
            producator = input("Dati producatorul medicamentului:")
            pret = float(input("Dati pretul medicamentului:"))
            reteta = input("Dati reteta (da/nu) a medicamentului:")

            self.__medicamentService.add(idMedicament,
                                         numeMedicament,
                                         producator,
                                         pret,
                                         reteta)
        except DataIncorecta as ID:
            print(ID)
        except Exception as e:
            print(e)

    def uiStergeMedicament(self):
        try:
            idMedicament = input("Dati id-ul"
                                 " medicamentului de sters: ")

            self.__medicamentService.delete(idMedicament)

        except DataIncorecta as ID:
            print(ID)
        except Exception as e:
            print(e)

    def uiModificaMedicament(self):
        try:
            idMedicament = input("Dati id-ul medicamentului"
                                 " de modificat: ")
            numeMedicament = input("Dati noul nume"
                                   " al medicamentului: ")
            producator = input("Dati noul producator"
                               " al medicamentului:")
            pret = float(input("Dati noua pret al"
                               " medicamentului:"))
            reteta = input("Dati noua reteta (da/nu)"
                           " a medicamentului:")

            self.__medicamentService.update(idMedicament,
                                            numeMedicament,
                                            producator,
                                            pret,
                                            reteta)
        except DataIncorecta as ID:
            print(ID)
        except Exception as e:
            print(e)

    def showAllMedicamente(self):
        for medicament in self.__medicamentService.getAll():
            print(medicament)

    def uiAdaugaCard(self):
        try:
            idCard = input("Dati id-ul cardului: ")
            nume = input("Dati numele clientului: ")
            prenume = input("Dati prenumele clientului: ")
            datanasterii = datetime.strptime(input("Dati "
                                             " data nasterii: "),
                                             "%d.%m.%Y")
            CNP = input("Dati CNP-ul: ")
            datainreg = datetime.strptime(input("Dati"
                                          " data inregistrarii: "),
                                          "%d.%m.%Y")
            self.__cardService.add(idCard,
                                   nume,
                                   prenume,
                                   datanasterii,
                                   CNP,
                                   datainreg)
        except DataIncorecta as ID:
            print(ID)
        except Exception as e:
            print(e)

    def uiStergeCard(self):
        try:
            idCard = input("Dati id-ul cardului de sters: ")

            self.__cardService.delete(idCard)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaCard(self):
        try:
            idCard = input("Dati id-ul cardului de modificat: ")
            nume = input("Dati noul nume al clientului: ")
            prenume = input("Dati noul prenume al clientului: ")
            datanasterii = datetime.strptime(input("Dati data "
                                                   "nasterii: "
                                                   ""), "%d.%m.%Y")
            CNP = input("Dati noul CNP: ")
            datainreg = datetime.strptime(input("Dati data"
                                                " inregistrarii: "
                                                ""), "%d.%m.%Y")

            self.__cardService.update(idCard, nume, prenume,
                                      datanasterii, CNP, datainreg)
        except DataIncorecta as ID:
            print(ID)
        except Exception as e:
            print(e)

    def showAllCard(self):
        for card in self.__cardService.getAll():
            print(card)

    def runCRUDTranzactieMenu(self):
        while True:
            print("1. Adauga tranzactie")
            print("2. Sterge tranzactie")
            print("3. Modifica tranzactie")
            print("a. Afiseaza toate tranzactiile")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaTranzactie()
            elif optiune == "2":
                self.uiStergeTranzactie()
            elif optiune == "3":
                self.uiModificaTranzactie()
            elif optiune == "a":
                self.showAllTranzactie()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAdaugaTranzactie(self):
        try:
            idTr = input("Dati id-ul tranzactiei: ")
            idMedicament = input("Dati id-ul medicamentului: ")
            idCard = input("Dati id-ul cardului: ")
            nr_bucati = input("Dati nr de bucati:")
            datasiora = datetime.strptime(input("Dati "
                                                "data si ora a "
                                                "inregistrarii:"
                                                " "), "%d.%m.%Y %H:%M")

            self.__tranzactieService.add(idTr, idMedicament,
                                         idCard, nr_bucati, datasiora)
        except DataIncorecta as ID:
            print(ID)
        except Exception as e:
            print(e)

    def uiStergeTranzactie(self):
        try:
            idTr = input("Dati id-ul tranzactiei de sters: ")

            self.__tranzactieService.delete(idTr)
        except DataIncorecta as ID:
            print(ID)
        except Exception as e:
            print(e)

    def uiModificaTranzactie(self):
        try:
            idTr = input("Dati  id-ul tranzactiei: ")
            idMedicament = input("Dati id-ul medicamentului: ")
            idCard = input("Dati noul id-ul cardului: ")
            nr_bucati = input("Dati nr de bucati:")
            datasiora = datetime.strptime(input("Dati noua "
                                                "data si ora a"
                                                " inregistrarii:"
                                                " "), "%d.%m.%Y %H:%M")

            self.__tranzactieService.update(idTr, idMedicament,
                                            idCard, nr_bucati, datasiora)
        except DataIncorecta as ID:
            print(ID)
        except Exception as e:
            print(e)

    def showAllTranzactie(self):
        for tranzactie in self.__tranzactieService.getAll():
            print(tranzactie)

    def UiCautareFullText(self):
        string = input("Dati textul pe care vreti sa il cautati:")
        lista = self.__tranzactieService.Cautare_Full_Text(string)
        for i in lista:
            print(lista)

    def runGenerareRandom(self):
        idMedicament = 1
        n = int(input("Dati numarul de medicamente pe care "
                      "vreti sa il generati: "))
        numemed = ["nurofen", "bioflu", "colebil", "ACC"]
        ret = ["da", "nu"]
        list = ["a", "b", "c"]
        med = string.digits
        for i in range(n):
            try:
                idMedicament = str(random.randint(10, 200))
                numeMedicament = random.choice(numemed)
                producator = random.choice(list)
                pret = float(random.randint(10, 200))
                reteta = random.choice(ret)
                self.__medicamentService.add(idMedicament,
                                             numeMedicament,
                                             producator,
                                             pret,
                                             reteta)
            except Exception as e:
                print(e)

    def UiAfisareTranzactii(self):
        try:
            data1 = datetime.strptime(input("Dati prima "
                                            "data:"), "%d.%m.%Y %H:%M")
            data2 = datetime.strptime(input("Dati a doua "
                                            "data:"), "%d.%m.%Y %H:%M")
            list = self.__tranzactieService.\
                AfisareTranzactiiInterval(data1, data2)

            for i in list:
                print(i)
        except Exception as e:
            print("Data si ora trebuie introduse corect. Reincercati!")

    def UiOrdoneazaDupaNrVanzari(self):
        for nr_vanzari in self.__tranzactieService \
                .OrdoneazaDupaNrVanzari():
            print(nr_vanzari)

    def StergeInCascada(self):
        try:
            idEntitate = input("Dati id-ul"
                               "medicamentului de sters: ")

            self.__tranzactieService.Stergere(idEntitate)

        except DataIncorecta as ID:
            print(ID)
        except Exception as e:
            print(e)

    def UiOrdonareValReduceri(self):
        for i in self.__tranzactieService.\
                Ordonare_Descrescator_ValReduceri():
            print(i)

    def UiStergereTranzactiiInterval(self):
        try:
            data1 = datetime.strptime(input("Dati prima "
                                            "data:"), "%d.%m.%Y %H:%M")
            data2 = datetime.strptime(input("Dati a doua"
                                            " data:"), "%d.%m.%Y %H:%M")
            list = self.__tranzactieService.\
                StergeTranzactiiInterval(data1, data2)
        except Exception as e:
            print("Data si ora trebuie introduse corect. Reincercati!")

    def UiScumpire(self):
        try:
            pretdat = float(input("Dati pretul:"))
            procent = float(input("Dati procentul cu care "
                                  "sa se faca scumpirea:"))
            self.__medicamentService.\
                ScumpireCuProcentaj(procent, pretdat)
        except Exception as e:
            print("Procentul si pretul trebuie "
                  "introduse corect. Reincercati!")
