from Domain.cardClient import CardClient
from Domain.medicament import Medicament
from Domain.tranzactie import Tranzactie


def test_medicament():
    medicament = Medicament('1', 'paracetamol', 'a', 12, 'nu')
    assert medicament.idEntitate == '1'
    assert medicament.numeMedicament == 'paracetamol'
    assert medicament.producator == 'a'


def test_card():
    card = CardClient('1', 'vlad', 'anca',
                      '12.12.2002', '602543673652', '12.12.2020')
    assert card.idEntitate == '1'
    assert card.nume == 'vlad'
    assert card.prenume == 'anca'


def test_tranzactie():
    tranzactie = Tranzactie('1', '1', '1', '12', '12.12.2020 20:20')
    assert tranzactie.idEntitate == '1'
    assert tranzactie.nr_bucati == '12'
    assert tranzactie.datasiora == '12.12.2020 20:20'


def test_domain():
    test_card()
    test_medicament()
    test_tranzactie()
