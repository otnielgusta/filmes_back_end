# main.py
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

from auth import autenticar, get_headers
from consts import EM_CARTAZ, POPULAR, TOP_RATED, CHEGANDO, base_url

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/filmes")
def listar_filmes():
    lista_filmes = [EM_CARTAZ, POPULAR, TOP_RATED, CHEGANDO]
    return lista_filmes

@app.get("/detalhe")
def buscar_detalhe(item_id: int):
    header = get_headers()
    resposta = requests.get(f"{base_url}/3/movie/{item_id}?language=pt-BR", headers=header)
    return resposta.json()


@app.get("/auth")
def auth():
    return autenticar()