# k8s/helm configuration for try.openbiosim.org

## How to install

Command to add the jupyterhub repo to helm. Only need to run
this once.

```
$ helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
$ helm repo update
```

Command both to install the notebook server, and to upgrade the 
notebook server.

```
$ helm upgrade --cleanup-on-fail --install notebook jupyterhub/jupyterhub --namespace notebook --create-namespace --version=3.3.7 --values notebook.yaml
```

## Authentication

We are using github authentication. This is automatic, and should almost 
be instant after the first login. This is based on setting up an oauth
app in the OpenBioSim organisation.

## Listing users

Get the HUB ID and then run

```
$ kubectl --namespace notebook logs hub-{GET HUB ID} | grep "User logged in"
```

(replacing the HUB ID as needed)


Prune by getting a root prompt on the pod

````
$ kubectl debug node/aks-mainpool-13388046-vmss000000 -it --image=mcr.microsoft.com/dotnet/runtime-deps:6.0
````

Then break out

````
$ chroot /host
````

Then list nodes using

````
$ crictl images
````

Remove unused images using

````
$ crictl --prune
````

