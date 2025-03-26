# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "b5fab3bf-ae88-4bcf-816e-a65cad7ccb13",
# META       "default_lakehouse_name": "LH_Meine_Daten",
# META       "default_lakehouse_workspace_id": "c46e5216-31ef-4136-97bd-0206be8da638",
# META       "known_lakehouses": [
# META         {
# META           "id": "b5fab3bf-ae88-4bcf-816e-a65cad7ccb13"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.sql("SELECT * FROM LH_Meine_Daten.two LIMIT 1000")
# display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.printSchema()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import col

df = df.withColumnRenamed("English_-_US", "English") \
       .withColumnRenamed("German_-_DE", "German") \
       .withColumnRenamed("Corrections", "Corrections") \
       .withColumnRenamed("Column4", "Other")

df.printSchema()


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import current_date

# Neue Spalte "datum" mit aktuellem Datum hinzufügen
df = df.withColumn("datum", current_date())

display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

delta_table_path = "Tables/two" #fill in your delta table path 
# data = spark.range(5,10) 
df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(delta_table_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
