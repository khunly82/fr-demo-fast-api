1.1. Ajouter une fonctionalité fibo dans l'api
*cette fonction prendra un entier en paramètre et retournera le nombre de fibonacci correspondant au nombre*

1.2. Ajouter une fonction equation(a: float, b: float, c: float)
*cette fonction renverra un dictionnaire correspondant aux à la solution d'une equation du type ax² + bx + c = 0*
```python
result = {
    'delta': ...,
    'solution1': ...
    'solution2': ...
}
```

1.3. Ajouter une nouvelle fonction contact (POST /api/contact)
    dont le but sera d'envoyer un email à l'administrateur de l'api (à vous)
    parametres: 
        - nom: str (max: 50)
        - email: str email valide
        - content: str (max: 1000)

    info envoi mail
    host: ssl0.ovh.net
    port: 465
    username: tf@khunly.be
    password: test1234=

1.4 Exo recap

- Installer le package 'httpx'

```sh
uv add httpx
```

- Créer une classe PokemonService
    - get_pokemon(numero: int)
      *permet de se connecter à l'api pokeapi pour récupérer les infos d'un pokemon*
- Créer une classe OpenAIService
    - get_description(nom: str)
      *permet de se connecter à openAI pour récupérer la description du pokemon*
- Ajouter une fonctionnalité dans l'api FastApi
    @app.get('/pokemon/{numero}')
    - get_pokemon_full_info(numero: Annotated[int, ?])
    Injecter les 2 services OpenAIService et PokemonService
    pour renvoyer un dto {
        numero,
        nom,
        taille en m du pokemon
        poids en kg du pokemon
        description d'openAI du pokemon
    }

    