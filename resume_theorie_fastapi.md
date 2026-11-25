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

## 14. Base path de l'application

FastAPI peut recevoir un `root_path`.

Le root path represente le prefixe public commun a toutes les routes.
Par exemple, avec `root_path="/api"` :

- une route `/hello` est exposee publiquement sous `/api/hello` ;
- une route `/contact` est exposee publiquement sous `/api/contact`.

Cette notion est utile lorsqu'une application est placee derriere un proxy ou un reverse proxy.
La configuration doit correspondre au chemin utilise par l'environnement de production.

## 15. Validation avancee avec Pydantic

Pydantic permet d'utiliser des contraintes plus precises que les types simples.

Exemples de contraintes presentes dans les exercices :

- `max_length=50` : longueur maximale d'une chaine ;
- `max_length=1000` : longueur maximale du contenu d'un message ;
- `EmailStr` : format d'une adresse e-mail valide ;
- `PositiveFloat` : nombre flottant strictement positif ;
- `NegativeFloat` : nombre flottant strictement negatif.

Pour valider une adresse e-mail, Pydantic necessite un validateur adapte, comme `EmailStr`.

Les contraintes peuvent etre combinees avec les annotations Python afin de produire une documentation claire et des erreurs de validation automatiques.

## 16. E-mail, SMTP et FastAPI-Mail

Pour envoyer un e-mail, une application se connecte generalement a un serveur SMTP.

Les principaux parametres de configuration sont :

- l'hote SMTP ;
- le port ;
- le nom d'utilisateur ;
- le mot de passe ;
- le type de chiffrement ;
- l'adresse d'expedition.

Le port 465 est souvent utilise avec une connexion SMTP directe utilisant SSL/TLS.

FastAPI-Mail fournit des classes pour :

- configurer la connexion SMTP ;
- construire un message ;
- definir les destinataires ;
- definir l'objet ;
- envoyer un contenu HTML ;
- indiquer une adresse de reponse.

## 17. Variables d'environnement

Les informations sensibles ou propres a chaque environnement ne doivent pas etre inscrites directement dans le code.

On utilise souvent des variables d'environnement pour separer :

- les identifiants SMTP ;
- les mots de passe ;
- les cle API ;
- les URLs de services externes ;
- les ports et autres parametres de deploiement.

Python peut lire ces valeurs avec `os.getenv(...)`.

Le package `python-dotenv` permet de charger des variables depuis un fichier `.env` avec `load_dotenv()`.

Un fichier `.env` ne doit pas etre versionne lorsqu'il contient des secrets.
Il doit etre presente dans le depot sous forme d'exemple, par exemple `.env.example`, sans valeurs sensibles.

## 18. Reponses HTTP et exceptions

Une route peut preciser son code de reponse attendu avec `status_code`.

Par exemple, une creation ou une operation ayant reussi peut utiliser `201`.

Lorsqu'une erreur est connue, FastAPI permet de lever une `HTTPException`.

Une exception HTTP contient notamment :

- un code HTTP ;
- un message ou un detail ;
- eventuellement des informations supplementaires.

Il est preferable de ne pas renvoyer au client des informations techniques sensibles.
A la place, l'erreur peut etre enregistree dans un fichier de logs tout en renvoyant au client un message adapte.

## 19. Programmation asynchrone

FastAPI peut executer des fonctions synchrones ou asynchrones.

Une fonction asynchrone est declaree avec `async def`.
Une operation attendue est declenchee avec `await`.

Cette approche est utile lorsqu'une operation attend une ressource externe :

- reponse d'une API HTTP ;
- envoi d'un e-mail ;
- acces a une base de donnees ;
- lecture ou ecriture de fichier.

Pendant l'attente, le programme peut traiter d'autres operations.
Cela evite de bloquer inutilement le serveur.

## 20. Injection de dependances

L'injection de dependances permet de fournir automatiquement a une route les objets dont elle a besoin.

Dans FastAPI, elle est declaree avec `Depends(...)`.
Le framework construit ou recupere la dependance, puis la transmet a la fonction.

Cette methode permet :

- de separer la route de la construction des services ;
- de reutiliser un meme service ;
- de faciliter les tests ;
- d'appliquer une logique commune a plusieurs routes ;
- de remplacer une implementation facilement.

