from Domain.medicament import Medicament
from Domain.MedError import MedicamentError


class MedValidator:
    def valideaza(self, medicament: Medicament):
        erori = []
        if medicament.pret < 0:
            erori.append("Pretul trebuie sa "
                         "fie strict pozitiv!")
        if medicament.reteta not in ["da", "nu"]:
            erori.append("Daca medicamentul necesita reteta "
                         "scrieti 'da', respectiv nu"
                         " in caz contrar")
        if len(erori) > 0:
            raise MedicamentError(erori)
