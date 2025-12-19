"""
Funciones para el tratamiento de los datos
Caso de Negocio: Estimacion de Costos de Equipos Proyecto de Construccion
"""
from databricks.sdk.runtime import *
import pyspark as ps
import pyspark.sql.functions as F
from pyspark.sql import Row, DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, DateType
from pyspark.sql.window import Window
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import sklearn as sk

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
def save_table_unity(df, table_name, catalogo = "dataknow_dll", schema = "construccion"):
    """
    Funcion para guardar un dataframe en la unidad de almacenamiento de Databricks
    """
    tabla_destino = f"{catalogo}.{schema}.{table_name}"
    df.write \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable(tabla_destino)