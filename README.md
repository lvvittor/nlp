## Download preprocessed datasets

[Link to Google Drive](https://drive.google.com/drive/folders/1r7K3apA_rGbjXh3fYxzX08VVmowZ9_p-?usp=sharing)

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

