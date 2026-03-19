import duckdb
import pandas as pd

df=pd.read_csv("insurance_claims.csv")

# 1. ¿Cuántos registros tiene el dataset?
print(duckdb.query("SELECT COUNT(*) AS total FROM df").df())

# 2. ¿Cuál es el importe máximo reclamado?
print(duckdb.query("SELECT MAX(total_claim_amount) AS maximo FROM df").df())

# 3. ¿Cuántos casos de fraude hay?
print(duckdb.query("""
    SELECT fraud_reported,
           COUNT(*) AS total
    FROM df
    GROUP BY fraud_reported
    ORDER BY total DESC
""").df())

# 4. ¿Cuál es la reclamación media por estado?
print(duckdb.query("""
    SELECT incident_state,
           AVG(total_claim_amount) AS media,
           COUNT(*) AS casos
    FROM df
    GROUP BY incident_state
    ORDER BY media DESC
""").df())