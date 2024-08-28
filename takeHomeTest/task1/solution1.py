import pandas as pd
from pyspark.sql import *
from pyhive import  hive

##Creating spark session with hive enabled
spark = SparkSession.builder \
            .appName("ifood_1") \
            .config("hive.metastore.uris", "thrift://service-sab-hive-metastore:31457") \
            .master('local[*]') \
            .config('spark.jars.ivy', "/app/.ivy2") \
            .config("spark.driver.maxResultSize", "50g") \
            .config("spark.hadoop.fs.s3a.endpoint", "http://minio-service:9001") \
            .config("spark.hadoop.fs.s3a.access.key", "5FCOJ3tSURKM65xXPnW8") \
            .config("spark.hadoop.fs.s3a.secret.key", "cOMprohE5zopGpfV8pXNXpIuQQAHsQsX2bEhL4C2") \
            .config("spark.hadoop.fs.s3a.path.style.access", "true") \
            .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
            .enableHiveSupport() \
            .getOrCreate()

##Reading file from s3a(minio)
read_files_taxi = spark.read \
    .format("parquet") \
    .load("s3a://ifood-processo-seletivo/files_taxi/*.parquet")


##Filtered files
selected_columns_taxi = read_files_taxi.select(
    "VendorID",
    "passenger_count",
    "total_amount",
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
)

selected_columns_taxi.show()

path_to_save = "s3a://ifod-processo-seletivo/silver/"

##write files on s3a
selected_columns_taxi = spark.write \
    .format("parquet") \
    .mode("append") \
    .save(path_to_save)

Database = "ifoodDatabase"
hive_activated = "unabled"
##connection_hive = "pandas"
connection_hive = "pyspark"

if hive_activated == "enabled":
   
   ##example if we are using hive in pyspark
   if connection_hive == "pyspark":
    
     ##path on external table using s3a(minio)
    create_table_query = '''
    CREATE EXTERNAL TABLE IF NOT EXISTS {Database}.taxiIfood (
        VendorID BIGINT,
        tpep_pickup_datetime TIMESTAMP,
        tpep_dropoff_datetime TIMESTAMP,
        passenger_count DOUBLE,
        total_amount DOUBLE
    )
    STORED AS PARQUET
    LOCATION 's3a://ifood-processo-seletivo/silver/'
    '''

    spark.sql(f'USE {Database}') ##double check
    spark.sql(create_table_query) 
    print("Created table")
        




























 





