from dataclasses import dataclass
from Domain.medicament import Medicament


@dataclass
class MedicamentVanzariViewModel:
    medicament: Medicament
    nrvanzare: float

    def __str__(self):
        return f'{self.medicament} are nr de vanzari: {self.nrvanzare}'
