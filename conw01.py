import pandas as pd
from tkinter import filedialog
import numpy as np

def activate_function(u):
    return 1 / (1 + np.exp(-u))

def calcular_resultado_activacion(fila, pesos_decimales):
    return np.dot(fila, pesos_decimales)

def generar_pesos_aleatorios(n, primera_iteracion):
    if primera_iteracion:
        return [1] + [round(np.random.rand(), 4) for _ in range(n - 1)]
    else:
        return [round(np.random.rand(), 4) for _ in range(n)]

def cargar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if archivo:
        df = pd.read_csv(archivo)
        xn = df.iloc[:, :-1].values.astype(float)  # Convertir a float
        print("xn=", xn)
        y_values = df.iloc[:, -1].values
        print("y=", y_values)

        return xn, y_values
    else:
        return None, None

def procesar_matriz(xn, y_values, entry_ite):
    ite = int(entry_ite.get())
    print("ite", ite)

    for iteracion in range(ite):  # Bucle para iteraciones
        print(f"Iteración {iteracion + 1}")

        numero_columnas_xn = len(xn[0])
        # Establecer w0 manualmente como 1
        pesos_decimales = [1] + generar_pesos_aleatorios(numero_columnas_xn - 1, iteracion == 0)

        for i, ww in enumerate(pesos_decimales):
            print(f"w{i} =", ww)

        for i, fila in enumerate(xn):
            # Verificar si la fila es de tamaño 3x1
            if len(fila) == 3:
                # Crear una copia de la fila antes de aplicar los pesos
                fila_copia = fila.copy()
                # Multiplicar cada elemento de la fila copia por el peso correspondiente
                fila_copia[1:] *= pesos_decimales[1:]  # Excluir el primer peso que es para ww0

            resultado_activacion = activate_function(calcular_resultado_activacion(fila_copia, pesos_decimales))
            print(f"Resultado de la activación para la fila {i + 1}:", resultado_activacion)
