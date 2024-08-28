from pyspark.sql import *

##Creating spark session
spark = SparkSession.builder \
            .appName("ifood_2") \
            .getOrCreate()

##Reading file from s3a(minio)
read_files_taxi_silver = spark.read \
    .format("parquet") \
    .load("s3a://ifood-processo-seletivo/silver/*.parquet")

##parquets temp view 
read_files_taxi_silver.createOrReplaceTempView("temp")

'''
Qual a média de passageiros (passenger_count) por
hora e por dia considerando todos os yellow taxis da
frota.
'''

##wuery to hour
query_hour = '''
SELECT
    HOUR(tpep_pickup_datetime) AS hour,
    AVG(passenger_count) AS average_passenger_count
FROM
    temp
GROUP BY
    HOUR(tpep_pickup_datetime)
ORDER BY
    hour;
'''

result_hour = spark.sql(query_hour)
##result
print("passageiro por hora:")
result_hour.show()

##query to day
query_day = '''
SELECT
    DAYOFMONTH(tpep_pickup_datetime) AS day,
    DAYOFWEEK(tpep_pickup_datetime) AS day_of_week,
    AVG(passenger_count) AS average_passenger_count
FROM
    temp
GROUP BY
    DAYOFMONTH(tpep_pickup_datetime),
    DAYOFWEEK(tpep_pickup_datetime)
ORDER BY
    day, day_of_week;
'''

result_day = spark.sql(query_day)
print("passageiro por dia:")
##result 
result_day.show()

'''
Question:
Qual a média de valor total (total_amount) recebido
em um mês considerando todos os yellow taxis da
frota.
'''

amount_query = '''
SELECT
    YEAR(tpep_pickup_datetime) AS year,
    MONTH(tpep_pickup_datetime) AS month,
    AVG(total_amount) AS average_total_amount
FROM
    temp
GROUP BY
    YEAR(tpep_pickup_datetime),
    MONTH(tpep_pickup_datetime)
ORDER BY
    year, month;
'''


result_amount = spark.sql(amount_query)
print("média do valor total em meses:")
##result
result_amount.show()




