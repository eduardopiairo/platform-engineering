# demo-app

`demo-app` is a small Python service built with FastAPI. It exists to demonstrate the platform-engineering pipeline: build a container, publish it, and deploy it to Kubernetes through GitOps.

| | |
| --- | --- |
| **Type** | Service |
| **Owner** | development |
| **Lifecycle** | Experimental |
| **Image** | [`edpiairo/demo-app`](https://hub.docker.com/r/edpiairo/demo-app) |
| **Port** | 8000 |

## Endpoints

| Path | Description |
| --- | --- |
| `GET /` | Hello message with the pod hostname and the `APP_VERSION` |
| `GET /healthz` | Liveness probe |
| `GET /readyz` | Readiness probe |
| `GET /info` | Hostname, start time, and all `APP_*` environment variables |

## How a change reaches the cluster

1. A push that touches `demo-app/src/`, the `Dockerfile` or `requirements.txt` triggers the [Build Demo App](https://github.com/eduardopiairo/platform-engineering/blob/main/.github/workflows/demo-app-build.yml) workflow.
2. The `ci` job builds a multi-arch image (amd64 and arm64), tags it `0.0.<run number>` and pushes it to Docker Hub.
3. The same job writes that version to `appVersion` in `charts/demo-app/Chart.yaml` and commits it back to the branch.
4. The `cd` job runs on a self-hosted runner inside the kind cluster and calls `argocd app sync demo-app`.
5. Argo CD deploys the Helm chart in `charts/demo-app` to the `demo` namespace.

## Run it locally

```bash
cd demo-app
docker build -t demo-app:dev .
docker run -p 8000:8000 demo-app:dev
curl http://localhost:8000/
```

## Repository layout

| Path | Contents |
| --- | --- |
| `src/app.py` | Application code |
| `charts/demo-app/` | Helm chart that Argo CD deploys |
| `charts/argocd/` | Argo CD install values and the `Application` manifest |
| `k8s/` | Plain Kubernetes manifests for a manual deploy |
| `self-hosted-runner/` | Actions Runner Controller setup for the `cd` job |

For full setup steps, including creating the kind cluster, installing Argo CD and configuring secrets, see the [README](https://github.com/eduardopiairo/platform-engineering/blob/main/demo-app/README.md).
