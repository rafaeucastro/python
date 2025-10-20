Namespace: Isola recursos dentro do cluster, permitindo múltiplos ambientes ou equipes compartilhando o mesmo cluster.
Pod: A menor unidade implantável do Kubernetes, que agrupa um ou mais containers compartilhando rede e armazenamento.
Deployment: Gerencia a criação e atualização de réplicas de pods, garantindo disponibilidade e controle de versões.
Service: expõe um pod ou deployment para o cluster ou Nó
- ClusterIP
- NodePort
ConfigMap: Armazena dados de configuração em pares chave-valor para serem consumidos pelos pods.
Secret: Semelhante ao ConfigMap, mas usado para armazenar dados sensíveis, como senhas e tokens.

#### Comandos
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

Verificar o log de um pod
comando: `kubectl logs -f podname`

Criar uma secret genérica para o mysql
comando: `kubectl create secret generic mysecret --from-literal MYSQL_ROOT_PASSWORD=admin`

Executar interativamente um pod
comando: `kubectl exec -it podname -- bash`

Criar um ConfigMap:
comando: `kubectl create configmap myindex --from-file index.html`

