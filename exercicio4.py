# Método de Jacobi na Matriz

import numpy as np

# Valores iniciais que serão inseridos na função
x0, y0, z0 = 0, 0, 0
x0 = float(input('Escolha um valor inicial de x para iniciar a aproximação. n: '))
y0 = float(input('Escolha um valor inicial de y para iniciar a aproximação. n: '))
z0 = float(input('Escolha um valor inicial de z para iniciar a aproximação. n: '))
raizes_x = []
raizes_y = []
raizes_z = []

def metodoDeJacobi(x0, y0, z0, tol):
    x, y, z = 0, 0, 0 # Essas variáveis são os valores que serão calculados, e recalculados, e recalculados... até a aproximar o bastante da solução
    x, y, z = x0, y0, z0

    while True:
        # Calcula novos valores de x e y usando a iteração de Jacobi
        x_novo = (1 + y + z) / 3
        y_novo = (2 + x + z) / 3
        z_novo = (3 + x + y) / 3

        # Critério de parada com a tolerância dada, ou seja, se ele aproximou a solução do sistema o suficiente da resposta exata
        if abs(x_novo - x) < tol and abs(y_novo - y) and abs(z_novo - z) < tol:
            break

        # Atualiza os valores de x e y
        x, y, z = x_novo, y_novo, z_novo

        raizes_x.append(x)
        raizes_y.append(y)
        raizes_z.append(z)

tolerancias = [10**-i for i in range(2, 9)] # Valores de tolerância, a gente vai usar pra iterar a função pra cada elemento dessa lista

# Executa o método de Jacobi para cada tolerância. "tol" assume o valor de 1 valor de "tolerancias" a cada iteração
for tol in tolerancias:
    iteracoes = metodoDeJacobi(x0, y0, z0, tol)

print('-' * 30, '\nAproximando os valores de x\n', '-' * 30, '\n', raizes_x)
print('-' * 30, '\nAproximando os valores de y\n', '-' * 30, '\n', raizes_y)
print('-' * 30, '\nAproximando os valores de z\n', '-' * 30, '\n', raizes_z)