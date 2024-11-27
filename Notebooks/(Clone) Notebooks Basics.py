# Databricks notebook source
print("hello world!")

# COMMAND ----------

# MAGIC %sql
# MAGIC select 'mySQL' as col1

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'
# MAGIC

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.ls("/databricks-datasets/travel_recommendations_realtime/")

# COMMAND ----------


