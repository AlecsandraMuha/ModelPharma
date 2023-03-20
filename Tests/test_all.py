from Tests.testCardRepoJson import testCardClient
from Tests.testDomain import test_domain
from Tests.testMedicamentRepoJson import testMedicament
from Tests.testService import test_get_all
from Tests.testTranzactieRepoJson import testtranzactie
from Tests.test_undoredo import test_redo, test_undo


def test_all():
    test_domain()
    testtranzactie()
    testMedicament()
    testCardClient()
    test_get_all()
    test_redo()
    test_undo()
