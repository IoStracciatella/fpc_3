import numpy as np
import matplotlib.pyplot as plt

# Define a função f(x) e a sua derivada f'(x)
def f(x):
    return x * np.exp(-x**2) - 0.1

def df(x):
    return np.exp(-x**2) * (1 - 2 * x**2)

limiteDeIteracoes = int(input('Defina um limite de iterações para evitar um loop infinito: '))

# Função que realiza o método de Newton
def metodoDeNewton(x0, tol=1e-5, limiteDeIteracoes=100):
    x = x0
    for i in range(limiteDeIteracoes):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x, i
        if dfx == 0:
            print("Derivada zero. Método falhou.")
            return None, i
        x = x - fx / dfx
    print("Número máximo de iterações atingido.")
    return x, limiteDeIteracoes

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

# Testa o método de Newton com os valores iniciais escolhidos
x0_values = [float(input('Escolha um ponto inicial x0: ')), float(input('Agora escolhe outro ponto inicial x0: '))]
for x0 in x0_values:
    raiz, iteracoes = metodoDeNewton(x0)
    print(f"Raiz encontrada: {raiz} com {iteracoes} iterações para x0 = {x0}")
