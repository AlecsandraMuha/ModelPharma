from Domain.medicament import Medicament
from Repository.RepositoryInMemory import RepositoryInMemory
from Tests.clear_f import clear_filename


def testMedicament():
    filename = "testmedicament.json"
    clear_filename(filename)

    open(filename, "w").close()

    test = RepositoryInMemory()

    assert test.read() == []

    medicament = Medicament("1", "colebil", "a", 15, "da")

    test.add(medicament)

    assert test.read("1") == medicament
