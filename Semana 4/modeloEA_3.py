import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Los mismos datos
np.random.seed(42)
siniestros = np.random.exponential(scale=1500, size=200)

# Ajustar distribución
param = stats.expon.fit(siniestros)

# VaR — Value at Risk
VaR_95 = stats.expon.ppf(0.95, *param)
VaR_99 = stats.expon.ppf(0.99, *param)

# CVaR — Conditional Value at Risk
CVaR_95 = siniestros[siniestros >= VaR_95].mean()
CVaR_99 = siniestros[siniestros >= VaR_99].mean() # CVaR_99% = "nan €" porque Var_99% = Máximo = 6.501,24€

print("=== MEDIDAS DE RIESGO ===")
print(f"VaR  95%:  {VaR_95:.2f} €")
print(f"VaR  99%:  {VaR_99:.2f} €")
print(f"CVaR 95%:  {CVaR_95:.2f} €")
print(f"CVaR 99%:  {CVaR_99:.2f} €")

# Gráfico con VaR marcado
x = np.linspace(0, max(siniestros), 200)
plt.figure(figsize=(10, 5))
plt.hist(siniestros, bins=30, density=True,
         color="steelblue", edgecolor="white", label="Datos reales")
plt.plot(x, stats.expon.pdf(x, *param),
         color="red", linewidth=2, label="Exponencial ajustada")
plt.axvline(VaR_95, color="orange", linestyle="--",
            label=f"VaR 95%: {VaR_95:.0f}€")
plt.axvline(VaR_99, color="darkred", linestyle="--",
            label=f"VaR 99%: {VaR_99:.0f}€")
plt.title("Distribución de siniestros con VaR")
plt.xlabel("Coste (€)")
plt.ylabel("Densidad")
plt.legend()
plt.savefig("var_siniestros.png", dpi=150, bbox_inches="tight")
plt.show()