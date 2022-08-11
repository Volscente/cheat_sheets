---
title: "PySpark"
tags: "Cheat Sheet"
---

# Read CSV
[StackOverflow Thread](https://stackoverflow.com/questions/40413526/reading-csv-files-with-quoted-fields-containing-embedded-commas)

```python
spark_dataframe = spark.read.option("delimiter", ";") \
    .option("header", True)\
    .option("inferschema", "true")\
    .option("encoding", "UTF-8")\
    .option("quote", "\"")\
    .option("escape", "\"")\
    .option("dateFormat" , "yyyy.MM.dd HH:mm:ss")\
    .option("multiline", 'true')\
    .option("quotestr", '"')\
    .csv(file_path)
```

# Filter with Group By
[StackOverflow Thread](https://stackoverflow.com/questions/48829993/groupby-column-and-filter-rows-with-maximum-value-in-pyspark)
```python
import pyspark.sql.functions as f

# Create a Window partition over the column that you desire to group by column
window = Window.partitionBy('grouping_column')

# Keep only the row with the minimum value in the column to filter among all the same group
df = df.withColumn('min_filtering_column', f.min('filtering_column').over(window))\
.where(col('filtering_column') == col('min_filtering_column'))\
.drop('min_filtering_column')
```
