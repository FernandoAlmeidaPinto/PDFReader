from typing import Optional

from fastapi import FastAPI

from ColetarInfos.index import FuxoLeituraPDF

app = FastAPI()

exemplo = 'Robert.pdf'
pdf_path = 'Exemplos/' + exemplo

@app.get("/")
def read_root():
    return FuxoLeituraPDF(pdf_path)