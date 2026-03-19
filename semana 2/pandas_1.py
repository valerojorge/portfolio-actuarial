import pandas as pd

# Creación de una tabla de siniestros
datos = {
    "conductor": ["joven","adulto", "senior", "joven", "adulto"],
    "zona": ["urbana", "rural", "urbana", "rural", "urbana"],
    "siniestros": [2,0,1,1,0],
    "coste": [3200,0,1500,2800,0]
}

df= pd.DataFrame(datos)
print(df)

# ¿Cuántas filas y columnas tiene la tabla?
print(df.shape)

# Resumen estadístico
print(df.describe())

# Ver solo la columna de costes
print(df["coste"])

# Filtrar solo conductores jóvenes
jovenes=df[df["conductor"]=="joven"]
print(jovenes)

