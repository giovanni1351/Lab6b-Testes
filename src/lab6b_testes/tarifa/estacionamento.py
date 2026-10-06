


from math import ceil


def calcular_tarifa(minutos: int) -> float:
    if not isinstance(minutos,int):
        raise TypeError("Valor não inteiro")
    if minutos < 0:
        raise ValueError("Valor negativo")

    if minutos <= 15: 
        return 0
    if minutos <= 180:
        return 12
    if minutos <= 720:
        return 12 + ceil((minutos - 180)/60) * 3.0
    return 60
