import numpy as np

# Define a matriz A
A = np.array([[1, 0, 0],
              [0, 2, 0],
              [0, 0, 3]])

# Definimos o vetor inicial x0 e normalizamos ele
# Preciamos normalizar o vetor porque caso contrário, ele cresceria muito conforme fosse multiplicado pelas matrizes,
# e não queremos isso, queremos apenas estudar "mudanças na direção" do vetor
x = np.array([1, 1, 1], dtype=float)
x = x / np.linalg.norm(x)

# Quanto mais iterações, mais próximo o vetor será do autovalor dominante da matriz
numero_iteracoes = 10
numero_iteracoes = int(input('Quantas iterações você quer realizar? n: '))

for i in range(numero_iteracoes = numero_iteracoes):
    # Multiplica o vetor pela matriz
    y = np.dot(A, x)
    
    # Calcula o autovalor aproximado
    lambda_aprox = np.dot(x, y)
    
    # Temos que normalizar o vetor para a próxima iteração, como explicado anteriormente
    x = y / np.linalg.norm(y)
    
    # Mostra o resultado da iteração
    print(f"Iteração {i + 1}: autovalor aproximado = {lambda_aprox}, autovetor = {x}")

# Implementação para matriz com valores aleatórios entre 0 e 1
n = 3  # Você pode mudar o valor de n para matrizes maiores
A_random = np.diag(np.random.uniform(0, 1, n))

x = np.ones(n)
x = x / np.linalg.norm(x)

for i in range(numero_iteracoes):
    y = np.dot(A_random, x)
    lambda_aprox = np.dot(x, y)
    x = y / np.linalg.norm(y)
    print(f"Iteração de N°{i + 1} (aleatória): autovalor aproximado = {lambda_aprox}, autovetor = {x}")
