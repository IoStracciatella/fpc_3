#for Jacobi method
import numpy as np
import numpy.linalg as al
import copy

print('-' * 30)
print('Método de Jacobi')
print('-' * 30)

A=np.array([[10.,-1.,2.,0.],[-1.,11.,-1.,3.],[2.,-1.,10.,-1.],[0.,3.,-1.,8.]])
b=np.array([6.,25.,-11.,15.])
n=4
x0=np.array([0.,0.,0.,0.])
x=copy.deepcopy(x0)
NO=1000
Tol=1.e-3
k=1

while (k<NO):
    for i in range(n): #i=0,1,2,...n-1
        #summation of aij * X0j
        sum_a=0.0
        for j in range(n): #j=0,1,2,...n-1
            if j!=i:
                sum_a=sum_a+A[i][j]*x0[j]
        x[i]=(b[i]-sum_a)/A[i][i]
    
    diff_inf=al.norm(x-x0,np.inf)/al.norm(x,np.inf)
    print(k, "ª iteração", x)
    if (diff_inf<Tol):
        break
    k=k+1
    x0=copy.deepcopy(x)

if (k==NO+1):
    print("O método falhou após pois não há iterações!")
else:
    print("Método concluído com sucesso :D")