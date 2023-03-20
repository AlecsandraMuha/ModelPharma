from typing import Protocol
from Domain.Entitate import Entitate


class Repository(Protocol):
    def read(self, idEntitate=None):
        ...

    def add(self, entitate: Entitate):
        ...

    def delete(self, idEntitate: str):
        ...

    def update(self, entitate: Entitate):
        ...
