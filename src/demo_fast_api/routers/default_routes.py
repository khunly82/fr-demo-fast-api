from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, Query

from demo_fast_api.dto.requests import ContactRequest
from demo_fast_api.infrastructure.mailer import Mailer

router = APIRouter(tags=['Default'])

@router.get('/hello')
def say_hello(name: Annotated[str, Query()] = 'World'):
    return f'Hello {name} !!'


@router.post('/contact', status_code=201)
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

