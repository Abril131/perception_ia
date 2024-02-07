import numpy as np
import pandas as pd
from tkinter import filedialog
import matplotlib.pyplot as plt

class Epoch:
    def __init__(self, id,norma, weights):
        self.id = id
        self.norma = norma
        self.weights = weights

    def __str__(self):
        return f"Epoch: {self.id},Norma: {self.norma} Weights: {self.weights}"

def calcular_resultado_activacion(fila_copia, pesos_decimales):
    return np.dot(fila_copia, pesos_decimales)

def generar_pesos_w(w):
    #w_values = [1] + [round(val, 4) for val in np.random.uniform(-1, 1, w-1).tolist()]
    w_values = [round(val, 4) for val in np.random.uniform(-1, 1, w)]
    return w_values

def generar_w(w):
    w_values = [1] + [round(val, 4) for val in np.random.uniform(-1, 1, w-1).tolist()]
    #w_values = [round(val, 4) for val in np.random.uniform(-1, 1, w)]
    return w_values

def calcu_delta(eta,norma_e_y, fila_copia):
    return eta * np.dot(norma_e_y, fila_copia)

def cargar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if archivo:
        df = pd.read_csv(archivo)
        xn = df.iloc[:, :-1].values
        print("xn:", xn)
        y_values = df.iloc[:, -1].values
        print("y:", y_values)
        return xn, y_values
    else:
        raise ValueError("No se seleccionó ningún archivo CSV.")

def activate_function(u):
   # return 1 / (1 + np.exp(-u))
    if isinstance(u, (int, float, np.float64)):
       return 1 if u >= 0 else 0
    elif isinstance(u, np.ndarray):
        return np.array([1 if val >= 0 else 0 for val in u])
    else:
        raise ValueError("Unsupported data type in activate_function")


def procesar_matriz(xn, y_values, ite, entry_eta):
    epochs_historia = []
    epochs_norma = []
    b = 1
    # Lista para almacenar la norma del error en cada iteración

    for iteracion in range(ite):  # Bucle para iteraciones
        print(f"----------Iteración {iteracion + 1}")

        norma_errores_historia = []

        # Lista para almacenar la norma del error en cada iteración
        suma_u = 0
        er_e= 0

        for i, fila in enumerate(xn):
            numero_columnas_xn = len(xn[0])
            w = np.array([generar_pesos_w(numero_columnas_xn)])
            W = np.array([generar_w(numero_columnas_xn)])

            fila_copia = fila.copy()
            print("filaco", fila_copia)

            u = calcular_resultado_activacion(fila_copia, w.flatten()) + b
            print("wn", w.flatten())
            print("u=", u)
            print("w", w.flatten(), "*", "x", fila, "=", u)

            suma_u += u
            # Calcular el error
            error = y_values[i] - activate_function(u)
            print(f"Error", error)



            norma_e_y = np.linalg.norm(error)
            print("errorno", norma_e_y)
            er_e += norma_e_y
            norma_errores_historia.append(norma_e_y)
            delta = calcu_delta(entry_eta, norma_e_y, fila_copia)
            print("Delta:", delta)

            if len(delta) > 0 and len(w[1:]) > 0:
                W[1:] = w[1:] + delta[1:]
            print("WW", W)

        # Almacena la norma del error para esta iteración
        #epochs_norma.append(norma_errores_historia)

        epoch = Epoch(id=iteracion + 1, norma=norma_errores_historia[-1], weights=W.flatten().tolist())
        epochs_historia.append(epoch)

        #print("nerr", epochs_norma)
        #print(epoch)

    return epochs_historia