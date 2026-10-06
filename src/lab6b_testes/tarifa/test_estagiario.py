import pytest

from lab6b_testes.tarifa.estacionamento_estagiario import calcular_tarifa


@pytest.mark.parametrize(
    "minutos, esperado",
    [
        pytest.param(0, 0.00, id="0min-0reais"),
        pytest.param(8, 0.00, id="8min-0reais"),
        pytest.param(14, 0.00, id="14min-0reais"),
        pytest.param(15, 0.00, id="15min-0reais"),
        pytest.param(16, 12.00, id="16min-12reais"),
        pytest.param(100, 12.00, id="100min-12reais"),
        pytest.param(179, 12.00, id="179min-12reais"),
        pytest.param(180, 12.00, id="180min-12reais"),
        pytest.param(181, 15.00, id="181min-15reais"),
        pytest.param(210, 15.00, id="210min-15reais"),
        pytest.param(239, 15.00, id="239min-15reais"),
        pytest.param(240, 15.00, id="240min-15reais"),
        pytest.param(241, 18.00, id="241min-18reais"),
        pytest.param(270, 18.00, id="270min-18reais"),
        pytest.param(299, 18.00, id="299min-18reais"),
        pytest.param(300, 18.00, id="300min-18reais"),
        pytest.param(301, 21.00, id="301min-21reais"),
        pytest.param(330, 21.00, id="330min-21reais"),
        pytest.param(359, 21.00, id="359min-21reais"),
        pytest.param(360, 21.00, id="360min-21reais"),
        pytest.param(361, 24.00, id="361min-24reais"),
        pytest.param(390, 24.00, id="390min-24reais"),
        pytest.param(419, 24.00, id="419min-24reais"),
        pytest.param(420, 24.00, id="420min-24reais"),
        pytest.param(421, 27.00, id="421min-27reais"),
        pytest.param(450, 27.00, id="450min-27reais"),
        pytest.param(479, 27.00, id="479min-27reais"),
        pytest.param(480, 27.00, id="480min-27reais"),
        pytest.param(481, 30.00, id="481min-30reais"),
        pytest.param(510, 30.00, id="510min-30reais"),
        pytest.param(539, 30.00, id="539min-30reais"),
        pytest.param(540, 30.00, id="540min-30reais"),
        pytest.param(541, 33.00, id="541min-33reais"),
        pytest.param(570, 33.00, id="570min-33reais"),
        pytest.param(599, 33.00, id="599min-33reais"),
        pytest.param(600, 33.00, id="600min-33reais"),
        pytest.param(601, 36.00, id="601min-36reais"),
        pytest.param(630, 36.00, id="630min-36reais"),
        pytest.param(659, 36.00, id="659min-36reais"),
        pytest.param(660, 36.00, id="660min-36reais"),
        pytest.param(661, 39.00, id="661min-39reais"),
        pytest.param(690, 39.00, id="690min-39reais"),
        pytest.param(719, 39.00, id="719min-39reais"),
        pytest.param(720, 39.00, id="720min-39reais"),
        pytest.param(721, 60.00, id="721min-60reais"),
        pytest.param(1000, 60.00, id="1000min-60reais"),
    ],
)
def test_valores_aceitos_na_tarifa(minutos, esperado):
    assert calcular_tarifa(minutos) == esperado


@pytest.mark.parametrize("minutos", [-1, -60], ids=["limite-negativo", "negativo"])
def test_tempo_negativo(minutos):
    with pytest.raises(ValueError):
        calcular_tarifa(minutos)


@pytest.mark.parametrize(
    "minutos", [15.0, 15.5, "15", None, [], {}],
    ids=["float-integral", "float-fracionario", "texto", "nulo", "lista", "dicionario"],
)
def test_tempo_nao_inteiro(minutos):
    with pytest.raises(TypeError):
        calcular_tarifa(minutos)
