from dataclasses import dataclass

from Domain.Entitate import Entitate


@dataclass
class Medicament(Entitate):
    numeMedicament: str
    producator: str
    pret: float
    reteta: str
