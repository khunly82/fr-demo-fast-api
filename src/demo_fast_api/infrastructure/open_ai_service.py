import json
import os
from types import CoroutineType
from dotenv import load_dotenv

load_dotenv()
from httpx import AsyncClient


BASE_URL = 'https://api.openai.com/v1'



HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv('OPEN_AI_KEY')}'
}

class OpenAIService:

    async def get_pokemons_description(self, names: list[str]) -> CoroutineType[list[str]]:
        PRE_POMPT = [
            { 'role': 'developer', 'content': 'User va te donner une liste de pokemons tu devras lui renvoyer la liste des descriptions de chaque pokemon dans le même ordre' },
        ]

        JSON_SCHEMA = {
            'type': 'object',
            'required': ['descriptions'],
            'properties': { 'descriptions':
                { 'type': 'array', 'items': { 'type': 'string' } }
            }
        }
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

    async def get_types(self) -> CoroutineType[list[dict]]:
        PRE_POMPT = [
            { 'role': 'developer', 'content': 'Tu dois me donner la liste de tous les types (vol, feu, ...) qui existent dans Pokemon. Pour chacun des types donne moi le nom en francais, la description, une couleur en hexa (sans le #)' },
        ]

        JSON_SCHEMA = {
            'type': 'object',
            'required': ['types'],
            'properties': { 'types':
                { 'type': 'array', 'items': { 
                    'type': 'object', 
                    'required' : ['nom', 'couleur_hex', 'description'],
                    'properties': { 'couleur_hex': { 'pattern': '^[A-F0-9]{6}$' } }
                } }
            }
        }
        async with AsyncClient() as client:
            response = await client.post(f'{BASE_URL}/chat/completions', headers=HEADERS, json={
                'model': 'gpt-4o-mini',
                'messages': PRE_POMPT,
                'response_format': {
                    'type': 'json_schema',
                    'json_schema': {
                        'name': 'types',
                        'schema': JSON_SCHEMA
                    }
                } 
            }, timeout=300)
            return json.loads(
                response.json().get('choices')[0].get('message').get('content')
            ).get('types')