Dans l'exemple du formulaire de contact, le mailer est fourni comme dependance a la route.

## 21. Infrastructure et services

Une application peut etre organisee en plusieurs couches.

La couche `dto` definit les donnees echangees.
La couche `infrastructure` contient les outils techniques, comme l'envoi d'e-mails.
La couche `server` expose les routes HTTP.

Les services peuvent encapsuler des acces a des API externes :

- `PokemonService` interroge PokeAPI ;
- `OpenAIService` demande une description a OpenAI.

Cette organisation evite que les routes melangent directement la logique HTTP, les transformations de donnees et les appels externes.

## 22. Appels HTTP externes avec httpx

`httpx` est un client HTTP pour Python.

Il permet notamment :

- d'envoyer des requetes GET, POST, PUT ou DELETE ;
- d'utiliser les clients HTTP de maniere synchrone ou asynchrone ;
- d'envoyer des en-tetes ;
- de lire une reponse JSON ;
- de gerer les erreurs HTTP.

Pour plusieurs operations FastAPI, un client asynchrone est adapte.
Il utilise `async def` et `await` pour ne pas bloquer le serveur pendant les appels externes.

## 23. API PokeAPI

PokeAPI est une API publique fournissant des informations sur les Pokemon.

Pour obtenir un Pokemon, l'application peut interroger une route publique contenant son numero.

Les informations utiles peuvent notamment etre :

- le numero ;
- le nom ;
- la taille ;
- le poids ;
- d'autres donnees propres a la reponse PokeAPI.

La taille et le poids fournis par l'API sont generalement des valeurs exprimees dans leurs propres unites.
Une conversion peut etre necessaire pour les afficher en metres ou en kilogrammes.

Le service doit transformer la reponse externe en un objet ou un DTO exploite par l'application.

## 24. Appels a OpenAI

OpenAIService peut etre charge de demander une description d'un Pokemon a un modele d'IA.

Dans ce type d'integration :

- les informations du Pokemon constituent le contexte ;
- le nom ou les caracteristiques peuvent servir a construire une instruction ;
- la reponse du modele est extraite et retournee par le service ;
- la cle API doit rester cote serveur ;
- la cle ne doit jamais etre exposee dans le navigateur ou le depots.

Cette approche doit aussi prendre en compte les couts, les limites d'utilisation, les erreurs du service et les delais de reponse.

## 25. DTO combinant plusieurs sources

Lorsqu'une route combine plusieurs services, elle peut produire un nouveau DTO.

Par exemple, le resultat d'un Pokemon peut contenir :

- son numero ;
- son nom ;
- sa taille en metres ;
- son poids en kilogrammes ;
- sa description generee.

Ce DTO constitue un contrat clair entre l'API FastAPI et ses clients.
Il masque les structures parfois complexes des API externes.

## 26. Parametres de chemin avances

Dans une route comme `/pokemon/{numero}`, `numero` est un parametre de chemin.

Ce parametre peut etre contraint avec une annotation FastAPI.
Par exemple, il est possible d'imposer un entier positif ou borne.

Les contraintes peuvent etre declarees avec `Query`, `Path` ou des types Pydantic selon le contexte.

## 27. Corps contenant une liste

Une route peut recevoir une liste d'objets ou une liste de nombres dans son corps JSON.

Par exemple :

- une liste de numeros de Pokemon ;
- une limite maximale de dix elements ;
- une verification d'unicite.

Pydantic peut valider la longueur d'une liste avec une contrainte sur le modele ou sur le champ.

Les contraintes d'unicite peuvent etre implementees avec un validateur Pydantic.
Cela permet d'ecarter les doublons avant l'execution de la logique metier.

## 28. Exécution concurrente avec asyncio.gather

Lorsque plusieurs appels externes sont independants, ils peuvent etre executes de maniere concurrente.

`asyncio.gather(...)` attend plusieurs operations asynchrones et retourne leurs resultats.

Cela permet notamment d'interroger PokeAPI pour plusieurs Pokemon simultanement.

La concurrence differencie deux notions :

- parallelisme : plusieurs operations s'executent reellement en meme temps ;
- concurrence : plusieurs operations peuvent progresser pendant leurs attentes.

Avec des appels HTTP asynchrones, la concurrence permet souvent d'obtenir tous les resultats sans attendre chaque requete l'une apres l'autre.
