from pyspark.sql import SparkSession

spark = SparkSession.builder\
        .master("local[4]")\
        .appName("Colab_pyspark")\
        .config('spark.ui.port', '4050')\
        .getOrCreate()