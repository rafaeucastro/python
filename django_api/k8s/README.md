Detalhar manifesto
comando: `kubectl explain deployment.metadata`

Recursos kubernetes
comando: `kubectl api-resources`
- Pods, Deployment, Service

Listar todos os pods
comando: `kubectl get pods`

Inspecionar pod
comando: `kubectl describe pod djangoapp`

Aplicar um manifesto no cluster
comando: `kubectl apply -f k8s/service.yaml`

Verificar especificação sobre campos do manifesto:
comando: `kubectl explain deployment.spec`

Expor um deployment de modo imperativo (Linha de comando), cria um service.
comando: `kubectl expose deployment mydeploy --port=8080 --target-port=80 --protocol=TCP -n dev`

Criar um namespace:
comando: `kubectl create namespace dev`

Editar um recurso em tempo de execução
comando: `kubectl edit deployment mydeploy -o yaml`

Aumentar réplicas de um deployment
comando: `kubectl scale --replicas 5 deployment mydeploy`