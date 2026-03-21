import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Los mismos datos del "modeloEA_1.py"
np.random.seed(42)
siniestros = np.random.exponential(scale=1500, size=200)

# Ajustar distribución exponencial por MLE
# MLE = Maximum Likelihood Estimation (Estimación de Máxima Verosimilitud)
param = stats.expon.fit(siniestros)
print(f"Media estimada por MLE: {param[1]:.2f} €")
print(f"Media real de los datos: {siniestros.mean():.2f} €")

# Comparar datos reales vs distribución ajustada
x = np.linspace(0, max(siniestros), 200)

plt.figure(figsize=(10, 5))
plt.hist(siniestros, bins=30, density=True,
         color="steelblue", edgecolor="white", label="Datos reales")
plt.plot(x, stats.expon.pdf(x, *param),
         color="red", linewidth=2, label="Exponencial ajustada")
plt.title("Ajuste de distribución exponencial — MLE")
plt.xlabel("Coste (€)")
plt.ylabel("Densidad")
plt.legend()
plt.savefig("ajuste_exponencial.png", dpi=150, bbox_inches="tight")
plt.show()
