# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
datasets=[
    {
        "file_name":"orders"
    },
    {
        "file_name":"customers"
    },
    {
        "file_name":"products"
    }
]

# COMMAND ----------


dbutils.jobs.taskValues.set("output_datasets",datasets)