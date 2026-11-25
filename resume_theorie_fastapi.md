# Resume theorique - FastAPI

## 1. Qu'est-ce qu'une API

Une API (Application Programming Interface) permet a deux applications de communiquer.
Dans une API HTTP, le client envoie une requete a un serveur, puis le serveur retourne une reponse.

Une requete comprend notamment :

- une methode HTTP ;
- une URL ;
- eventuellement des parametres ;
- eventuellement un corps de donnees.

Une reponse comprend notamment :

- un code HTTP ;
- des en-tetes ;
- eventuellement un corps au format JSON.

## 2. FastAPI

FastAPI est un framework Python permettant de creer rapidement des API HTTP.

Ses principaux avantages sont :

- une syntaxe simple ;
- l'utilisation des types Python ;
- la validation automatique des donnees ;
- la generation automatique de la documentation ;
- de bonnes performances, grace a une architecture ASGI.

La documentation interactive est generalement accessible aux adresses `/docs` et `/redoc`.

## 3. Routes et methodes HTTP

Une route associe une URL a une fonction Python.

Exemples de methodes HTTP :

- `GET` : recuperer une ressource ou executer une lecture ;
- `POST` : envoyer des donnees pour creer ou effectuer une operation ;
- `PUT` : remplacer une ressource ;
- `PATCH` : modifier partiellement une ressource ;
- `DELETE` : supprimer une ressource.

Dans FastAPI, une route peut etre declaree avec des decorateurs, par exemple `@app.get(...)` ou `@app.post(...)`.

La partie apres la methode indique le chemin, par exemple `/api/hello`.

## 4. Parametres de requete

Les informations peuvent etre envoyees de plusieurs manieres.

### Parametres de chemin

Ils font partie de l'URL :

```text
/utilisateurs/42
```

### Parametres de requete

Ils sont places apres `?` dans l'URL :

```text
/api/hello?name=Alice
```

Dans FastAPI, ils peuvent etre declares avec `Query`.

### Corps de la requete

Le corps contient generalement des donnees JSON envoyees par un client.

Il est utilise pour les operations `POST`, `PUT` ou `PATCH`.

Dans FastAPI, il peut etre declare avec `Body`.

## 5. Validation des donnees

FastAPI utilise les annotations de types Python pour valider les parametres.

Par exemple :

- `int` impose une valeur entiere ;
- `float` impose une valeur decimale ;
- `str` impose une chaine de caracteres ;
- `Query(ge=0)` impose une valeur superieure ou egale a zero ;
- `Query(lt=100)` impose une valeur strictement inferieure a 100.

Lorsqu'une valeur ne respecte pas ces contraintes, FastAPI renvoie automatiquement une erreur HTTP avec les details du probleme.

## 6. Pydantic et les modeles DTO

Pydantic permet de definir la structure et les contraintes des objets echanges avec l'API.

Un modele Pydantic peut representer :

- les donnees attendues dans une requete : modele de requete ;
- les donnees retournees au client : modele de reponse.

Ces modeles sont souvent appeles DTO (Data Transfer Object), car ils decrivent les donnees qui transitent entre le client et le serveur.

Un DTO permet notamment de :

- garantir une structure de donnees claire ;
- centraliser les validations ;
- separer les donnees HTTP de la logique interne ;
- documenter automatiquement les champs attendus.

## 7. Dataclasses et reponses

Une dataclass est une classe Python utilisee pour representer des donnees.
Elle permet de reduire le code necessaire pour definir les attributs d'un objet.

La reponse doit respecter la structure attendue par l'API.
Pour indiquer explicitement cette structure, FastAPI propose l'argument `response_model`.

Une reponse peut aussi contenir des valeurs optionnelles :

```python
sol1: float | None = None
```

Cette notation signifie que le champ peut contenir un nombre flottant ou la valeur `None`.

## 8. Serialisation JSON

Les fonctions Python peuvent retourner des objets Python, comme des dictionnaires ou des modeles.

FastAPI les convertit automatiquement en JSON pour les envoyer au client.
Ce processus s'appelle la serialisation.

En sens inverse, les donnees JSON du corps de la requete sont converties en objets Python.
Ce processus s'appelle la deserialisation.

## 9. Codes de statut HTTP

Les codes de statut indiquent le resultat du traitement.

- `200` : requete reussie ;
- `201` : ressource creee ;
- `400` : requete invalide ;
- `422` : donnees non valides selon les contraintes FastAPI/Pydantic ;
- `404` : ressource non trouvee ;
- `500` : erreur interne du serveur.

## 10. Resolution d'une equation du second degre

Pour une equation de la forme `ax² + bx + c = 0`, on calcule le discriminant :

```text
delta = b² - 4ac
```

Trois cas sont possibles :

- `delta > 0` : deux solutions reelles ;
- `delta = 0` : une solution reelle double ;
- `delta < 0` : aucune solution reelle.

Les deux solutions sont calculees avec :

```text
(-b + sqrt(delta)) / (2a)
(-b - sqrt(delta)) / (2a)
```

Pour les operations mathematiques comme la racine carree, Python fournit notamment le module `math`.

## 11. Calcul de Fibonacci

La suite de Fibonacci est definie par :

- `fibo(0) = 0` ;
- `fibo(1) = 1` ;
- `fibo(n) = fibo(n - 1) + fibo(n - 2)`.

Elle peut etre implementee avec une fonction recursive.

Cette approche est simple a comprendre, mais elle recalcule plusieurs fois les memes valeurs.

La methode `@cache` permet de memoriser les resultats deja calcules.
Elle evite les recalculs inutiles et rend les appels suivants plus rapides.

## 12. Separation des responsabilites

Une application bien organisee separe les differents roles :

- les routes gerent les demandes HTTP ;
- les DTO definissent les donnees echangees ;
- les fonctions de traitement portent la logique metier ;
- le serveur lance l'application.

Cette organisation rend le projet plus lisible, plus facile a tester et plus facile a maintenir.

## 13. Serveur ASGI et Uvicorn

FastAPI est une application ASGI : elle communique avec un serveur compatible ASGI.

Uvicorn est un serveur ASGI qui peut lancer l'application FastAPI.

Le lancement peut etre configure avec :

- l'adresse de l'application ;
- le port ;
- le mode reload.

Le mode reload redemarre automatiquement le serveur lorsque les fichiers du projet sont modifies.
