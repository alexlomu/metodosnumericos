import numpy as np
import matplotlib.pyplot as plt

def ecuacion_diferencial(x, y):
    return (2 - 3*x - y) / (x - 1)

def solucion_exacta(x):
    return (2*x-1.5*x*np.exp(2)+1)/(x-1)

def predictor_corrector(ecuacion, x0, y0, h, xf):
    x_values = [x0]
    y_values = [y0]
    errores = [0.0]  # Inicializar errores con 0 para el primer paso

    while x_values[-1] < xf:
        # Predictor (método de Euler)
        y_pred = y_values[-1] + h * ecuacion(x_values[-1], y_values[-1])

        # Corrector (método de Euler mejorado o método de Heun)
        y_corr = y_values[-1] + 0.5 * h * (ecuacion(x_values[-1], y_values[-1]) + ecuacion(x_values[-1] + h, y_pred))

        # Aplicar restricciones
        y_corr = max(-10, min(y_corr, 1))

        # Calcular el error en cada paso
        error = abs(solucion_exacta(x_values[-1]) - y_corr)
        errores.append(error)

        # Actualizar tiempo y valor de la función
        x_values.append(x_values[-1] + h)
        y_values.append(y_corr)

    return x_values, y_values, errores

# Parámetros iniciales
x0 = 2.0  # Tiempo inicial
y0 = -1.0  # Valor inicial de la función
h = 0.1   # Tamaño del paso
xf = 6.0  # Tiempo final

# Resolver la ecuación diferencial usando el método predictor-corrector
x, y, errores = predictor_corrector(ecuacion_diferencial, x0, y0, h, xf)

# Mostrar la solución y el error en el terminal
for i in range(len(x)):
    print(f"x = {x[i]:.2f}, y = {y[i]:.6f}, Error = {errores[i]:.6f}")

# Graficar la solución y el error
plt.subplot(2, 1, 1)
plt.plot(x, y, label='Solución Aproximada')
plt.plot(x, solucion_exacta(np.array(x)), label='Solución Exacta', linestyle='dashed')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Solución de la Ecuación Diferencial y Comparación con la Solución Exacta')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x, errores, label='Error')
plt.xlabel('x')
plt.ylabel('Error')
plt.title('Error en la Solución Aproximada')
plt.legend()

plt.tight_layout()
plt.show()
