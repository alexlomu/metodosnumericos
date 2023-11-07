def euler_method(func, y0, x0, xn, h):
    x_values = [x0]
    y_values = [y0]
    x = x0
    y = y0
    while x < xn:
        y = y + h * func(x, y)
        x = x + h
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

def func(x, y):
    return (2 - 3*x - y) / (x - 1)

# Datos iniciales y restricciones
x0 = 2
xn = 6
y0 = -1
h = 4/100

# Llamada al método de Euler
x_values, y_values = euler_method(func, y0, x0, xn, h)

# Filtrar valores que cumplen las restricciones
x_values_filtered = []
y_values_filtered = []

for x, y in zip(x_values, y_values):
    if 2 <= x <= 6 and -10 <= y <= 1:
        x_values_filtered.append(x)
        y_values_filtered.append(y)

# Imprimir resultados
for x, y in zip(x_values_filtered, y_values_filtered):
    print(f"x = {x}, y = {y}")
