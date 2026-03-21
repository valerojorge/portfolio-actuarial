import numpy as np
import matplotlib.pyplot as plt

# Simulamos 200 siniestros con coste medio de 1500€
np.random.seed(42)
siniestros = np.random.exponential(scale=1500, size=200)

# Estadísticas básicas
print(f"Media:      {siniestros.mean():.2f} €")
print(f"Desviación: {siniestros.std():.2f} €")
print(f"Mínimo:     {siniestros.min():.2f} €")
print(f"Máximo:     {siniestros.max():.2f} €")

# Histograma
plt.figure(figsize=(10, 5))
plt.hist(siniestros, bins=30, color="steelblue", edgecolor="white")
plt.title("Distribución de costes de siniestros")
plt.xlabel("Coste (€)")
plt.ylabel("Frecuencia")
plt.savefig("histograma_siniestros.png", dpi=150, bbox_inches="tight")
plt.show()



