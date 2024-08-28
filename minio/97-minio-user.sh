#!/bin/bash
BASEDIR="$( cd "$( dirname "${0}" )" && pwd )"

NAMESPACE="ps-ifood"
if [ "$1" != "" ]
then
    NAMESPACE="${1}"
fi
echo "Namespace: ${1}"

kubectl create namespace "${NAMESPACE}"

export MINIO_ROOT_USER=$(kubectl get secret --namespace ${NAMESPACE} minio-service -o jsonpath="{.data.root-user}" | base64 -d)
export MINIO_ROOT_PASSWORD=$(kubectl get secret --namespace ${NAMESPACE} minio-service -o jsonpath="{.data.root-password}" | base64 -d)

echo "Minio Root User ${MINIO_ROOT_USER}"
echo "Minio Root Password ${MINIO_ROOT_PASSWORD}"
