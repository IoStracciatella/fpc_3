# Iteração de Ponto Fixo

import numpy as np
import matplotlib.pyplot as plt

# Define a função phi(x) = 1/sqrt(x)
def phi(x):
    return 1/np.sqrt(x)

print('-' * 30)
print('Iteração de Ponto Fixo')
print('-' * 30)
valorIterador = int(input('Quantas iterações você quer realizar? n: '))
x0 = 0.75

# Inicializa listas para armazenar os valore gerados em cada iteração
valores_x = [x0]
valores_y = [phi(x0)]

# Executa a iteração de ponto fixo com cruzamento entre y=x e y=phi(x)
for i in range(valorIterador):
    proximo_x = phi(valores_x[-1])  # Calcula o próximo valor
    valores_x.append(valores_x[-1])  # Repete o x para a representação visual
    valores_y.append(proximo_x)
    
    valores_x.append(proximo_x)  # Move o x para o próximo valor calculado
    valores_y.append(proximo_x)  # Define y = x para o próximo ponto

# Plota o gráfico com as iterações
x_range = np.linspace(0.7, 1.2, 100)
plt.figure(figsize=(8, 8))
plt.plot(x_range, x_range, 'k--', label='y = x')  # Linha y = x
plt.plot(x_range, phi(x_range), 'g-', label='y = ' r"$\varphi(x)$")  # Gráfico da função phi(x)
plt.plot(valores_x, valores_y, 'b-o', markersize=5, label='Iteração de ponto fixo')
plt.xlabel('x')
plt.ylabel(r"$\varphi(x)$")
plt.title('Iteração de Ponto Fixo para ' r"$\varphi(x)$ = 1/sqrt(x)")
plt.grid()
plt.legend()
plt.show()