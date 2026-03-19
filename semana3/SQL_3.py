import duckdb
import pandas as pd

datos = {
    "conductor": ["joven", "adulto", "senior", "joven", "adulto"],
    "zona": ["urbana", "rural", "urbana", "rural", "urbana"],
    "siniestros": [2, 0, 1, 1, 0],
    "coste": [3200, 0, 1500, 2800, 0]
}

df = pd.DataFrame(datos)

# Coste medio por conductor
resultado = duckdb.query("""
    SELECT conductor,
           AVG(coste) AS coste_medio,
           SUM(siniestros) AS total_siniestros,
           COUNT(*) AS num_registros
    FROM df
    GROUP BY conductor
""").df()

print(resultado)




