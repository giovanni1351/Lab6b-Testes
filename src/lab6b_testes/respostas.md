## Exercício 1

### (a) Implementação

`tarifa/estacionamento.py` calcula a tarifa e rejeita tempo negativo ou não inteiro. A divisão por 60 usa arredondamento para cima, pois uma fração de hora já é cobrada inteira.

### (b) Classes de equivalência

| Classe | Entrada (minutos inteiros) | Resultado | Representante |
| --- | --- | --- | --- |
| V1 | 0 a 15 | R$ 0,00 | 8 |
| V2 | 16 a 180 | R$ 12,00 | 100 |
| V3 | 181 a 240 | R$ 15,00 | 210 |
| V4 | 241 a 300 | R$ 18,00 | 270 |
| V5 | 301 a 360 | R$ 21,00 | 330 |
| V6 | 361 a 420 | R$ 24,00 | 390 |
| V7 | 421 a 480 | R$ 27,00 | 450 |
| V8 | 481 a 540 | R$ 30,00 | 510 |
| V9 | 541 a 600 | R$ 33,00 | 570 |
| V10 | 601 a 660 | R$ 36,00 | 630 |
| V11 | 661 a 720 | R$ 39,00 | 690 |
| V12 | Acima de 720 | R$ 60,00 | 1000 |
| I1 | Inteiros negativos | ValueError | -1 |
| I2 | Valores não inteiros | TypeError | 15.5 |

181 a 720 não é uma única classe quando distinguimos o valor cobrado: há nove intervalos com resultados diferentes. Embora usem a mesma fórmula, cada início de hora adicional cria uma fronteira.

### (c) Testes

A suíte inclui representantes, 0, os vizinhos de 15 e 180 e os três valores ao redor de cada fronteira de hora (239/240/241 até 659/660/661), além de 719/720/721. Entradas negativas e de tipo incorreto têm testes separados com `pytest.raises`. Cada caso válido possui um identificador com tempo e tarifa.

A validação segue a convenção `isinstance(minutos, int)` apresentada no laboratório; em Python, `bool` também é uma subclasse de `int`.
