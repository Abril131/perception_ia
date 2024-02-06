import pandas as pd

datos = {
   'x1': [0, 1, 0, 1],
    'x2': [0, 1, 1, 1],
    'x3': [0, 1, 0, 1],
    'y': [0, 1, 0, 1]
}

df = pd.DataFrame(datos)

nombre_archivo = 'datosss.csv'

df.to_csv(nombre_archivo, index=False)

print(f'Se ha creado el archivo CSV: {nombre_archivo}')
