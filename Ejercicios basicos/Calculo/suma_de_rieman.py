import numpy as np

# Definir la función f(x) = x^2
def f(x):
    return x**2

# Número de subintervalos
n = 100

# Calcular el ancho de cada subintervalo
delta_x = 1 / n

# Calcular la suma de Riemann
suma_riemann = 0
for i in range(1, n+1):
    xi = i / n
    suma_riemann += f(xi) * delta_x

# Imprimir el resultado
print("Aproximación del área utilizando sumas de Riemann para n = 100:", suma_riemann)
