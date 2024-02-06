import pandas as pd
from matplotlib import pyplot as plt

def plot_error(epochs_historia, ite):
    plt.figure(figsize=(10, 5))
    plt.plot([epoch.id for epoch in epochs_historia], [epoch.norma for epoch in epochs_historia],
             label='Norma del Error', color='tab:red')
    plt.title('Evolución de la Norma del Error')
    plt.xlabel('Iteración')
    plt.ylabel('Norma del Error')
    plt.legend()

    # Guardar la gráfica en un archivo
    plt.savefig(f'grafica_error_norma_{ite}.png')

def plot_weights(epochs_historia, ite):
    plt.figure(figsize=(10, 5))
    for i in range(len(epochs_historia[0].weights)):
        plt.plot([epoch.id for epoch in epochs_historia], [epoch.weights[i] for epoch in epochs_historia],
                 label=f'W {i + 1}')
    plt.title('Pesos')
    plt.xlabel('Iteración')
    plt.ylabel('Valor del Peso')
    plt.legend()


    plt.savefig(f'grafica_pesos_{ite}.png')
def save_csv(epochs_historia, ite):
    # Guardar la información en archivos CSV
    df_error_norma = pd.DataFrame({'Iteracion': [epoch.id for epoch in epochs_historia],
                                   'Error_Norma': [epoch.norma for epoch in epochs_historia]})
    df_weights = pd.DataFrame({'Iteracion': [epoch.id for epoch in epochs_historia],
                               'Weights': [epoch.weights for epoch in epochs_historia]})
    df_error_norma.to_csv(f'error_norma_{ite}.csv', index=False)
    df_weights.to_csv(f'weights_{ite}.csv', index=False)
