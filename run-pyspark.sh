#!/bin/bash

# Get current file location
BASEDIR=$(cd -P -- "$(dirname -- "${0}")" && pwd -P)
SPARK_VERSION="3.3.0"

##echo "spark:x:${SPARK_USER}:${SPARK_USER}::/home/spark:/bin/sh" > /etc/passwd

export PYSPARK_PYTHON=/usr/share/miniconda/envs/qualityEnviroment/bin/python

time spark-submit --master local \
    --conf spark.jars.ivy="${PWD}/.ivy2" \
    --deploy-mode client \
    --conf spark.task.cpus="1" \
    --conf spark.driver.memory=8g \
    --conf spark.driver.memory=8g \
    --conf spark.executor.memoryOverhead=4096 \
    --conf spark.executor.instances=4 \
    --conf "spark.executor.extraJavaOptions=-Dlog4j.configuration=${LOG4J_PROPERTIES}" \
    --conf "spark.driver.extraJavaOptions=-Dlog4j.configuration=${LOG4J_PROPERTIES}" \
    --packages org.apache.spark:spark-hadoop-cloud_2.12:${SPARK_VERSION} \
    --conf spark.hadoop.fs.s3a.endpoint="http://minio-service:9001" \
    --conf spark.hadoop.fs.s3a.access.key="5FCOJ3tSURKM65xXPnW8" \
    --conf spark.hadoop.fs.s3a.secret.key="cOMprohE5zopGpfV8pXNXpIuQQAHsQsX2bEhL4C2" \
    --conf spark.hadoop.fs.s3a.path.style.access="true" \
    --conf spark.hadoop.fs.s3a.impl="org.apache.hadoop.fs.s3a.S3AFileSystem" \
    "${BASEDIR}/takeHomeTest/read_and_writes3/solution1.py"

    
