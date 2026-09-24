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

## Deploy to the local kind cluster

```bash
kind load docker-image demo-app:0.0.1 --name <your-cluster>
kubectl apply -f k8s/
```
