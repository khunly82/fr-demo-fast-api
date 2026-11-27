from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, Path
from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from demo_fast_api.domain.db import get_session
from demo_fast_api.domain.espece import Espece
from demo_fast_api.domain.type import Type
from demo_fast_api.dto.requests import TypeRequest
from demo_fast_api.dto.responses import TypeDetailsResponse, TypeResponse
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

@router.get('/{id}', response_model=TypeDetailsResponse)
def get_by_id(
    id: Annotated[int, Path()],
    session: Annotated[Session, Depends(get_session)],
):
    """
    Si l'id n'existe pas renvoyer un code 404
    sinon renvoyer le nom, la couleur, la description, l'id
    et le nombre d'especes possédant ce type dans la db
    """
    stmt = select(Type).where(Type.id == id)
    type = session.scalars(stmt).one_or_none()
    if not type:
        raise HTTPException(status_code=404)
    stmt2 = (
        select(func.count())
        .select_from(Espece)
        .where(or_(Espece.type1_id == id, Espece.type2_id == id))
    )
    return TypeDetailsResponse(
        **type.__dict__,
        nb_especes = session.scalar(stmt2)
    )
    

@router.post('', status_code=201, response_model=int)
def create(
    session: Annotated[Session, Depends(get_session)],
    dto: Annotated[TypeRequest, Body()],
):
    """ajouter un type dans la db"""
    stmt = select(Type).where(Type.nom == dto.nom)
    type: Type|None = session.scalars(stmt).one_or_none()
    if type:
        raise HTTPException(status_code=409, detail="Le nom du type existe deja")
    t = Type(**dto.__dict__)
    session.add(t)
    session.flush()
    return t.id

@router.put('/{id}')
def update(
    id: Annotated[int, Path()],
    session: Annotated[Session, Depends(get_session)],
    dto: Annotated[TypeRequest, Body()],
):
    """mettre à jour un type dans la db"""
    stmt = select(Type).where(Type.nom == dto.nom, Type.id != id)
    type: Type|None = session.scalars(stmt).one_or_none()
    if type:
        raise HTTPException(status_code=409, detail="Le nom du type existe deja")
    type_to_update = session.scalars(select(Type).where(Type.id == id)).one_or_none()
    if not type_to_update:
        raise HTTPException(status_code=404)
    type_to_update.nom = dto.nom
    type_to_update.description = dto.description
    type_to_update.couleur_hex = dto.couleur_hex
    return type_to_update.id

@router.delete('/{id}')
def delete(
    id: Annotated[int, Path()],
    session: Annotated[Session, Depends(get_session)],
):
    """supprimer un type de la db, si des especes sont associées au type ne pas supprimer et renvoyer un code 400"""
    type_to_delete = session.scalars(select(Type).where(Type.id == id)).one_or_none()
    if not type_to_delete:
        raise HTTPException(status_code=404)
    stmt2 = (
        select(func.count())
        .select_from(Espece)
        .where(or_(Espece.type1_id == id, Espece.type2_id == id))
    )
    if session.scalar(stmt2):
        raise HTTPException(status_code=400)
    session.delete(type_to_delete)
    


"""
READ -> GET
CREATE -> POST
UPDATE -> PUT (remplacer de la ressource) / PATCH (modification de la ressource)
DELETE -> DELETE

RECUPERER LES entêtes de la ressources -> HEAD
"""