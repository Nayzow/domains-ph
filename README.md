# Domains.ph

## Description

L'application web Domains.ph a pour but de recenser et de cartographier des sites potentiels de phishing frauduleux. L'application est responsive et profite donc également d'un affichage pour mobile. 

La documentation de l'API FastApi et de l'application web Angular, ainsi que leur code source, sont disponible sur leurs liens respectifs sur Github. Une image Docker de chaque projet est également accessible sur Docker Hub via les liens fournis.

La configuration YAML pour le déploiement des services est également présentée ci-dessous. Enfin, un APM Elastic a été installé dans l'application web pour permettre sa supervision.

## Présentation

![presentation.gif](resources/presentation.gif)

## Documentation

### Frontend :
- Web App Angular (Typescript)
- Github : https://github.com/Nayzow/DNS-Services-Frontend
- Docker Hub : https://hub.docker.com/r/nayzow/dns-services-frontend

### Backend :
- Api FastApi (Python)
- Github : https://github.com/Nayzow/DNS-Services-API
- Docker Hub : https://hub.docker.com/r/nayzow/dns-services-api

### Nginx :

L'application web tourne sur un serveur nginx dont le proxy redirige les requêtes à l'url :

```bash
/api
```

Vers l'url de l'api définiti dans le fichier de l'application web Angular :

```bash
nginx.conf
```

## Déploiement

Le déploiement est configuré pour tourner en local. Pour déployer le projet il suffit de récupérer le fichier "docker-compose.yaml" avec le code ci-dessous :

```yaml
version: '3'
services:
  api:
    image: nayzow/dns-services-api
    ports:
      - "8888:8888"

  app:
    image: nayzow/dns-services-frontend
    ports:
      - "80:80"
```

Lien du fichier de déploiement : https://github.com/Nayzow/Domain-sh/blob/main/docker-compose.YAML

Et ensuite d'effectuer cette commande dans le répertoire courant du fichier "docker-compose.yaml" :

```bash
docker-compose up
```

L'application Web est désormais disponible à l'adresse http://localhost

L'API est désormais disponible à l'adresse http://localhost:8888

## Production

Vous pouvez également copier la configuration YAML dans la section custom stack sur Portainer ou sur un autre service d'orchéstration de containers.

Pour que le projet tourne dans un environnement de production il faut lancer l'application en mode production aprés avoir configurer la variable d'environnement "apiUrl" pour les requêtes cotés client dans l'application Angular, par exemple :

```typescript
export const environment = {  
  production: true,  
  apiUrl: 'http://40.68.218.243:8888'  
};
```

Dans le fichier :

```bash
src/environnements/environnement.ts 
```

## Supervision

Version de l'apm elastic pour superviser les containers :

```json
"elastic-apm-node" : ^3.42.0
```
