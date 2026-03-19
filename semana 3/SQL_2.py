import duckdb
import pandas as pd

# Creamos nuestra tabla de siniestros
datos = {
    "conductor": ["joven", "adulto", "senior", "joven", "adulto"],
    "zona": ["urbana", "rural", "urbana", "rural", "urbana"],
    "siniestros": [2, 0, 1, 1, 0],
    "coste": [3200, 0, 1500, 2800, 0]
}

df = pd.DataFrame(datos)

# Filtrar solo conductores jóvenes
jovenes = duckdb.query("""
    SELECT *
    FROM df
    WHERE conductor = 'joven'
""").df()
print("Conductores jóvenes:")
print(jovenes)

# Filtrar costes mayores a 1000
costes_altos = duckdb.query("""
    SELECT *
    FROM df
    WHERE coste > 1000
""").df()
print("\nCostes mayores a 1000€:")
print(costes_altos)