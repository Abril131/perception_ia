import tkinter as tk
from arc import cargar_archivo, procesar_matriz
from grafica import plot_and_save
from grafica_error import plot_error

def cargar_csv():
    xn, y_values, = cargar_archivo()
    errores, norma_errores, pesos = procesar_matriz(xn, y_values, entry_ite, entry_eta)
    plot_and_save(pesos)
    plot_error(errores, norma_errores)


w = tk.Tk()
w.configure(background="alice blue")
w.title("Neu")

eta = tk.Label(w, text="ETA")
eta.grid(row=1, column=0, padx=10, pady=10)
entry_eta = tk.Entry(w)
entry_eta.grid(row=1, column=1, padx=10, pady=10)

ite = tk.Label(w, text="Iteraciones")
ite.grid(row=2, column=0, padx=10, pady=10)
entry_ite = tk.Entry(w)
entry_ite.grid(row=2, column=1, padx=10, pady=10)

# Botón para cargar el archivo CSV
boton_cargar_csv = tk.Button(w, text="Cargar CSV", command=cargar_csv)
boton_cargar_csv.grid(row=2, column=2, padx=10, pady=10)

w.mainloop()

