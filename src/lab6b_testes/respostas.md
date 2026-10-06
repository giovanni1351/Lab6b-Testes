## exercício 1

### (b) classes de equivalência

| classe | entrada (minutos inteiros) | resultado | representante |
| --- | --- | --- | --- |
| v1 | 0 a 15 | r$ 0,00 | 8 |
| v2 | 16 a 180 | r$ 12,00 | 100 |
| v3 | 181 a 240 | r$ 15,00 | 210 |
| v4 | 241 a 300 | r$ 18,00 | 270 |
| v5 | 301 a 360 | r$ 21,00 | 330 |
| v6 | 361 a 420 | r$ 24,00 | 390 |
| v7 | 421 a 480 | r$ 27,00 | 450 |
| v8 | 481 a 540 | r$ 30,00 | 510 |
| v9 | 541 a 600 | r$ 33,00 | 570 |
| v10 | 601 a 660 | r$ 36,00 | 630 |
| v11 | 661 a 720 | r$ 39,00 | 690 |
| v12 | acima de 720 | r$ 60,00 | 1000 |
| i1 | inteiros negativos | erro de valor | -1 |
| i2 | valores não inteiros | erro de tipo | 15.5 |

não dá pra colocar de 181 a 720 em uma classe só, porque o preço muda nessa faixa. são nove faixas com preços diferentes. cada vez que começa mais uma hora, mesmo sem completar ela, o valor sobe 3 reais.

## exercício 2

### (a) erros encontrados olhando o código

| defeito | menor entrada | obtido | esperado | correção |
| --- | --- | --- | --- | --- |
| dá erro para zero por usar `<= 0` | 0 | erro de valor | r$ 0,00 | usar `< 0` |
| cobra com 15 minutos por usar `< 15` | 15 | r$ 12,00 | r$ 0,00 | usar `<= 15` |
| não cobra a hora incompleta por usar `// 60` | 181 | r$ 12,00 | r$ 15,00 | usar `ceil((minutos - 180) / 60)` |
| cobra a diária com 720 minutos por usar `< 720` | 720 | r$ 60,00 | r$ 39,00 | usar `<= 720` |

entre 181 e 719 minutos, a conta fica errada quando sobra uma parte de hora depois dos 180 minutos. quando as horas extras são completas, como em 240 ou 300 minutos, o valor fica certo.

### (b) resultado dos testes

sim, os testes pegam os quatro erros: zero dando erro, cobrança com 15 minutos, hora incompleta sem cobrar e diária começando antes da hora. deu **30 falhas e 24 testes passando**.

### (c) apenas quatro representantes

não pegaria nenhum erro. com 8 minutos é grátis, com 100 custa 12 reais, com 300 são duas horas extras completas e com 1000 já cobra a diária. esses quatro valores dão certo mesmo no código errado. faltam valores perto dos limites e com horas incompletas.

## exercício 3

### (a) tabela completa

s = sim; n = não. c = credencial; v = compras ≥ r$ 150,00; a = cadastro no aplicativo; t = permanência ≤ 240 minutos.

| regra | c | v | a | t | isento |
| --- | --- | --- | --- | --- | --- |
| c1 | s | s | s | s | s |
| c2 | s | s | s | n | s |
| c3 | s | s | n | s | s |
| c4 | s | s | n | n | s |
| c5 | s | n | s | s | s |
| c6 | s | n | s | n | s |
| c7 | s | n | n | s | s |
| c8 | s | n | n | n | s |
| c9 | n | s | s | s | s |
| c10 | n | s | s | n | n |
| c11 | n | s | n | s | s |
| c12 | n | s | n | n | n |
| c13 | n | n | s | s | s |
| c14 | n | n | s | n | n |
| c15 | n | n | n | s | n |
| c16 | n | n | n | n | n |

tabela reduzida (x = tanto faz o valor, o resultado deve ser o mesmo):

| condição / ação | r1 | r2 | r3 | r4 | r5 |
| --- | --- | --- | --- | --- | --- |
| credencial | s | n | n | n | n |
| compras ≥ r$ 150,00 | x | x | s | n | n |
| cadastro no aplicativo | x | x | x | s | n |
| permanência ≤ 240 minutos | x | n | s | s | x |
| isento | s | n | s | s | n |
| regras completas cobertas | c1–c8 | c10, c12, c14, c16 | c9, c11 | c13 | c15, c16 |

- r1: quem tem credencial não paga. por isso compras, aplicativo e tempo ficam com x.
- r2: sem credencial e passando de 240 minutos, tem que pagar. compras e aplicativo ficam com x porque não mudam isso.
- r3: comprou pelo menos 150 reais e ficou até 240 minutos, não paga. tanto faz ter aplicativo ou não, então ele fica com x.
- r4: sem credencial e com menos de 150 reais em compras, precisa ter aplicativo e ficar até 240 minutos pra não pagar. aqui não tem x.
- r5: sem credencial, sem aplicativo e com menos de 150 reais em compras, tem que pagar. o tempo fica com x porque não muda isso.

a c16 aparece em r2 e r5, mas nas duas o cliente paga. juntando as regras, todas as 16 combinações estão cobertas.

## exercício 4

### (a) onde o código errado falha

no código errado, quem tem cadastro no aplicativo não paga, mesmo passando de 240 minutos.

ele erra nas regras **c10 e c14**: o cliente não tem credencial, tem aplicativo e ficou mais de 240 minutos. o valor da compra não muda esse erro. o código diz que não precisa pagar, mas deveria pagar.

os cinco testes do colega passam nos dois códigos. em r2 o cliente não tem aplicativo. em r4 ele tem, mas fica dentro do tempo. nenhum teste usa um cliente sem credencial, com aplicativo e passando do tempo.

### (b) correção mantendo cinco casos

o x do aplicativo em r2 quer dizer que ter cadastro ou não deveria dar o mesmo resultado. o colega só testou sem cadastro. colocando um cliente com cadastro, dá pra ver se ele continua pagando quando passa de 240 minutos.

| regra | credencial | compra (r$) | aplicativo | minutos | esperado |
| --- | --- | --- | --- | --- | --- |
| r1 | sim | 149,99 | não | 241 | sim |
| r2 | não | 150,00 | sim | 241 | não |
| r3 | não | 150,00 | não | 240 | sim |
| r4 | não | 149,99 | sim | 240 | sim |
| r5 | não | 149,99 | não | 240 | não |

agora r2 testa a c10 e pega o erro. continuam sendo cinco casos, usando valores perto dos limites de compra e tempo.

### (c) regra geral para os x

nos x, escolha um valor que ajude a mostrar um erro. se o resultado é não pagar, coloque valores que normalmente fariam o cliente pagar. se o resultado é pagar, coloque valores que normalmente ajudariam a não pagar. assim dá pra conferir se o x realmente não muda o resultado. um valor só pode não pegar todos os erros, então às vezes precisa testar outras combinações.
