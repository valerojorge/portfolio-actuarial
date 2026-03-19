import pandas as pd
df= pd.read_csv("insurance_claims.csv")
# primeras 5 filas
print(df.head())
# dimensiones
print(df.shape)
# nombres de columnas
print(df.columns)
# estadísticas básicas
print(df.describe())