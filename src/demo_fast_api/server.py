import os

from dotenv import load_dotenv

from demo_fast_api.infrastructure.mailer import Mailer

load_dotenv()

import math
from functools import cache
from typing import Annotated

import uvicorn
from fastapi import Body, Depends, FastAPI, Query
from fastapi.exceptions import HTTPException

from demo_fast_api.dto.requests import ContactRequest, EquationRequest
from demo_fast_api.dto.responses import EquationResponse

app = FastAPI(root_path='/api')

@app.get('/hello')
def say_hello(name: Annotated[str, Query()] = 'World'):
    return f'Hello {name} !!'

@app.get('/fibo', response_model=int)
@cache
def fibo(nb: Annotated[int, Query(ge=0, lt=100)] = 0):
    if nb <= 1:
        return nb
    return fibo(nb - 1) + fibo(nb - 2)


@app.post('/equation', response_model=EquationResponse)
def equation(dto: Annotated[EquationRequest, Body()]):
    a = dto.a
    b = dto.b
    c = dto.c
    delta = b**2 - 4 * a * c
    if delta >= 0:
        return {
            'delta': delta,
            'sol1': (-b + math.sqrt(delta)) / (2 * a),
            'sol2': (-b - math.sqrt(delta)) / (2 * a),
        }
    return { 'delta': delta }

@app.post('/contact', status_code=201)
async def contact(
    dto: Annotated[ContactRequest, Body()],
    mailer: Annotated[Mailer, Depends(Mailer)]
):
    try:
        await mailer.send_mail(
            to=['khun.ly@bstorm.be'],
            replyTo=[dto.email],
            subject=f'{dto.name} vous a envoyé un message',
            body=f'<p>Contenu du message: {dto.content}</p>'
        )
    except Exception as error:
        # logger l'erreur dans un fichier de log
        raise HTTPException(detail=str(error), status_code=500)

def main():
    uvicorn.run('demo_fast_api.server:app', port=8080, reload=True)