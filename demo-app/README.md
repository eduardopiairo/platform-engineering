# demo-app

A minimal FastAPI application used to demo containerization, Kubernetes deployments, and the platform-engineering pipeline.

## Endpoints

| Path | Description |
| --- | --- |
| `/` | Basic hello-world response |
| `/healthz` | Liveness probe |
| `/readyz` | Readiness probe |
| `/info` | Hostname, start time, and `APP_*` env vars |

## Build

```bash
cd demo-app
docker build -t demo-app:0.0.1 .
```

## Run

```bash
docker run -p 8000:8000 demo-app:0.0.1
```

The app will be available at http://localhost:8000.

## Upload (push to Docker Hub)

```bash
# Authenticate
docker login

# Tag the image with your Docker Hub namespace
# (a bare "demo-app" tag targets the reserved "library/" namespace and will be denied)
docker tag demo-app:0.0.1 edpiairo/demo-app:0.0.1

# Push
docker push edpiairo/demo-app:0.0.1
```

## Create the demo-cluster with kind

```bash
# Make sure Docker is running
docker info

# Create the cluster and switch kubectl to it
kind create cluster --name demo-cluster
kubectl config use-context kind-demo-cluster
kubectl get nodes
```

To tear it down later:

```bash
kind delete cluster --name demo-cluster
```

## Deploy to the local kind cluster

```bash
kind load docker-image demo-app:0.0.1 --name demo-cluster
kubectl apply -f k8s/
```

## Install Argo CD (Helm)

```bash
# Add the Argo Helm repository
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update

# Install Argo CD into its own namespace with the local overrides
# (plain HTTP, no Dex, and the "ci" account used by the cd job)
helm upgrade --install argocd argo/argo-cd --version 10.9.2 \
  --namespace argocd \
  --create-namespace \
  -f demo-app/charts/argocd/values.yaml

# Wait for the pods to be ready
kubectl get pods -n argocd -w
```

Access the UI:

```bash
# Port-forward the Argo CD server
kubectl port-forward svc/argocd-server -n argocd 8080:80

# Get the initial admin password (username: admin)
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d; echo
```

The UI will be available at http://localhost:8080.

Register the demo-app with Argo CD:

```bash
kubectl apply -f demo-app/charts/argocd/demo-app-application.yaml
```

## Continuous delivery (Argo CD sync)

After the `ci` job pushes the image and commits the new `appVersion`, the `cd`
job in [demo-app-build.yml](../.github/workflows/demo-app-build.yml) runs on the
self-hosted runner (an ARC pod in the kind cluster, see
[self-hosted-runner/README.md](self-hosted-runner/README.md)), installs the `argocd` CLI and
calls `argocd app sync demo-app`, then waits until the app is synced and healthy.

The job logs in as the Argo CD `admin` user. Store the admin password once as the
`ARGOCD_PASSWORD` repository secret:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath='{.data.password}' | base64 -d \
  | gh secret set ARGOCD_PASSWORD --repo eduardopiairo/platform-engineering
```
