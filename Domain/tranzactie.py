from dataclasses import dataclass

from Domain.Entitate import Entitate


@dataclass
class Tranzactie(Entitate):
    idMedicament: str
    idCard: str
    nr_bucati: str
    datasiora: str
