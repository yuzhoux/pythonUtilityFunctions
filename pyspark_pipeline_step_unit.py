from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, HiveContext

conf = (SparkConf().setAppName("example")
	.set("spark.yarn.queue","team_queue")
	.set("spark.dynamicAllocation.minExecutors","2")
	.set("spark.dynamicAllocation.maxExecutors","100")
	.set("spark.shuffle.service.enabled","true")
	.set("spark.executor.memory","5g")
	.set("spark.driver.memory","3g")
	.set("spark.executor.cores","3")
	.set("spark.sql.parquet.compression.codec","uncompressed")
	.set("spark.sql.hive.convertMetastoreParquet","false")
	.set("spark.akka.timeout","10000s")
	.set("spark.network.timeout","10000s")
	)

sc = SparkContext(conf = conf)
sqlContext = HiveContext(sc)

df = sqlContext.sql("""
	select statement
	""").persist()

df.schema.names


# create this hadoop table first
# create external table schema.table(col1 string, col2 string)
# row format delimited fields terminated by ','
# stored as textfile location "hdfs://location";

df.select("col1","col2").write.format("csv").mode('overwrite').save("hdfs://location")

