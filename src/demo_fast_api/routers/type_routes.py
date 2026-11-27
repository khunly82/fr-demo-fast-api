from typing import Annotated

from fastapi import APIRouter, Depends, Path
from sqlalchemy import select
from sqlalchemy.orm import Session

from demo_fast_api.domain.db import get_session
from demo_fast_api.domain.type import Type
from demo_fast_api.dto.responses import TypeResponse
from demo_fast_api.infrastructure.open_ai_service import OpenAIService

router = APIRouter(prefix='/type', tags=['Type'])

@router.get('', response_model=list[TypeResponse])
async def get_all(
    session: Annotated[Session, Depends(get_session)],
    open_ai_service: Annotated[OpenAIService, Depends(OpenAIService)]
):
    """
    Récupérer l'ensemble des types de pokemons
    """
    # connecter à la db et renvoyer la liste des types
    # stmt = text('select * from type')
    stmt = select(Type)
    result = session.scalars(stmt).all()
    # si la liste est vide se connecter à openai
    if not result:
        # et charger la db avec les données de l'api
        list_types = await open_ai_service.get_types()
        session.add_all([Type(**t)for t in list_types])
        session.flush()
        result = session.scalars(stmt).all()
    return result

@router.get('/{id}')
def get_by_id(id: Annotated[int, Path()]):
    """
    Si l'id n'existe pas renvoyer un code 404
    sinon renvoyer le nom, la couleur, la description, l'id
    et le nombre d'especes possédant ce type dans la db
    """
    pass

@router.post('', status_code=201)
def create():
    """ajouter un type dans la db"""
    pass

@router.put('/{id}')
def update(id: Annotated[int, Path()]):
    """mettre à jour un type dans la db"""
    pass

@router.delete('/{id}')
def delete(id: Annotated[int, Path()]):
    """supprimer un type de la db, si des especes sont associées au type ne pas supprimer et renvoyer un code 400"""
    pass


"""
READ -> GET
CREATE -> POST
UPDATE -> PUT (remplacer de la ressource) / PATCH (modification de la ressource)
DELETE -> DELETE

RECUPERER LES entêtes de la ressources -> HEAD
"""