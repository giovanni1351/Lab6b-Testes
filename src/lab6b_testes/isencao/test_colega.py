import pytest

from lab6b_testes.isencao.isencao import isento
from lab6b_testes.isencao.isento_errado import isento as isento_errado


CASOS_COLEGA = [
    (True, 0.00, False, 100, True),
    (False, 200.00, False, 300, False),
    (False, 200.00, False, 100, True),
    (False, 50.00, True, 100, True),
    (False, 50.00, False, 100, False),
]

CASOS_CORRIGIDOS = [
    (True, 149.99, False, 241, True),
    (False, 150.00, True, 241, False),
    (False, 150.00, False, 240, True),
    (False, 149.99, True, 240, True),
    (False, 149.99, False, 240, False),
]

IDS = ["R1", "R2", "R3", "R4", "R5"]


@pytest.mark.parametrize("pcd,compra,app,minutos,esperado", CASOS_COLEGA, ids=IDS)
def test_colega_na_implementacao_correta(pcd, compra, app, minutos, esperado):
    assert isento(pcd, compra, app, minutos) is esperado


@pytest.mark.parametrize("pcd,compra,app,minutos,esperado", CASOS_COLEGA, ids=IDS)
def test_colega_na_implementacao_errada(pcd, compra, app, minutos, esperado):
    assert isento_errado(pcd, compra, app, minutos) is esperado


@pytest.mark.parametrize("pcd,compra,app,minutos,esperado", CASOS_CORRIGIDOS, ids=IDS)
def test_corrigido_na_implementacao_correta(pcd, compra, app, minutos, esperado):
    assert isento(pcd, compra, app, minutos) is esperado


@pytest.mark.parametrize("pcd,compra,app,minutos,esperado", CASOS_CORRIGIDOS, ids=IDS)
def test_corrigido_na_implementacao_errada(pcd, compra, app, minutos, esperado):
    assert isento_errado(pcd, compra, app, minutos) is esperado
