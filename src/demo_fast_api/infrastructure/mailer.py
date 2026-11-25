import os

from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType


class Mailer:

    _config = ConnectionConfig(
        USE_CREDENTIALS=True,
        MAIL_USERNAME=os.getenv('SMTP.USERNAME'),
        MAIL_PASSWORD=os.getenv('SMTP.PASSWORD'),
        MAIL_PORT=int(os.getenv('SMTP.PORT', '465')),
        MAIL_SERVER=os.getenv('SMTP.HOST'),
        MAIL_STARTTLS=False,
        MAIL_SSL_TLS=True,
        MAIL_FROM=os.getenv('SMTP.USERNAME')
    )
    _dep = FastMail(_config)

    async def send_mail(
        self,
        to: list[str], 
        subject: str, 
        body: str, 
        replyTo: list[str]
    ):
        return await self._dep.send_message(MessageSchema(
            recipients=to,
            subject=subject,
            body=body,
            reply_to=replyTo,
            subtype=MessageType.html
        ))
        