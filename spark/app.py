from pyspark.sql import SparkSession
import time

spark = SparkSession.builder.appName("EasyApp").getOrCreate()

dades = [("Anna", 25), ("Pere", 40), ("Joan", 35), ("Maria", 28)]
columnes = ["Nom", "Edat"]

df = spark.createDataFrame(dades, columnes)

df.show()

df_filtrat = df.filter(df.Edat > 30)

df_filtrat.show()
time.sleep(300)

spark.stop()
