# Cálculo da Sequência de Fibonacci

import numpy

# Interface do programa
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? n: '))

# Definindo as variáveis que serão iteradas no loop, e depois usadas no cálculo da sequência
t1 = 0
t2 = 1
vetorFibonacci = [t1, t2]
print('-' * 30)
print('{} - {}'.format(t1, t2), end='')

# Loop que itera uma quantidade n de vezes, e para cada iteração, calcula 1 valor da sequência de Fibonacci através da diferença entre
# os valores de t1 e t2, e então, adicionados a uma matriz vetor
cont = 3 # O contador começa em 3 pois os 3 primeiros núemros da sequência já foram impressos
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    vetorFibonacci.append(t3)
    # Move os valores de t1 e t2 pra direita na reta numérica
    t1 = t2
    t2 = t3
    cont += 1
print(' - FIM')
print('-' * 30)
if input('Deseja ver os valores no vetor? s/n ').strip().lower() == 's': print('Valores no vetor', vetorFibonacci)
