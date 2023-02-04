import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Función para cargar archivo
def cargar_archivo():
    archivo = input("Ingresa el nombre del archivo (incluyendo la extensión): ")
    try:
        data = pd.read_csv(archivo)
        return data
    except:
        print("Error al cargar el archivo. Asegúrate de que el nombre y extensión sean correctos.")
        return None

# Función para calcular regresión lineal
def calcular_regresion(data):
    x = data[['x']]
    y = data[['y']]
    model = LinearRegression().fit(x, y)
    a = model.intercept_
    b = model.coef_
    print("La ecuación de la recta de regresión es: y = {0} + {1}x".format(a[0], b[0][0]))
    print("La pendiente (b) es:", b[0][0])
    print("El punto de intercepción (a) es:", a[0])
    print("La precisión del modelo es:", model.score(x, y))

# Programa principal
data = cargar_archivo()
if data is not None:
    calcular_regresion(data)
else:
    print("No se pudo realizar el cálculo de regresión.")