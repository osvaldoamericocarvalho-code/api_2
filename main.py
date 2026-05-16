from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/teste")
def hello_world():
    return {"mensagem": "Hello World"}


# http://127.0.0.1:8000/soma/3/2
@app.post("/soma/{numero1}/{numero2}")
def soma(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


# http://127.0.0.1:8000/soma_formato2?numero1=3&numero2=2
@app.post("/soma_formato2")
def soma_formato2(numero1: int, numero2: int):
    total = numero1 + numero2
    return {"resultado": total}


class Numeros(BaseModel):
    numero1: int
    numero2: int


# 'http://127.0.0.1:8000/soma_formato3'
#   -d '{
#   "numero1": 3,
#   "numero2": 2
# }'
@app.post("/soma_formato3")
def soma_formato3(numeros: Numeros):
    total = numeros.numero1 + numeros.numero2
    return {"resultado": total}
