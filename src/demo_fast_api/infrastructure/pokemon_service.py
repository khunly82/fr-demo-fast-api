from httpx import AsyncClient

from demo_fast_api.models.pokemon import Pokemon

BASE_URL = 'https://pokeapi.co/api/v2'

class PokemonService:
    async def get_pokemon(self, numero: int):
        async with AsyncClient() as client:
            response = await client.get(f'{BASE_URL}/pokemon/{numero}')
            # deserialiser le json en dictionnaire python
            
            if response.status_code == 200:
                return Pokemon.model_validate_json(response.text)
            raise ValueError('The id does not exists')