from dataclasses import dataclass

from Domain.Entitate import Entitate


@dataclass
class CardClient(Entitate):
    nume: str
    prenume: str
    datanasterii: str
    CNP: str
    datainreg: str
