# SmartFlat
Projet Domotique

## Installation site
* cloner le projet et installer les dépendances
```bash
## clone le projet
$ git clone git@github.com:felixcharvin/SmartFlat.git

## télécharge & installe les dépendances
$ cd SmartFlat/smartflat && npm install
```

* installer nodemon en global (permet de recharger le serveur à chaque modification)
```bash
$ npm install -g nodemon
```

## Configuration pour le raspberry pi
* modifier 'localhost' par l'IP du raspberry dans /vuejs/config/global.js
* ajouter "--host <IP_RASPBERRY> --port <PORT>" à la ligne 9 (scripts:dev:) dans le fichier package.json

## Lancement du site
* dans un premier terminal
```bash
## lancement de l'API avec nodemon
$ nodemon server.js

## lancement du site (mode développement)
$ npm run dev
```
* URL de l'API: [http://localhost:3000/api/](http://localhost:3000/api/)
* URL du site: [http://localhost:8080](http://localhost:8080)
