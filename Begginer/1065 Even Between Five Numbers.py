A = []
P = 0
I = 0
Pos = 0
Neg = 0
for x in range(0,5):
    A.append(float(input()))
    if A[x]%2 == 0: P += 1
    if A[x]%2 != 0: I += 1
    if A[x] > 0: Pos += 1
    if A[x] < 0: Neg += 1
print("{} valor(es) par(es)".format(int(P)))
print("{} valor(es) impar(es)".format(int(I)))
print("{} valor(es) positivo(s)".format(int(Pos)))
print("{} valor(es) negativo(s)".format(int(Neg)))