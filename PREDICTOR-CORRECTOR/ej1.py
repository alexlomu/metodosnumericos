import numpy as np
import matplotlib.pyplot as plt

def ecuacion_diferencial(x, y):
    return (2 - 3*x - y) / (x - 1)


def predictor_corrector(ecuacion, x0, y0, h, xf):
    # Inicializar listas para almacenar los resultados
    x_values = [x0]
    y_values = [y0]

    # Iterar hasta alcanzar el tiempo final tf
    while x_values[-1] < xf:
        # Predictor (método de Euler)
        y_pred = y_values[-1] + h * ecuacion(x_values[-1], y_values[-1])

        # Corrector (método de Euler mejorado o método de Heun)
        y_corr = y_values[-1] + 0.5 * h * (ecuacion(x_values[-1], y_values[-1]) + ecuacion(x_values[-1] + h, y_pred))

        # Actualizar tiempo y valor de la función
        x_values.append(x_values[-1] + h)
        y_values.append(y_corr)

    return x_values, y_values

# Parámetros iniciales
x0 = 2.0  # Tiempo inicial
y0 = 1.0  # Valor inicial de la función
h = 0.1   # Tamaño del paso
xf = 6.0  # Tiempo final

# Resolver la ecuación diferencial usando el método predictor-corrector
x, y = predictor_corrector(ecuacion_diferencial, x0, y0, h, xf)

# Mostrar la solución en el terminal
for i in range(len(x)):
    print(f"x = {x[i]}, y = {y[i]}")

# Graficar la solución
plt.plot(x, y, label='Solución')
plt.xlabel('Tiempo')
plt.ylabel('y(x)')
plt.title('Solución de la Ecuación Diferencial por Método Predictor-Corrector')
plt.legend()
plt.show()
