# main.py
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

from starlette.middleware.cors import CORSMiddleware

from auth import autenticar, get_headers
from consts import EM_CARTAZ, POPULAR, TOP_RATED, CHEGANDO, base_url

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    # adicione outros origens conforme necessário
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/filmes")
def listar_filmes():
    lista_filmes = {
        "continue_assistindo":EM_CARTAZ,
        "popular":POPULAR,
    "melhores_avaliados": TOP_RATED,
    "chegando_agora":CHEGANDO
    }
    return lista_filmes

@app.get("/detalhe")
def buscar_detalhe(item_id: int):
    header = get_headers()
    resposta = requests.get(f"{base_url}/3/movie/{item_id}?language=pt-BR", headers=header)
    return resposta.json()


@app.get("/auth")
def auth():
    return autenticar()