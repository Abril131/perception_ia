import numpy as np

def generar_pesos_w(n):
    w_values = [round(val, 4) for val in np.random.uniform(-1, 1, n)]
    return w_values

# Ejemplo de uso con n=5
n = 5
pesos = generar_pesos_w(n)
print(pesos)
