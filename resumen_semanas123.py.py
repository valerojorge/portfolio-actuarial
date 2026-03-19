import pandas as pd
import duckdb

datos = {
    "conductor": ["joven", "adulto", "senior", "joven", "adulto"],
    "zona": ["urbana", "rural", "urbana", "rural", "urbana"],
    "frecuencia": [0.12, 0.05, 0.07, 0.12, 0.05],
    "severidad": [3000, 2000, 1500, 3000, 2000],
    "coste": [3200, 0, 1500, 2800, 0]
}

df = pd.DataFrame(datos)

# Prima pura con Pandas
df["prima_pura"] = df["frecuencia"] * df["severidad"]
print("Tabla completa con prima pura:")
print(df)

# Análisis con SQL
print("\nPrima media y coste medio por conductor:")
print(duckdb.query("""
    SELECT conductor,
           AVG(prima_pura) AS prima_media,
           AVG(coste)      AS coste_medio,
           COUNT(*)        AS registros
    FROM df
    GROUP BY conductor
    ORDER BY prima_media DESC
""").df())