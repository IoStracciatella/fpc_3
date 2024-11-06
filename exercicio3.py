# Método de Jacobi

import numpy as np
import matplotlib.pyplot as plt

# Valores iniciais que serão inseridos na função
x0, y0 = 0, 0
x0 = float(input('Escolha um valor inicial de x para iniciar a aproximação. n: '))
y0 = float(input('Escolha um valor inicial de y para iniciar a aproximação. n: '))

def metodoDeJacobi(x0, y0, tol):
    x, y = 0, 0 # Essas variáveis são os valores que serão calculados, e recalculados, e recalculados... até a aproximar o bastante da solução
    x, y = x0, y0
    iteracoes = 0

    while True:
        # Calcula novos valores de x e y usando a iteração de Jacobi
        x_novo = (2 + y) / 3
        y_novo = (1 + 2 * x) / 4

        # Critério de parada com a tolerância dada, ou seja, se ele aproximou a solução do sistema o suficiente da resposta exata
        if abs(x_novo - x) < tol and abs(y_novo - y) < tol:
            break

        # Atualiza os valores de x e y
        x, y = x_novo, y_novo
        iteracoes += 1

    return iteracoes

tolerancias = [10**-i for i in range(2, 9)] # Valores de tolerância, a gente vai usar pra iterar a função pra cada elemento dessa lista
listaDeIteracoes = [] # Lista pra armazenar a quantidade de iterações usadas para aproximar o resultado para cada um dos erros

# Executa o método de Jacobi para cada tolerância. "tol" assume o valor de 1 valor de "tolerancias" a cada iteração
for tol in tolerancias:
    iteracoes = metodoDeJacobi(x0, y0, tol)
    listaDeIteracoes.append(iteracoes)

# Plota o gráfico
plt.plot(tolerancias, listaDeIteracoes, marker='o')
plt.xscale('log')
plt.xlabel('Erro (ε)')
plt.ylabel('Número de Iterações')
plt.title('Número de Iterações x Erro no Método de Jacobi')
plt.gca().invert_xaxis()
plt.show()
