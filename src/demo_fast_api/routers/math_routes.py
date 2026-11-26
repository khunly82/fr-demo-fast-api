

from functools import cache
import math
from typing import Annotated

from fastapi import APIRouter, Body, Query

from demo_fast_api.dto.requests import EquationRequest
from demo_fast_api.dto.responses import EquationResponse

router = APIRouter(prefix='/math', tags=['Math'])

@router.get('/fibo', response_model=int)
@cache
def fibo(nb: Annotated[int, Query(ge=0, lt=100)] = 0):
    if nb <= 1:
        return nb
    return fibo(nb - 1) + fibo(nb - 2)

@router.post('/equation', response_model=EquationResponse)
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
