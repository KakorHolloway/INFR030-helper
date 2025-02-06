Historique des commandes :

```
oc create configmap python --from-file=exo-4/app/app.py --dry-run=client -o yaml > exo-4/app-cm.yml
oc create secret generic mysql-secret --from-literal=password="B4teau123!" --dry-run=client -o yaml > exo-4/secret.yaml
oc apply -f exo-4/secret.yaml

oc apply -f exo-4/
```