import pandas as pd
df= pd.read_csv("insurance_claims.csv")
# 1. ¿Cuántos registros tiene el dataset?
print("Total registros:", df.shape[0])

# 2. ¿Cuáles son todas las columnas disponibles?
print("\nColumnas:", df.columns.tolist())

# 3. Estadísticas básicas de todas las columnas numéricas
print("\nEstadísticas:")
print(df.describe())

# 4. ¿Cuántos valores vacíos hay en cada columna?
print("\nValores vacíos:")
print(df.isnull().sum())