# SmartFlat
Projet Domotique

## Installation site
* cloner le projet et installer les dépendances
```bash
## clone le projet
$ git clone git@github.com:felixcharvin/SmartFlat.git

## télécharge & installe les dépendances
$ cd SmartFlat/vuejs && npm install
```

* installer nodemon en global (permet de recharger le serveur à chaque modification)
```bash
$ npm install -g nodemon
```

## Lancement du site
* dans un premier terminal
```bash
## lancement de l'API avec nodemon
$ nodemon server.js

## lancement du site (mode développement)
$ npm run dev
```
* URL de l'API: [http://localhost:3000/api/<object>](http://localhost:3000/api/<object>)
* URL du site: [http://localhost:8080](http://localhost:8080)