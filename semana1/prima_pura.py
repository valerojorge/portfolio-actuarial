conductores = ["joven", "adulto", "senior"]
frecuencias = [0.12, 0.05, 0.07]
severidades = [3000, 2000, 1500]

for i in range(3):
    prima = round((frecuencias[i] * severidades[i]),2)
    print(f"Conductor {conductores[i]}: prima pura = {prima} €")



