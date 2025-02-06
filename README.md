# Kubernetes cours 

## Paramétrage de l'environnement 

A partir de deux ou trois machines ubuntu (2vCPU et 4gb de RAM), suivez les instructions suivantes :

Dans le fichier /etc/hosts mettez sur chaque machine les champs :

```
<ip de la vm> master-0
<ip de la vm> worker-0
....
```

https://medium.com/@subhampradhan966/kubeadm-setup-for-ubuntu-24-04-lts-f6a5fc67f0df

Si vous redémarrez, lancez la commande suivante sur tous les noeuds
```
kubeadm reset 
swapoff -a 
```

relancez la commande ```kubeadm init --pod-network-cidr=10.244.0.0/16```, faites le cp donné dans le résultat de la commande et refaite un join sur les workers. 

## POUR CEUX QUI N'ONT PLUS LES VMS 

Téléchargez le lien suivant : https://github.com/okd-project/okd/releases/download/4.15.0-0.okd-2024-03-10-010116/openshift-client-windows-4.15.0-0.okd-2024-03-10-010116.zip

Récupérez le fichier oc.exe et mettez le dans un dossier spécifique (ex: C:/Users/monuser/exe)

Ouvrez le programme variable d'environnement et ajoutez ce chemin dans le path. 

Une fois fait, réouvrez un invite de commande et au lancez la commande de connexion récupérée sur le site :

https://console-openshift-console.apps.openshift.kakor.ovh



