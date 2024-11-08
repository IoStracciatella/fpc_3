Explicação resumida dos códigos:
1. A sequência de Fibonacci é gerada através de um loop que itera n vezes os valores de uma sequência. A cada iteração, 2 valores dessa sequência são somados, o resultado da soma é atribuído a uma variável V e
armazenado em uma lista. Após isso, com o valor que da soma dos 2 termos armazenado na variável, é calculado a soma de V com o termo anterior da sequência, e assim por diante, gerando a famosa sequência de
Fibonacci.
2. Para calcular os valores da iteração de ponto fixo, é criado um loop que itera n vezes, e a cada iteração o valor da imagem de uma função F é inserido na entrada de uma função B. Após isso, o valor da
imagem da função B é atribuído a entrada da função A, e esse processo é repetido inúmeras vezes, aproximando do ponto fixo da função (ou ponto de encontro) das funções a cada iteração.
3. O que o método de Jacobi faz: Ele aproxima os valores da solução de um sistema de equações a cada iteração do loop. Para calcular o erro entre a aproximação dos valores e as raízes reais exatas, primeiramente é
calculado, exatamente, as raízes reais das equações. Em seguida, para cada iteração é calculado a diferença entre as raízes e aproximação delas com o método de Jacobi, obtendo assim, os erros
4. Mesma ideia do código anterior. Aproximamos o valor de cada variável utilizando o método de Jacobi, mas dessa vez para um sistema 3 x 3
5. O método de Newton é utilizado para encontrar as raízes de uma função. A partir de um chute inicial para os valores das raízes, a cada iteração, o método de Newton aproxima os valores exatos dessa(s) raiz(es). Para isso, a cada iteração é calculada a diferença entre a raiz aproximada "x0" e o quociente da função no mesmo ponto x0, pela sua derivada. Dessa forma, a cada iteração, os valores exatos das raízes são aproximados
