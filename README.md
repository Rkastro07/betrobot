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
python update_odds.py --url https://sua-api.com/odds --param sport=football
```

Voce tambem pode definir `ODDS_API_TOKEN` para enviar autenticacao Bearer. Se nenhuma URL for informada, o script utilizara `https://example.com/api/odds`.

Defina a URL da sua API com `--url` ou `ODDS_API_URL` para usar o endpoint correto.


Depois de gerar `odds.json`, execute `python interface.py` para visualizar as odds em uma página web simples em `http://localhost:5000`.


