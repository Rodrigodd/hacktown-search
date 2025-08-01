# HackTown Search

Página simples para pesquisar por eventos no HackTown 2025.

https://rodrigodd.github.io/hacktown-search/


## Rodar localmente

Para rodar o projeto localmente, você pode usar qualquer servidor HTTP simples,
como o `http.server` do Python, e acessar a página através do navegador:

```bash
python -m http.server 8000
```

Para atualizar os dados dos events (`all_schedules.json`), execute o seguinte comando:

```bash
python fetch_all_schedules.py
```
