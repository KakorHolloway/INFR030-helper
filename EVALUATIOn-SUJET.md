# Sujet d'évaluation 

Le but de cet évaluation sera de déployer sur Kubernetes une application : Bookstack 

Pour ce faire, vous devrez créer les éléments suivants :

- Deux déploiement (un mariadb, et un autre avec bookstack). Afin de définir ces déploiement et les variables d'environnement associées, vous pourrez utiliser les exemples docker-compose ci joint : https://docs.linuxserver.io/images/docker-bookstack/#docker-cli-click-here-for-more-info et https://hub.docker.com/_/mysql. Attention la variable d'environnement APP_URL doit contenir l'url d'accès depuis l'extérieur à l'application bookstack. Une variable app_key, nécéssitera la mise en place d'une clé que vous pouvez générer lors de l'execution de commandes dans le conteneur bookstack. 

Vous pouvez utiliser la valeur suivante :
```base64:cBgxMm49Z++Tb7f/GHy1xdaGUwz9LCTagITUmnzu/R4=```

Les images que vous pouvez utiliser sont les suivantes : lscr.io/linuxserver/bookstack:latest et lscr.io/linuxserver/mariadb:latest
- Créez le secret qui stockera les mots de passe d'accès et de configuration de la bdd
- Stockez dans un pv nfs (192.168.1.56 /Volume1/public/nfs-share-openshift/groupe-x) ou un hostpath si vous êtes en local la base de donnée (/var/lib/mysql)
- Exposez votre service d'accès à bookstack via un nodeport si vous êtes en local ou une route si vous êtes sur openshift en vous aidant de l'exemple ci-dessous : 

```
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: flask
spec:
  host: flask-demo.apps.openshift.kakor.ovh
  port:
    targetPort: 5000
  tls:
    insecureEdgeTerminationPolicy: Redirect
    termination: edge
  to:
    kind: Service
    name: flask
    weight: 100
  wildcardPolicy: None
```
- Afin que je puisse connaitre les membres de chaque groupe, créez un fichier DOCUMENTATION.md qui vous identifie.