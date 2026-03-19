import pandas as pd

# Creación de una tabla de siniestros
datos = {
    "conductor": ["joven","adulto", "senior", "joven", "adulto"],
    "zona": ["urbana", "rural", "urbana", "rural", "urbana"],
    "siniestros": [2,0,1,1,0],
    "coste": [3200,0,1500,2800,0]
}

df= pd.DataFrame(datos)

# Coste medio por tipo de conductor
print("Coste medio por conductor:")
print(df.groupby("conductor")["coste"].mean())

# Siniestros totales por zona
print("\nSiniestros por zona:")
print(df.groupby("zona")["siniestros"].sum())

# Coste total por conductor

print("\nCoste total por conductor:")
print(df.groupby("conductor")["coste"].sum())