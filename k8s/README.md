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
$ helm upgrade --cleanup-on-fail --install notebook jupyterhub/jupyterhub --namespace notebook --create-namespace --version=2.0.0 --values notebook.yaml
```
