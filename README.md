# kube-notebook

Jupyter notebook for managing kubernetes operations.



## Build docker image


```bash
cd docker
docker build . -t devops-notebook
```

Publish to docker hub

```bash
docker tag  devops-notebook -t mdnmdn/devops-notebook
git push mdnmdn/devops-notebook
```

## Deploy to k8s


Deploy with simple ingress:

```bash
kubectl apply -k ./kube/with-ingress
```

Deploy without ingress (port-forward):

```bash
kubectl apply -k ./kube/base
```

In order to delete all the resouces:

```bash
kubectl delete -k ./kube/with-ingress
```



### Customization

In order to set the namespace update the [kube/base/kustomization.yaml](kube/base/kustomization.yaml).

The default password is set in [kube/base/custom-env.yaml](kube/base/custom-env.yaml).

The ingress configuration should be set in [kube/with-ingress/custom-ingress.yaml](kube/with-ingress/custom-ingress.yaml).


## TODO

* Add persistence with volume
* Add git sync
* Add default notebook

