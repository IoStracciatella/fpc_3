import numpy as np
import matplotlib.pyplot as plt

# Define a função f(x) e a sua derivada f'(x)
def f(x):
    return x * np.exp(-x**2) - 0.1

def df(x):
    return np.exp(-x**2) * (1 - 2 * x**2)

# Implementa o método de Newton
def newton_method(x0, tol=1e-5, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x, i
        if dfx == 0:
            print("Derivada zero. Método falhou.")
            return None, i
        x = x - fx / dfx
    print("Número máximo de iterações atingido.")
    return x, max_iter

# Plot da função para ver onde estão as raízes
x_vals = np.linspace(-1, 2, 400)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label='f(x) = x * exp(-x^2) - 0.1')
plt.axhline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

# Testa o método de Newton com valores iniciais próximos das raízes
x0_values = [float(input('Escolha um ponto inicial x0: ')), float(input('Agora escolhe outro ponto inicial x0: '))]
for x0 in x0_values:
    root, iterations = newton_method(x0)
    print(f"Raiz encontrada: {root} com {iterations} iterações para x0 = {x0}")