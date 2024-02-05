import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
def plot_error(errores_historia, norma_errores_historia):
    # Invertir el orden de la lista de norma de errores
    norma_errores_historia.reverse()

    # Graficar errores
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(norma_errores_historia, label='Norma del Error', color='tab:red')
    plt.title('Evolución de la Norma del Error')
    plt.xlabel('Iteración')
    plt.ylabel('Norma del Error')
    plt.legend()
    plt.show()
