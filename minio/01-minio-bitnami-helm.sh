#!/bin/bash
BASEDIR="$( cd "$( dirname "${0}" )" && pwd )"

NAMESPACE="ps-ifood"
if [ "$1" != "" ]
then
    NAMESPACE="${1}"
fi
echo "Namespace: ${1}"

kubectl create namespace "${NAMESPACE}"

#helm repo add bitnami https://charts.bitnami.com/bitnami
#helm repo update

helm -n "${NAMESPACE}" uninstall minio-service
#helm -n "${NAMESPACE}" install minio-service oci://registry-1.docker.io/bitnamicharts/minio
helm install minio-service bitnami/minio --version "12.8.12" --namespace ${NAMESPACE} # --values ${BASEDIR}/minio.yaml