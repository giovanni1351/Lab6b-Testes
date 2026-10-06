# Lab6b-Testes

Laboratório 6b da disciplina de Simulação e Teste de Software.
As respostas e tabelas estão em `src/lab6b_testes/respostas.md`.

Com Python 3.14 e uv, prepare o ambiente com `uv sync` e execute
`uv run pytest -q`. Com o ambiente já preparado, use
`.venv/bin/python -m pytest -q`.

A execução completa apresenta **102 testes passando e 31 falhas intencionais**:
30 na versão do estagiário (exercício 2) e uma na versão errada de isenção
aplicada aos casos corrigidos (exercício 4). Essas implementações preservam
os defeitos pedidos pelo enunciado.

Para executar apenas os testes dos exercícios 1 e 3:

```sh
uv run pytest -q src/lab6b_testes/tarifa/test_estacionamento.py src/lab6b_testes/isencao/test_isencao.py
```

`test_colega.py` mantém os cinco casos originais e os cinco corrigidos,
executando cada conjunto contra a implementação correta e a errada.
