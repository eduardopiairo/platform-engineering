# Local Octopus Deploy on Kubernetes (kind)

Steps to stand up a local Octopus Deploy instance in a dedicated `kind` cluster.

## 0. Prerequisites

Already installed on this machine: `docker`, `kubectl`, `helm`, `kind`.

Make sure Docker Desktop is running first:

```bash
open -a Docker
# wait until this succeeds:
docker info
```

License key: the base64 license blob lives in `octopus-deploy/license.b64`
(gitignored — never commit it). If that file is missing, paste your license
XML's base64 form into it before continuing.

## 1. Create a dedicated kind cluster

```bash
kind create cluster --name octopus
kubectl config use-context kind-octopus
kubectl get nodes
```

kind ships with the `rancher.io/local-path` storage provisioner and a default
`standard` StorageClass, so no extra storage setup is needed. Confirm it:

```bash
kubectl get storageclass
```

You should see a `standard` StorageClass marked `(default)`.

## 2. Install Octopus Deploy via Helm

```bash
helm upgrade my-octopus-instance oci://ghcr.io/octopusdeploy/octopusdeploy-helm --install --namespace octopus-deploy --create-namespace --set octopus.acceptEula="Y" --atomic \
  --set mssql.enabled="true" \
  --set-file octopus.licenseKeyBase64=./octopus-deploy/license.b64 \
  --set global.storageClass="standard"
```

This deploys Octopus Server plus an in-cluster MSSQL database
(`mssql.enabled=true`) into the `octopus-deploy` namespace. `--atomic` rolls
back automatically if the install fails, so give it a few minutes — the
first install pulls images and waits for MSSQL to become ready.

`--set-file` reads the license value straight from the local `license.b64`
file, so the real key never appears in this doc, your shell history file
(if you avoid retyping it), or anywhere meant to be shared.

## 3. Watch it come up

```bash
kubectl get pods -n octopus-deploy -w
```

Wait until the Octopus server pod and the mssql pod are `Running`/`Ready`.

## 4. Access the web UI

Find the service Helm created:

```bash
kubectl get svc -n octopus-deploy
```

Octopus's chart exposes the web UI on port `80` via a `NodePort` service by
default. Port-forward it to your laptop:

```bash
kubectl port-forward -n octopus-deploy svc/my-octopus-instance-octopusdeploy 8080:80
```

(Adjust the service name to whatever `kubectl get svc` showed.) Then open:

```
http://localhost:8080
```

## 5. First-time setup

The first time you load the UI, Octopus walks you through creating an admin
user and initial space — no extra CLI steps needed.

## Tear down

```bash
helm uninstall my-octopus-instance -n octopus-deploy
kind delete cluster --name octopus
```
