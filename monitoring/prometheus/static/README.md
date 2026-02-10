# Prometheus Static Provisioning & Configuration

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

## Create prometheus service
```
kubectl apply -f prometheus-service.yaml 
```

## Check the prometheus service
```
minikube service prometheus-service -n monitoring
```

## Deploy hey app
```
kubectl apply -f hey-deployment.yaml 
kubectl apply -f hey-service.yaml 
```

Check hey app
```
minikube service hey-service -n monitoring
```

## Update ConfigMap for adding hey app as a target
```
kubectl apply -f prometheus-configmap-update.yaml 
```