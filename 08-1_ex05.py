A = list()
B = list()
C = list()
for i in range(25):
    A.append(int(input(f'Digite o {i+1}º número inteiro de A: ')))

for i in range(25):
    B.append(int(input(f'Digite o {i+1}º número inteiro de B: ')))

for i in range(25):
    C.append(A[i])
    C.append(B[i])
print(f'Lista C de 50 elementos: {C}.')
