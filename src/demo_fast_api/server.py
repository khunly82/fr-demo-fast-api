from functools import cache
import math
from typing import Annotated

import uvicorn
from fastapi import Body, FastAPI, Query

from demo_fast_api.dto.queries import EquationQuery
from demo_fast_api.dto.responses import EquationResponse

app = FastAPI()

@app.get('/api/hello')
def say_hello(name: Annotated[str, Query()] = 'World'):
    return f'Hello {name} !!'

@app.get('/api/fibo', response_model=int)
@cache
def fibo(nb: Annotated[int, Query(ge=0, lt=100)] = 0):
    if nb <= 1:
        return nb
    return fibo(nb - 1) + fibo(nb - 2)


@app.post('/api/equation', response_model=EquationResponse)
def equation(dto: Annotated[EquationQuery, Body()]):
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

def main():
    uvicorn.run('demo_fast_api.server:app', port=8080, reload=True)