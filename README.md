# Análisis de Costos y Predicciones: Equipos 1 y 2

## **Descripción del Proyecto**
Este proyecto tiene como objetivo analizar los costos de dos equipos (Equipo 1 y Equipo 2) utilizando datos históricos de diversas materias primas. Se entrenaron modelos de series de tiempo utilizando **Prophet**, y se calcularon proyecciones de costos para los próximos **36 meses** con granularidad **diaria**. Finalmente, se realizó un análisis comparativo para determinar cuál de los equipos resulta más caro en términos de tendencia futura.

---

## **Flujo General del Proceso**
El desarrollo de este análisis comprende los siguientes pasos:

### **1. Ingesta y Procesamiento de Datos**
- Se utilizaron datos históricos de las materias primas **X**, **Y** y **Z**:
  - Cada materia prima contiene información sobre los precios diarios y su respectivo proveedor.
- Los datos se almacenaron en DataFrames de PySpark, con las siguientes claves:
  - **Date:** Fecha de la observación.
  - **Price:** Precio de la materia prima en la fecha correspondiente.

#### **Equipos Construidos**
1. **Equipo 1:**
   - Composición: 20% de **X** y 80% de **Y**.
   - Fórmula utilizada:
     \[
     \text{Costo del Equipo 1} = (\text{Precio de X} \times 0.2) + (\text{Precio de Y} \times 0.8)
     \]

2. **Equipo 2:**
   - Composición: 33.3% de **X**, 33.3% de **Y**, y 33.3% de **Z**.
   - Fórmula utilizada:
     \[
     \text{Costo del Equipo 2} = (\text{Precio de X} \times 0.3333) + (\text{Precio de Y} \times 0.3333) + (\text{Precio de Z} \times 0.3333)
     \]

Todos los cálculos se realizaron sobre **uniones internas (`INNER JOIN`)**, asegurando que únicamente se consideraran fechas comunes entre las materias primas.

---

### **2. Modelado Predictivo con Prophet**
Se utilizó el modelo **Prophet** para la predicción de costos futuros. Los principales pasos realizados fueron:

1. **Preparación de los datos:**
   - Se transformaron los datos de PySpark a Pandas, y se ajustaron los nombres de las columnas para cumplir con los requisitos de Prophet:
     - `Date` -> `ds` (Fecha).
     - `Costo del Equipo` -> `y` (Variable objetivo).
  
2. **Entrenamiento del modelo:**
   - Se entrenaron modelos independientes para el **Equipo 1** y el **Equipo 2**.
   - Se utilizó la última fecha en los datos históricos como punto de inicio, y se generaron **1095 días futuros (36 meses)**.

3. **Generación de proyecciones:**
   - Prophet generó las columnas `trend`, `yhat` (predicción central), `yhat_lower` y `yhat_upper` (intervalos de confianza).

---

### **3. Evaluación del Desempeño**
Se evaluaron los modelos de ambos equipos utilizando métricas clave de regresión:

- **MAE (Mean Absolute Error):**
  - Promedio de los errores absolutos entre los valores reales y predichos.
- **RMSE (Root Mean Squared Error):**
  - Raíz cuadrada del error cuadrático medio, penalizando errores grandes.
- **MAPE (Mean Absolute Percentage Error):**
  - Error porcentual promedio relativo.

#### **Resultados de Evaluación:**
| Métrica       | Equipo 1      | Equipo 2      |
|---------------|---------------|---------------|
| **MAE**       | 101.25        | 122.88        |
| **RMSE**      | 117.86        | 154.79        |
| **MAPE**      | **23.29%**    | **14.36%**    |

- El **Equipo 1** mostró un menor error absoluto y cuadrático, pero su MAPE fue mayor, indicando que las predicciones del modelo para el Equipo 2 fueron proporcionalmente más precisas.

---

### **4. Análisis Comparativo: Tendencia del Costo**
Se realizó un análisis para identificar qué equipo será más caro en términos de la **tendencia (`trend`) proyectada** por Prophet. Los pasos fueron:
1. Se combinaron las proyecciones de ambos equipos en un único DataFrame, alineando las fechas futuras.
2. Para cada fecha futura:
   - Se compararon las tendencias (`trend`) de los costos del Equipo 1 y el Equipo 2.
   - Se determinó cuál de los dos equipos tenía el costo proyectado más alto.
3. Finalmente, se generó un resumen del número de fechas en las que cada equipo mostró ser más caro.

#### **Conclusiones del análisis:**
- Ambos equipos mostraron períodos en los que fueron más caros, dependiendo de las fluctuaciones proyectadas en los datos históricos.
- El equipo con costos más altos variaba según las fechas, debido a las diferencias en las materias primas involucradas.

---

## **Herramientas y Tecnologías Utilizadas**
1. **Lenguaje de Programación:**
   - Python (PySpark, Prophet, Pandas, NumPy, Matplotlib)
2. **Plataforma:**
   - Databricks
3. **Almacenamiento:**
   - Unity Catalog (Delta Tables)
4. **Modelado Predictivo:**
   - Prophet
5. **Métricas de Evaluación:**
   - Scikit-Learn

---

## **Futuros Pasos y Mejoras**
1. **Incorporar beneficios adicionales para análisis costo-beneficio:**
   - Identificar "beneficios" asociados (calidad, tiempos de entrega, confiabilidad del proveedor).
2. **Explorar patrones no lineales o estacionales complejos:**
   - Considerar modos multiplicativos o estacionalidades personalizadas en Prophet.
3. **Optimización con datos externos:**
   - Incluir datos como inflación, indicadores del mercado o eventos externos que puedan afectar los costos.

---

## **Autores**
- **Nombre:** Juan Pablo Guerra Osorio

---
