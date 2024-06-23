Prefect Gitlab CI
=====

## Prepare Gitlab Settings

- Gitlab Runner Tag: minikube

## Variables defined at Gitlab to push Image

- DOCKER_USER: for docker.io
- DOCKER_AUTH_TOKEN: for docker.io
- PREFECT_API_URL: http://prefect-server:4200/api

## Prepare ServiceAccount to pull Image

https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account

```sh
#Create Secret
kubectl create secret docker-registry myregistrykey \
--docker-server=index.docker.io \
--docker-username=${DOCKER_USER} \
--docker-password=${DOCKER_PASSWORD_OR_AUTH_TOKEN} \
--docker-email=${DOCKER_EMAIL} \
-n prefect

# Create ServiceAccount
kubectl create serviceaccount prefect \ 
-n prefect

# Attach Secret to ServiceAccount
kubectl patch serviceaccount prefect \
-p '{"imagePullSecrets": [{"name": "myregistrykey"}]}' \
-n prefect
```
