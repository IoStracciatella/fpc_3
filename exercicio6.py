import numpy as np

# Define a matriz A
A = np.array([[1, 0, 0],
              [0, 2, 0],
              [0, 0, 3]])

# Define o vetor inicial x0 (normalizado)
x = np.array([1, 1, 1], dtype=float)
x = x / np.linalg.norm(x)

# Número de iterações
num_iteracoes = 10

for i in range(num_iteracoes):
    # Multiplica o vetor pela matriz
    y = np.dot(A, x)
    
    # Calcula o autovalor aproximado
    lambda_aprox = np.dot(x, y)
    
    # Normaliza o vetor para a próxima iteração
    x = y / np.linalg.norm(y)
    
    # Mostra o resultado da iteração
    print(f"Iteração {i + 1}: autovalor aproximado = {lambda_aprox}, autovetor = {x}")

# Implementação para matriz com valores aleatórios entre 0 e 1
n = 3  # Pode mudar o valor de n para matrizes maiores
A_random = np.diag(np.random.uniform(0, 1, n))

x = np.ones(n)
x = x / np.linalg.norm(x)

for i in range(num_iteracoes):
    y = np.dot(A_random, x)
    lambda_aprox = np.dot(x, y)
    x = y / np.linalg.norm(y)
    print(f"Iteração {i + 1} (aleatória): autovalor aproximado = {lambda_aprox}, autovetor = {x}")