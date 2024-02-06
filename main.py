import tkinter as tk
from arc import cargar_archivo, procesar_matriz, calcu_delta
from grafica_error import plot_error, plot_weights, save_csv

# Declarar las variables entry_eta y entry_ite como globales
entry_eta = None
entry_ite = None

def cargar_csv():
    global entry_eta, entry_ite  # Hacer referencia a las variables globales

    # Obtener los valores de ETA e Iteraciones desde las entradas de texto
    eta_value = float(entry_eta.get())
    ite_value = int(entry_ite.get())

    xn, y_values = cargar_archivo()
    epochs_historia = procesar_matriz(xn, y_values, ite_value, eta_value)
    plot_error(epochs_historia, ite_value)
    plot_weights(epochs_historia, ite_value)
    save_csv(epochs_historia, ite_value)

# Crear la ventana principal
w = tk.Tk()
w.configure(background="alice blue")
w.title("Neu")

# Etiqueta y entrada para ETA
eta_label = tk.Label(w, text="ETA")
eta_label.grid(row=1, column=0, padx=10, pady=10)
entry_eta = tk.Entry(w)
entry_eta.grid(row=1, column=1, padx=10, pady=10)

# Etiqueta y entrada para Iteraciones
ite_label = tk.Label(w, text="Iteraciones")
ite_label.grid(row=2, column=0, padx=10, pady=10)
entry_ite = tk.Entry(w)
entry_ite.grid(row=2, column=1, padx=10, pady=10)

# Botón para cargar el archivo CSV
boton_cargar_csv = tk.Button(w, text="Cargar CSV", command=cargar_csv)
boton_cargar_csv.grid(row=2, column=2, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
w.mainloop()

