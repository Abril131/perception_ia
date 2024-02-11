from tkinter import filedialog

import numpy as np
import pandas as pd


class Epoch:
    def __init__(self, id, norma, weights, allweights):
        self.id = id
        self.norma = norma
        self.weights = weights
        self.allweights = allweights

    def __str__(self):
        return f"Epoch: {self.id}, Norma: {self.norma} Weights: {self.weights[1:]}, AllWeights: {self.allweights}"


def calcular_u(filas, pesos_decimales):
    print("filas:", filas)
    print("pesos_decimales:", pesos_decimales)
    return np.linalg.multi_dot([filas[:, 1:], np.transpose(pesos_decimales[1:])]) + pesos_decimales[0]


def generar_pesos_w(w):
    w_values = [round(val, 4) for val in np.random.uniform(0, 1, w)]
    return w_values


def update_weights(w, delta_x):
    return np.round(np.add(w, delta_x), 4)


def calcu_delta(eta, error, fila_copia):
    return eta * np.dot(np.transpose(error), fila_copia)


def cargar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if archivo:
        df = pd.read_csv(archivo, header=None, delimiter=';')
        xn = df.iloc[:, :-1]
        print("xn:", xn)
        y_values = df.iloc[:, -1]
        print("y:", y_values)
        return xn, y_values
    else:
        print("No se seleccionó ningún archivo CSV.")
        return None, None


def activate_function(u):
    if isinstance(u, (int, float, np.float64)):
        return 1 if u >= 0 else 0
    elif isinstance(u, np.ndarray):
        return np.array([1 if val >= 0 else 0 for val in u])
    else:
        raise ValueError("Unsupported data type in activate_function")


def add_bias(xn):
    return np.insert(xn, 0, 1, axis=1)


def procesar_matriz(xn, y_values, ite_value, eta_value, tol_value):
    epochs_historia = []
    xn = add_bias(xn)
    b = xn[0]
    numero_columnas_xn = len(xn[0])

    w = np.array(generar_pesos_w(numero_columnas_xn))
    for iteracion in range(ite_value):
        print(f"----------Iteración {iteracion + 1}")
        norma_errores_historia = []
        u = calcular_u(xn, w)
        error = np.array(y_values - activate_function(u))
        norma_error = np.linalg.norm(error)
        norma_errores_historia.append(norma_error)
        if norma_error > tol_value:
            delta = calcu_delta(eta_value, error, xn)
            w = update_weights(w, delta)
        epoch = Epoch(id=iteracion + 1, norma=norma_errores_historia[-1] if norma_errores_historia else 0,
                      weights=w.flatten().tolist(), allweights=w.flatten().tolist())
        epochs_historia.append(epoch)

    return epochs_historia