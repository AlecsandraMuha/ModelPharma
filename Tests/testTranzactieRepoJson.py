from Domain.tranzactie import Tranzactie
from Repository.RepositoryInMemory import RepositoryInMemory
from Tests.clear_f import clear_filename


def testtranzactie():
    filename = "testtranzactie.json"
    clear_filename(filename)

    open(filename, "w").close()

    test = RepositoryInMemory()

    assert test.read() == []

    tranzactie = Tranzactie("1", "1", "1", "12", "12.12.2020 12:20")

    test.add(tranzactie)

    assert test.read("1") == tranzactie
