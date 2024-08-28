#!/bin/bash
BASEDIR="$( cd "$( dirname "${0}" )" && pwd )"

NAMESPACE="ps-ifood"

if [ "$1" != "" ]
then
    NAMESPACE="${1}"
fi
echo "Namespace: ${1}"

kubectl create namespace "${NAMESPACE}"

helm repo add bigdata-gradiant https://gradiant.github.io/bigdata-charts/

helm install hivems bigdata-gradiant/hive-metastore -n ${NAMESPACE}

kubectl -n ${NAMESPACE} get configmap hivems-hive-metastore -o yaml  > hivems-hive-metastore.yaml