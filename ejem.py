import numpy as np


def update_weights(w, dw):
  """
  Actualiza los pesos de una red neuronal.

  Parámetros:
    w: Un array que contiene los pesos actuales de la red neuronal.
    dw: Un array que contiene los cambios que se aplicarán a los pesos.

  Devuelve:
    Los pesos actualizados de la red neuronal.
  """

  # Convertir las variables a NumPy arrays.
  w = np.array(w)
  dw = np.array(dw)

  # Actualizar los pesos.
  w += dw

  return w

# Ejemplo de uso
w = np.array([0.1, 0.2, 0.3])
dw = np.array([0.01, 0.02, 0.03])

w = update_weights(w, dw)

print(w)



