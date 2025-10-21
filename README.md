# TrabalhoPratico1-TPPE

[![codecov](https://codecov.io/gh/yabamiah/trabalhoPratico1-TPPE/graph/badge.svg?token=BV1CPQE8SZ)](https://codecov.io/gh/yabamiah/trabalhoPratico1-TPPE)

Este projeto implementa a lógica de geração de rodadas, processamento de partidas e classificação para o Campeonato Brasileiro Série A.

## Como Executar os Testes

Para garantir que a aplicação funciona como esperado, siga os passos abaixo para configurar o ambiente e executar a suíte de testes.

### 1. Pré-requisitos (Configuração do Ambiente)

1. **Crie e ative um ambiente virtual:**

      * No macOS/Linux:

        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

      * No Windows:

        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

2. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

-----

### 2. Executando os Testes

Executa o arquivo all_tests.py, que agrega todos os casos de teste do unittest em uma suite, conforme solicitado nas especificações do trabalho.

```bash
python3 -m tests.all_tests
```

Executar todos os testes automaticamente:

```bash
pytest
```

Para gerar um relatório de cobertura e verificar quais partes do seu código estão sendo testadas:

```bash
pytest --cov=organizadorCampeonatoBrasileiro
```