import numpy as np
import matplotlib.pyplot as plt

# Define la función f(x, y)
def f(x, y):
    return 2*x*np.exp(-3*x) - 3*y

# Define el método de Euler
def euler(x0, y0, h, N):
    x_values = [x0]
    y_values = [y0]
    
    for i in range(N):
        x = x_values[-1]
        y = y_values[-1]
        
        y_prime = f(x, y)
        
        x_next = x + h
        y_next = y + h * y_prime
        
        x_values.append(x_next)
        y_values.append(y_next)
        
    return x_values, y_values

# Parámetros iniciales
x0_range = [-1, -0.5]  # Diferentes condiciones iniciales para x
y0_range = [-0.5, 2]  # Diferentes condiciones iniciales para y
h = 0.1  # Tamaño del paso
N = 50  # Número de pasos

# Resuelve la ecuación diferencial para ambas condiciones iniciales
for x0, y0 in zip(x0_range, y0_range):
    x_values, y_values = euler(x0, y0, h, N)
    plt.plot(x_values, y_values, label=f'x0={x0}, y0={y0}')

# Dibuja la gráfica
plt.xlabel('x')
plt.ylabel('y')
plt.title('Soluciones de la Ecuación Diferencial')
plt.legend()
plt.show()
