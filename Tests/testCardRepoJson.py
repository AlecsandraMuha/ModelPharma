from Domain.cardClient import CardClient
from Repository.RepositoryInMemory import RepositoryInMemory
from Tests.clear_f import clear_filename


def testCardClient():
    filename = "testcard.json"
    clear_filename(filename)

    open(filename, "w").close()

    test = RepositoryInMemory()

    assert test.read() == []

    card = CardClient("1", "vlad", "ana", "12.12.2000",
                      "6029282726252", "12.12.2020")

    test.add(card)

    assert test.read("1") == card
