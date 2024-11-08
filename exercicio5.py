import numpy as np
import matplotlib.pyplot as plt

# Define a função f(x) e a sua derivada f'(x)
def f(x):
    return x * np.exp(-x**2) - 0.1

def df(x):
    return np.exp(-x**2) * (1 - 2 * x**2)

escolhaTol = float(input('Defina um valor de tolerância (float): '))
limiteDeIteracoes = int(input('Defina um limite de iterações para evitar um loop infinito (RECOMENDADO VALORES ENTRE ]0, 10^5]) '))

# Função que realiza o método de Newton
def metodoDeNewton(x0, tol=escolhaTol, parLimiteDeIteracoes=limiteDeIteracoes):
    x = x0
    for i in range(parLimiteDeIteracoes):
        fx = f(x) # As variáveis fx e dfx armazenam os valores atuais de f(x) e f'(x) respectivamente, para que esse valor seja usado na próxima iteração
        dfx = df(x)
        if abs(fx) < tol: # Não é tão óbvio (eu acho), mas esse if verifica o quão próximo o valor escolhido está de zero. Ou seja, ele verifica se x0 está se aproximando de alguma raiz, dado que raízes são pontos onde f(x) = 0
            return x, i
        if dfx == 0: # Se a derivada é zero, o método falhou. Lembra, divisão por zero não existe
            print("Derivada zero. Método falhou.")
            return None, i
        x = x - fx / dfx
    print("Número máximo de iterações atingido.")
    return x, parLimiteDeIteracoes

# Plot da função para ver onde estão as raízes
x_vals = np.linspace(-1, 2, 400)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label='f(x) = x * exp(-x^2) - 0.1')
plt.axhline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.suptitle('Gráfico da função 'r"$f(x) = x e^{-x^2} - 0.1$")
plt.title('Observe o gráifico para ter uma noção de quais valores x0 escolher')
plt.show()

# Testa o método de Newton com os valores iniciais escolhidos
x0_values = [float(input('Escolha um ponto inicial x0: ')), float(input('Agora escolhe outro ponto inicial x0: '))]
for x0 in x0_values:
    raiz, iteracoes = metodoDeNewton(x0)
    print(f"Raiz encontrada: {raiz} com {iteracoes} iterações para x0 = {x0}")
