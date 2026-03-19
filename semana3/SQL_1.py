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

# Primera consulta SQL — seleccionar todo
resultado = duckdb.query("SELECT * FROM df").df()
print(resultado)


# El `SELECT * FROM df` significa:

# SELECT  →  dame
# *       →  todas las columnas
# FROM df →  de la tabla df