# Cálculo da Sequência de Fibonacci

# Interface do programa
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? n: '))

# Definindo as variáveis que serão iteradas no loop, e depois usadas no cálculo da sequência
t1 = 0
t2 = 1
print('-' * 30)
print('{} {}'.format(t1, t2), end='')

# Loop que itera uma quantidade n de vezes, e para cada iteração, calcula 1 valor da sequência de Fibonacci através da diferença entre
# os valores de t1 e t2
cont = 3 # O contador começa em 3 pois os 3 primeiros núemros da sequência já foram impressos
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t1, t2), end='')
    # Move os valores de t1 e t2 pra direita na reta numérica
    t1 = t2
    t2 = t3
    cont += 1
print(' - FIM')
print('-' * 30)
