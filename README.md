## Install dependencies

```bash
## Install poetry here: https://python-poetry.org/docs/
poetry install
```

## Run jupyterlab

```bash
poetry run python -m ipykernel install --user --name=nlp
poetry run jupyter lab --NotebookApp.token=nlp
```