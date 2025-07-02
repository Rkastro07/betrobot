# Betrobot Odds Updater

Este repositório contém um exemplo simples de como fazer uma requisição HTTP para atualizar as odds de um serviço externo.

## Instalação

1. Certifique-se de ter o Python 3 instalado.
2. Instale as dependências executando:

```bash
pip install -r requirements.txt
```

## Uso

Execute o script `update_odds.py` para buscar as odds do endpoint configurado e salvar o resultado em `odds.json`:

```bash
python update_odds.py
```

Altere a variável `api_url` no arquivo para o endpoint real da sua API de apostas.
