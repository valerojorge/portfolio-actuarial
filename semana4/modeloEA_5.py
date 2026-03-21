import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# =============================================
# ANÁLISIS ACTUARIAL COMPLETO DE SINIESTROS
# =============================================

np.random.seed(42)
siniestros = np.random.exponential(scale=1500, size=200)

# ── 1. ESTADÍSTICAS BÁSICAS ──
print("=== 1. ESTADÍSTICAS BÁSICAS ===")
print(f"Total siniestros: {len(siniestros)}")
print(f"Media:            {siniestros.mean():.2f} €")
print(f"Desviación:       {siniestros.std():.2f} €")
print(f"Mínimo:           {siniestros.min():.2f} €")
print(f"Máximo:           {siniestros.max():.2f} €")

# ── 2. AJUSTE DE DISTRIBUCIONES ──
param_exp     = stats.expon.fit(siniestros)
param_gamma   = stats.gamma.fit(siniestros)
param_lognorm = stats.lognorm.fit(siniestros)

# ── 3. TEST CHI-CUADRADO ──
def test_chi(siniestros, dist, param, clases, observadas):
    esperadas = []
    for i in range(len(clases)-1):
        p = dist.cdf(clases[i+1], *param) - dist.cdf(clases[i], *param)
        esperadas.append(p * len(siniestros))
    esperadas = np.array(esperadas)
    z = np.sum((observadas - esperadas)**2 / esperadas)
    gl = len(observadas) - len(param) - 1
    p_valor = 1 - stats.chi2.cdf(z, gl)
    return z, p_valor

clases = np.percentile(siniestros, np.linspace(0, 100, 11))
observadas, _ = np.histogram(siniestros, bins=clases)

z_exp,     p_exp     = test_chi(siniestros, stats.expon,   param_exp,     clases, observadas)
z_gamma,   p_gamma   = test_chi(siniestros, stats.gamma,   param_gamma,   clases, observadas)
z_lognorm, p_lognorm = test_chi(siniestros, stats.lognorm, param_lognorm, clases, observadas)


# Valores críticos
vc_exp     = stats.chi2.ppf(0.95, df=7)
vc_gamma   = stats.chi2.ppf(0.95, df=6)
vc_lognorm = stats.chi2.ppf(0.95, df=6)

print("\n=== 2. TEST CHI-CUADRADO ===")
print(f"Exponencial  →  z: {z_exp:.4f}   vc: {vc_exp:.4f}   p-valor: {p_exp:.4f}   {'NO rechazamos H0 ✅' if z_exp < vc_exp else 'Rechazamos H0 ❌'}")
print(f"Gamma        →  z: {z_gamma:.4f}   vc: {vc_gamma:.4f}   p-valor: {p_gamma:.4f}   {'NO rechazamos H0 ✅' if z_gamma < vc_gamma else 'Rechazamos H0 ❌'}")
print(f"Log-normal   →  z: {z_lognorm:.4f}   vc: {vc_lognorm:.4f}   p-valor: {p_lognorm:.4f}   {'NO rechazamos H0 ✅' if z_lognorm < vc_lognorm else 'Rechazamos H0 ❌'}")

# Mejor distribución
mejor = max([("Exponencial", p_exp),
             ("Gamma", p_gamma),
             ("Log-normal", p_lognorm)],
            key=lambda x: x[1])
print(f"\nMejor distribución: {mejor[0]} (p-valor: {mejor[1]:.4f})")

# ── 4. MEDIDAS DE RIESGO ──
print("\n=== 3. MEDIDAS DE RIESGO ===")
VaR_95 = stats.expon.ppf(0.95, *param_exp)
VaR_99 = stats.expon.ppf(0.99, *param_exp)
CVaR_95 = siniestros[siniestros >= VaR_95].mean()

print(f"VaR  95%:  {VaR_95:.2f} €")
print(f"VaR  99%:  {VaR_99:.2f} €")
print(f"CVaR 95%:  {CVaR_95:.2f} €")

# ── 5. GRÁFICO FINAL ──
x = np.linspace(0, max(siniestros), 200)
plt.figure(figsize=(12, 6))
plt.hist(siniestros, bins=30, density=True,
         color="steelblue", edgecolor="white", label="Datos reales")
plt.plot(x, stats.expon.pdf(x, *param_exp),
         color="red", linewidth=2, label=f"Exponencial p={p_exp:.3f}")
plt.plot(x, stats.gamma.pdf(x, *param_gamma),
         color="green", linewidth=2, label=f"Gamma p={p_gamma:.3f}")
plt.plot(x, stats.lognorm.pdf(x, *param_lognorm),
         color="orange", linewidth=2, label=f"Log-normal p={p_lognorm:.3f}")
plt.axvline(VaR_95, color="purple", linestyle="--",
            label=f"VaR 95%: {VaR_95:.0f}€")
plt.axvline(VaR_99, color="darkred", linestyle="--",
            label=f"VaR 99%: {VaR_99:.0f}€")
plt.title("Análisis Actuarial Completo de Siniestros")
plt.xlabel("Coste (€)")
plt.ylabel("Densidad")
plt.legend()
plt.savefig("analisis_actuarial_completo.png", dpi=150, bbox_inches="tight")
plt.show()