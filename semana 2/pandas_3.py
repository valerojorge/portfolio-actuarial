import pandas as pd

# Creación de una tabla de siniestros
datos = {
    "conductor": ["joven","adulto", "senior", "joven", "adulto"],
    "zona": ["urbana", "rural", "urbana", "rural", "urbana"],
    "frecuencia": [2,0,1,1,0],
    "severidad": [3200,0,1500,2800,0]
}

df= pd.DataFrame(datos)

# Calcular prima pura para cada fila

df["prima_pura"]=df["frecuencia"] * df["severidad"]
print(df)

# Prima pura media por conductor

print("\nPrima media por conductor")
print(df.groupby("conductor")["prima_pura"].mean())