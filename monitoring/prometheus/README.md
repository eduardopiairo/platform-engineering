# Prometheus

## Create namespace
```
kubectl apply -f prometheus-namespace.yaml 
```

## Create Config Map
```
kubectl apply -f prometheus-configmap.yaml 
```

## Deploy prometehus server
```
kubectl apply -f prometheus-deployment.yaml 
```
