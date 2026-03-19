import duckdb
import pandas as pd

# Cargamos un dataset real (el de la semana 2 "insurance claims")
df=pd.read_csv("insurance_claims.csv")

# Consulta 1 — primeras 5 filas
print(duckdb.query("SELECT * FROM df LIMIT 5").df())

# Consulta 2 — columnas que más nos interesan (limite de 10 filas)
print(duckdb.query("""
    SELECT policy_number,
           total_claim_amount,
           fraud_reported
    FROM df
    LIMIT 10
""").df())

# Consulta 3 — media de reclamaciones por tipo de fraude
print(duckdb.query("""
    SELECT fraud_reported,
           AVG(total_claim_amount) AS reclamacion_media,
           COUNT(*) AS total
    FROM df
    GROUP BY fraud_reported
""").df())