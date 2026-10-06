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

## Exercício 2

### (a) Divergências por inspeção

| Defeito | Menor entrada | Obtido | Esperado | Correção |
| --- | --- | --- | --- | --- |
| Rejeita zero com `<= 0` | 0 | ValueError | R$ 0,00 | Usar `< 0` |
| Exclui 15 da tolerância com `< 15` | 15 | R$ 12,00 | R$ 0,00 | Usar `<= 15` |
| Trunca a hora adicional com `// 60` | 181 | R$ 12,00 | R$ 15,00 | Usar `ceil((minutos - 180) / 60)` |
| Aplica diária já em 720 com `< 720` | 720 | R$ 60,00 | R$ 39,00 | Usar `<= 720` |

O truncamento erra todos os tempos de 181 a 719 cujo adicional não seja múltiplo de 60. Nos múltiplos exatos, o cálculo coincide com o esperado.

### (b) Execução da suíte copiada

`test_estagiario.py` copia os mesmos dados e testes do exercício 1, mudando o import. A execução revela as quatro divergências: zero, tolerância, frações de hora e início antecipado da diária. Os resultados esperados continuam sendo os da especificação.

### (c) Apenas quatro representantes

8, 100, 300 e 1000 passam: 8 está dentro da tolerância, 100 na tarifa fixa, 300 tem duas horas adicionais exatas e 1000 já está na diária. Essa suíte não detecta nenhum dos quatro defeitos. Além de omitir fronteiras, trata como um só grupo a faixa que contém várias tarifas.

Resultado observado: **30 falhas e 24 testes passando**. As falhas são intencionais neste exercício, pois a implementação do slide deve ser preservada.

## Exercício 3

### (a) Tabela completa

S = sim; N = não. C = credencial; V = compras ≥ R$ 150,00; A = cadastro no aplicativo; T = permanência ≤ 240 minutos.

| Regra | C | V | A | T | Isento |
| --- | --- | --- | --- | --- | --- |
| C1 | S | S | S | S | S |
| C2 | S | S | S | N | S |
| C3 | S | S | N | S | S |
| C4 | S | S | N | N | S |
| C5 | S | N | S | S | S |
| C6 | S | N | S | N | S |
| C7 | S | N | N | S | S |
| C8 | S | N | N | N | S |
| C9 | N | S | S | S | S |
| C10 | N | S | S | N | N |
| C11 | N | S | N | S | S |
| C12 | N | S | N | N | N |
| C13 | N | N | S | S | S |
| C14 | N | N | S | N | N |
| C15 | N | N | N | S | N |
| C16 | N | N | N | N | N |

Tabela reduzida (X = condição indiferente):

| Condição / ação | R1 | R2 | R3 | R4 | R5 |
| --- | --- | --- | --- | --- | --- |
| Credencial | S | N | N | N | N |
| Compras ≥ R$ 150,00 | X | X | S | N | N |
| Cadastro no aplicativo | X | X | X | S | N |
| Permanência ≤ 240 minutos | X | N | S | S | X |
| Isento | S | N | S | S | N |
| Regras completas cobertas | C1–C8 | C10, C12, C14, C16 | C9, C11 | C13 | C15, C16 |

- R1: credencial garante isenção, então compras, aplicativo e tempo são X.
- R2: sem credencial e acima de 240 minutos, compras e aplicativo não concedem isenção, então ambos são X.
- R3: compras suficientes e tempo permitido garantem isenção, então aplicativo é X.
- R4: compras insuficientes tornam aplicativo e tempo necessários; não há X.
- R5: sem credencial, compras suficientes ou aplicativo, nenhum tempo concede isenção, então tempo é X.

As regras reduzidas podem se sobrepor em C16 (R2 e R5), mas ambas indicam False. A união cobre as 16 combinações.

### (b) Implementação

`isencao/isencao.py` implementa `pcd or (minutos <= 240 and (valor_compra >= 150 or cadastro_app))`, devolvendo um booleano.

### (c) Valores concretos

`test_isencao.py` tem cinco casos com ids R1 a R5. Compras e tempo usam 149,99/150,00 e 240/241. Em R1, os X desfavorecem a isenção; em R2, compras e aplicativo favorecem a isenção, verificando que o tempo ainda impede o benefício. R3 desativa o aplicativo e R5 usa tempo permitido.

Resultado: **5 testes passando**.
