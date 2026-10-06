from lab6b_testes.tarifa.estacionamento import calcular_tarifa
import pytest

@pytest.mark.parametrize("minutos, esperado",[
    (14,0),
    (15,0),
    (16,12),
    (179,12),
    (180,12),
    (181,15),
    (239,15),
    (240,15),
    (241,18),
    (299,18),
    (300,18),
    (301,21),
    (359,21),
    (360,21),
    (361,24),
    (419,24),
    (420,24),
    (421,27),
    (479,27),
    (480,27),
    (481,30),
    (539,30),
    (540,30),
    (541,33),
    (599,33),
    (600,33),
    (601,36),
    (659,36),
    (660,36),
    (661,39),
    (719,39),
    (720,39),
    (721,60),
    (1000,60),

    ])
def test_valores_aceitos_na_tarifa(minutos, esperado):
    assert calcular_tarifa(minutos) == esperado