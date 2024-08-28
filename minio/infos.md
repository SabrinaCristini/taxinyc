Error from server (AlreadyExists): namespaces "ps-ifood" already exists
Error: uninstall: Release not loaded: minio-service: release: not found
NAME: minio-service
LAST DEPLOYED: Tue Aug 27 21:03:04 2024
NAMESPACE: ps-ifood
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: minio
CHART VERSION: 12.8.12
APP VERSION: 2023.9.30

** Please be patient while the chart is being deployed **

MinIO&reg; can be accessed via port  on the following DNS name from within your cluster:

   minio-service.ps-ifood.svc.cluster.local

To get your credentials run:

   export ROOT_USER=$(kubectl get secret --namespace ps-ifood minio-service -o jsonpath="{.data.root-user}" | base64 -d)
   export ROOT_PASSWORD=$(kubectl get secret --namespace ps-ifood minio-service -o jsonpath="{.data.root-password}" | base64 -d)

To connect to your MinIO&reg; server using a client:

- Run a MinIO&reg; Client pod and append the desired command (e.g. 'admin info'):

   kubectl run --namespace ps-ifood minio-service-client \
     --rm --tty -i --restart='Never' \
     --env MINIO_SERVER_ROOT_USER=$ROOT_USER \
     --env MINIO_SERVER_ROOT_PASSWORD=$ROOT_PASSWORD \
     --env MINIO_SERVER_HOST=minio-service \
     --image docker.io/bitnami/minio-client:2023.9.29-debian-11-r2 -- admin info minio

To access the MinIO&reg; web UI:

- Get the MinIO&reg; URL:

   echo "MinIO&reg; web URL: http://127.0.0.1:9001/minio"
   kubectl port-forward --namespace ps-ifood svc/minio-service 9001:9001