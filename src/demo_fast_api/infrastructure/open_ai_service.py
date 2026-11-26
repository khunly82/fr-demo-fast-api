import json
import os
from types import CoroutineType
from dotenv import load_dotenv

load_dotenv()
from httpx import AsyncClient


BASE_URL = 'https://api.openai.com/v1'

PRE_POMPT = [
    { 'role': 'developer', 'content': 'User va te donner une liste de pokemons tu devras lui renvoyer la liste des descriptions de chaque pokemon dans le même ordre' }
]

HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv('OPEN_AI_KEY')}'
}

JSON_SCHEMA = {
    'type': 'object',
    'required': ['descriptions'],
    'properties': { 'descriptions':
        { 'type': 'array', 'items': { 'type': 'string' } }
    }
}

class OpenAIService:

    async def get_pokemons_description(self, names: list[str]) -> CoroutineType[list[str]]:
        async with AsyncClient() as client:
            response = await client.post(f'{BASE_URL}/chat/completions', headers=HEADERS, json={
                'model': 'gpt-4o-mini',
                'messages': [
                    *PRE_POMPT,
                    { 'role': 'user', 'content': ','.join(names) }
                ],
                'response_format': {
                    'type': 'json_schema',
                    'json_schema': {
                        'name': 'descriptions',
                        'schema': JSON_SCHEMA
                    }
                } 
            }, timeout=300)
            return json.loads(
                response.json().get('choices')[0].get('message').get('content')
            ).get('descriptions')


