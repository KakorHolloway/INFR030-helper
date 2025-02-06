# Kubernetes cours 

## Paramétrage de l'environnement 

A partir de deux ou trois machines ubuntu (2vCPU et 4gb de RAM), suivez les instructions suivantes :

Dans le fichier /etc/hosts mettez sur chaque machine les champs :

<ip de la vm> master-0
<ip de la vm> worker-0
....

https://medium.com/@subhampradhan966/kubeadm-setup-for-ubuntu-24-04-lts-f6a5fc67f0df

Si vous redémarrez, lancez la commande suivante sur tous les noeuds
```
kubeadm reset 
swapoff -a 
```

relancez la commande ```kubeadm init --pod-network-cidr=10.244.0.0/16```, faites le cp donné dans le résultat de la commande et refaite un join sur les workers. 


