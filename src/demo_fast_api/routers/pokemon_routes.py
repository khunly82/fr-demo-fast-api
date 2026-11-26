# @app.get('/pokemon/{numero}')
# async def get_full_pokemon(
#     numero: Annotated[int, Path()],
#     pokemon_service: Annotated[PokemonService, Depends(PokemonService)]
# ):
#     try:
#         pkmn: Pokemon = await pokemon_service.get_pokemon(numero)
#         return {
#             'numero': pkmn.id,
#             'nom': pkmn.name,
#             'poids': pkmn.weight / 10,
#             'taille': pkmn.height / 10
#         }
#     except ValueError as ex:
#         print(str(ex))
#         raise HTTPException(status_code=404)

# @app.post('/pokemons')
# async def get_full_pokemons(
#     numeros: Annotated[list[int], Body()],
#     pokemon_service: Annotated[PokemonService, Depends(PokemonService)],
#     open_ai_service: Annotated[OpenAIService, Depends(OpenAIService)],
# ):
#     try:
#         pokemons: list[Pokemon] = await asyncio.gather(*[
#             pokemon_service.get_pokemon(numero)
#             for numero in numeros
#         ])
#         desc = await open_ai_service.get_pokemons_description([
#             p.name for p in pokemons
#         ])
#         return [{
#             'numero': p.id,
#             'nom': p.name,
#             'poids': p.weight / 10,
#             'taille': p.height / 10,
#             'description': d
#         } for p, d in zip(pokemons, desc)]
        
#     except ValueError as ex:
#         print(str(ex))
#         raise HTTPException(status_code=404)
