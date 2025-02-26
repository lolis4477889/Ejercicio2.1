# -*- coding: utf-8 -*-
"""Ejercicio1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KlrJQkGXWwdPNDhnXFpKZLE0LcOpU0mB
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir la función

def f(x):
    return x**3 - 4*x - 9

# Algoritmo numérico del Método de Bisección
def biseccion(a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable en el intervalo dado.")
        return None

    iteraciones = []
    errores_abs = []
    errores_rel = []
    errores_cuad = []
    c_old = a  # Para calcular errores

    for i in range(max_iter):
        c = (a + b) / 2
        iteraciones.append(c)

        error_abs = abs(c - c_old)
        error_rel = abs(error_abs / c) if c != 0 else 0
        error_cuad = error_abs ** 2

        errores_abs.append(error_abs)
        errores_rel.append(error_rel)
        errores_cuad.append(error_cuad)

        if abs(f(c)) < tol or error_abs < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_old = c

    return iteraciones, errores_abs, errores_rel, errores_cuad

# Parámetros iniciales
a, b = 2, 3
iteraciones, errores_abs, errores_rel, errores_cuad = biseccion(a, b)

# Crear la figura
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Gráfica de la función y la convergencia de iteraciones
x = np.linspace(a - 1, b + 1, 400)
y = f(x)

ax[0].plot(x, y, label=r'$f(x) = x^3 - 4x - 9$', color='b')
ax[0].axhline(0, color='k', linestyle='--', linewidth=1)
ax[0].scatter(iteraciones, [f(c) for c in iteraciones], color='red', label='Iteraciones')
ax[0].set_xlabel('x')
ax[0].set_ylabel('f(x)')
ax[0].set_title("Convergencia del Método de Bisección")
ax[0].legend()
ax[0].grid()

# Gráfica de convergencia del error
ax[1].plot(range(1, len(errores_abs)+1), errores_abs, marker='o', linestyle='-', color='r', label='Error Absoluto')
ax[1].plot(range(1, len(errores_rel)+1), errores_rel, marker='s', linestyle='-', color='g', label='Error Relativo')
ax[1].plot(range(1, len(errores_cuad)+1), errores_cuad, marker='^', linestyle='-', color='b', label='Error Cuadrático')
ax[1].set_yscale("log")
ax[1].set_xlabel("Iteración")
ax[1].set_ylabel("Error")
ax[1].set_title("Errores en cada Iteración")
ax[1].legend()
ax[1].grid()

# Guardar y mostrar la figura
plt.savefig("biseccion_errores.png", dpi=300)
plt.show()