#!/bin/bash
BASEDIR="$( cd "$( dirname "${0}" )" && pwd )"

NAMESPACE="ps-ifood"
if [ "$1" != "" ]
then
    NAMESPACE="${1}"
fi
echo "Namespace: ${1}"

kubectl --namespace "${NAMESPACE}"  port-forward svc/minio-service 9001:9001 9000:9000 --address=0.0.0.0