# kube-notebook

Jupyter notebook for managing kubernetes operation


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

## Deploy to docker

```bash
k apply -f kube/deploy.yaml -n devops 

```