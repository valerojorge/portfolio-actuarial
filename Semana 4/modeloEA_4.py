import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Los mismos datos
np.random.seed(42)
siniestros = np.random.exponential(scale=1500, size=200)

# Ajustar distribuciones
param_exp     = stats.expon.fit(siniestros)
param_gamma   = stats.gamma.fit(siniestros)
param_lognorm = stats.lognorm.fit(siniestros)

# Crear 10 grupos con percentiles
clases = np.percentile(siniestros, np.linspace(0, 100, 11))

# ni — frecuencias observadas
observadas, _ = np.histogram(siniestros, bins=clases)

print("=== GRUPOS Y FRECUENCIAS OBSERVADAS ===")
for i in range(len(clases)-1):
    print(f"Grupo {i+1}: {clases[i]:.0f}€ - {clases[i+1]:.0f}€  →  ni = {observadas[i]}")
# Función que calcula el test chi-cuadrado
def test_chi(siniestros, dist, param, clases, observadas):
    
    # npî — frecuencias esperadas
    esperadas = []
    for i in range(len(clases)-1):
        p = dist.cdf(clases[i+1], *param) - dist.cdf(clases[i], *param)
        esperadas.append(p * len(siniestros))
    esperadas = np.array(esperadas)

    # z = Σ (ni - npî)² / npî
    z = np.sum((observadas - esperadas)**2 / esperadas)

    # Grados de libertad = grupos - parámetros - 1
    gl = len(observadas) - len(param) - 1

    # p-valor
    p_valor = 1 - stats.chi2.cdf(z, gl)

    return z, p_valor, gl

# Calcular para cada distribución
z_exp,     p_exp,     gl_exp     = test_chi(siniestros, stats.expon,   param_exp,     clases, observadas)
z_gamma,   p_gamma,   gl_gamma   = test_chi(siniestros, stats.gamma,   param_gamma,   clases, observadas)
z_lognorm, p_lognorm, gl_lognorm = test_chi(siniestros, stats.lognorm, param_lognorm, clases, observadas)

print("\n=== TEST CHI-CUADRADO ===")
print(f"Exponencial  →  z: {z_exp:.4f}   gl: {gl_exp}   p-valor: {p_exp:.4f}")
print(f"Gamma        →  z: {z_gamma:.4f}   gl: {gl_gamma}   p-valor: {p_gamma:.4f}")
print(f"Log-normal   →  z: {z_lognorm:.4f}   gl: {gl_lognorm}   p-valor: {p_lognorm:.4f}")
print("\nMejor distribución → z más pequeño y p-valor más alto")

# Gráfico comparativo
x = np.linspace(0, max(siniestros), 200)
plt.figure(figsize=(10, 5))
plt.hist(siniestros, bins=30, density=True,
         color="steelblue", edgecolor="white", label="Datos reales")
plt.plot(x, stats.expon.pdf(x, *param_exp),
         color="red", linewidth=2, label=f"Exponencial p={p_exp:.3f}")
plt.plot(x, stats.gamma.pdf(x, *param_gamma),
         color="green", linewidth=2, label=f"Gamma p={p_gamma:.3f}")
plt.plot(x, stats.lognorm.pdf(x, *param_lognorm),
         color="orange", linewidth=2, label=f"Log-normal p={p_lognorm:.3f}")
plt.title("Comparación de distribuciones — Test Chi-cuadrado")
plt.xlabel("Coste (€)")
plt.ylabel("Densidad")
plt.legend()
plt.savefig("comparacion_distribuciones.png", dpi=150, bbox_inches="tight")
plt.show()