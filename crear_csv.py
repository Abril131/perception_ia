import pandas as pd

datos = {
   'x0': [1, 1, 1, 1, 0],
    'x1': [0, 0, 1, 1, 1],
    'x2': [0, 1, 0, 1, 0],
    'y': [0, 0, 0, 1, 0]
}

df = pd.DataFrame(datos)

nombre_archivo = 'datos.csv'

df.to_csv(nombre_archivo, index=False)

print(f'Se ha creado el archivo CSV: {nombre_archivo}')
