"""
Funciones para el tratamiento de los datos
Caso de Negocio: Estimacion de Costos de Equipos Proyecto de Construccion
"""
from databricks.sdk.runtime import *
import pyspark as ps
import pyspark.sql.functions as F
from pyspark.sql import Row, DataFrame
import pandas as pd
import numpy as np
import sklearn as sk