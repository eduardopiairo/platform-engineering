# Self-hosted GitHub Actions runners

Runs the GitHub Actions runners for this repository inside the local `demo-cluster`
(kind), using [actions-runner-controller](https://github.com/actions/actions-runner-controller)
(ARC) installed with Helm. The `demo-app-build` workflow targets these runners via
`runs-on: self-hosted`.

## 0. Prerequisites

- `docker`, `kind`, `kubectl` and `helm` installed
- The `demo-cluster` kind cluster running (see [demo-app/README.md](../README.md))
- A GitHub Personal Access Token (classic) with the `repo` scope, so the controller
  can register runners on `eduardopiairo/platform-engineering`

```bash
kubectl config use-context kind-demo-cluster
```

## 1. Install cert-manager

ARC's admission webhooks need cert-manager.

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.8.2/cert-manager.yaml

kubectl get pods -n cert-manager
```

## 2. Install the actions-runner-controller

```bash
helm repo add actions-runner-controller https://actions-runner-controller.github.io/actions-runner-controller
helm repo update

# Keep the token out of files committed to the repo
export GITHUB_TOKEN=<your-personal-access-token>

helm upgrade --install actions-runner-controller \
  actions-runner-controller/actions-runner-controller \
  --namespace actions-runner-system \
  --create-namespace \
  --set authSecret.create=true \
  --set authSecret.github_token="$GITHUB_TOKEN" \
  --wait

kubectl get pods -n actions-runner-system
```

## 3. Deploy the runners

[runnerdeployment.yaml](../runnerdeployment.yaml) defines a `RunnerDeployment` with one
runner registered against `eduardopiairo/platform-engineering`.

```bash
kubectl apply -f demo-app/runnerdeployment.yaml
```

## 4. Verify

```bash
kubectl get runnerdeployments,runners
kubectl get pods
```

The runner should also appear as **Idle** under
**GitHub → repository Settings → Actions → Runners**. To use more runners, raise
`spec.replicas` in `runnerdeployment.yaml` and re-apply it.

## 5. Clean up

```bash
kubectl delete -f demo-app/runnerdeployment.yaml
helm uninstall actions-runner-controller -n actions-runner-system
helm uninstall cert-manager -n cert-manager
```
