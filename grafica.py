import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def plot_and_save( pesos_historia):
    num_pesos = len(pesos_historia[0][0])
    num_iteraciones = len(pesos_historia)

    # Crear listas separadas para cada peso
    pesos_separados = [[] for _ in range(num_pesos)]

    for iteracion in range(num_iteraciones):
        for i in range(num_pesos):
            peso_i = pesos_historia[iteracion][i][0]
            pesos_separados[i].append(peso_i)

    # Graficar cada peso por separado
    plt.figure(figsize=(15, 5))

    for i in range(num_pesos):
        plt.plot(pesos_separados[i], label=f'Peso {i + 1}')

    plt.title('Evolución de Pesos')
    plt.xlabel('Iteración')
    plt.ylabel('Peso')
    plt.legend()
    plt.show()
