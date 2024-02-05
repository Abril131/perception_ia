import pandas as pd
import numpy as np
from tkinter import filedialog

def activate_function(u):
    return 1 / (1 + np.exp(-u))

def calcular_resultado_activacion(fila, pesos_decimales):
    return np.dot(fila, pesos_decimales)



def update_weights(w, pesos_matriz):
    w = np.array(w)
    pesos_matriz = np.array(pesos_matriz)

    w += pesos_matriz
    return w

def generar_pesos_w(n):
    w_values = [1] + [round(val, 4) for val in np.random.rand(n - 1).tolist()]
    return w_values

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

def procesar_matriz(xn, y_values, entry_ite, entry_eta):
    ite = int(entry_ite.get())
    eta = float(entry_eta.get())

    errores_historia = []  # Lista para almacenar los errores en cada iteración
    norma_errores_historia = []  # Lista para almacenar la norma del error en cada iteración
    pesos_historia = []  # Lista para almacenar los pesos en cada iteración

    numero_columnas_xn = len(xn[0])
    w = np.array([generar_pesos_w(numero_columnas_xn)])

    for iteracion in range(ite):  # Bucle para iteraciones
        print(f"Iteración {iteracion + 1}")

        w_iteracion = []  # Lista para almacenar los valores de w en esta iteración

        for i, fila in enumerate(xn):
            # Se elimina la línea que ajusta los valores de fila_copia
            fila_copia = fila.copy()

            u = calcular_resultado_activacion(fila_copia, w.flatten())
            print("u=", u)

            resultado_activacion = activate_function(u)

            print(f"Resultado para la fila {i + 1}: {resultado_activacion}")

            # Calcular el error
            error = y_values[i] - resultado_activacion
            print(f"Error para la fila {i + 1}: {error}")

            # Actualizar los pesos
            pesos_matriz = eta * error * fila_copia.reshape((1, -1))
            print("AX:", pesos_matriz)
            w = update_weights(w, pesos_matriz)
            print("w=", w)

            w_iteracion.append(w.flatten().tolist())  # Agregar los valores de w en esta iteración a la lista

        # Calcular la norma del error y agregarla a la lista
        norma_error_iteracion = np.linalg.norm(errores_historia)
        norma_errores_historia.append(norma_error_iteracion)
        print("norma error:", norma_error_iteracion)
        print("norma error2:", norma_errores_historia)

        errores_historia.append(error)  # Agregar el total de errores a la lista
        pesos_historia.append(w_iteracion)  # Agregar la lista de w de esta iteración a la lista principal

    # Guardar todos los datos de w en un solo archivo CSV
    df_w = pd.DataFrame(np.concatenate(pesos_historia))
    nombre_archivo = 'w.csv'
    df_w.to_csv(nombre_archivo, index=False)

    return errores_historia, norma_errores_historia, pesos_historia

