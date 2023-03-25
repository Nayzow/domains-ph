# Domains.ph Frontend

## Description

Frontend du projet Domains.ph. L'application web est réalisée avec Angular et le langage TypeScript. Elle comporte plusieurs pages affichant des listes de noms de domaines de phishing potentiellement frauduleux et permet également de les cartographier.

- Documentation de l'API : https://github.com/Nayzow/dns-services-api

- Documentation complete du projet pour installer l'application web et l'API: https://github.com/Nayzow/domains-ph

## Présentation

![presentation.gif](src/assets/images/presentation.gif)

## Installation

### Installation avec l'API pour profiter de l'affichage des données

Lien du fichier de déploiement : https://github.com/Nayzow/Domain-sh/blob/main/docker-compose.YAML

Ensuite d'effectuer cette commande dans le répertoire courant du fichier "docker-compose.yaml" :

```bash
docker-compose up
```

L'application Web est désormais disponible à l'adresse http://localhost

L'API est désormais disponible à l'adresse http://localhost:8888

### Installation classique

#### 1. Clonez le dépôt du projet en utilisant la commande

```bash
git clone https://github.com/Nayzow/DNS-Services-API
```

Assurez-vous d'avoir Node.js et npm installés sur votre ordinateur. Vous pouvez vérifier leur installation en ouvrant une invite de commande et en tapant node -v et npm -v.


#### 2. À la racine du projet, installez les dépendances en utilisant la commande

```bash
npm install
```

#### 3. Démarrez l'application en utilisant les commandes

```bash
dns-service-frontend@0.0.0 start
```

```bash
ng serve
```

L'application devrait maintenant être accessible à l'adresse http://localhost:4200/

### Installation avec Docker

Assurez-vous d'avoir Docker installé sur votre machine.

#### 1. Clonez le dépôt du projet en utilisant la commande

```bash
git clone https://github.com/Nayzow/DNS-Services-API
```

#### 2. À la racine du projet, Construisez l'image Docker à partir du fichier Dockerfile en utilisant la commande

```bash
docker build -t dns-services-frontend .
```

#### 3. Exécutez le conteneur en utilisant la commande

```bash
docker run --name dns-services-frontend -p 80:80 -d dns-services-frontend
```

L'application devrait maintenant être accessible à l'adresse http://localhost:80/ à l'aide d'un serveur nginx.

## Routes de l'application

Les routes de l'application sont définies dans le fichier app-routing.module.ts. Les routes disponibles sont :

```
/ : renvoie au menu principal (home).
```

```
/domains : voir la liste des domaines potentiellement frauduleux à partir d'un nom de domaine.
```

```
/domains/:domain : voir les données relatives à un nom de domaine.
```
