A = []
B = 0
C = 0
for x in range(0,6):
    A.append(float(input()))
    if A[x] > 0: 
        B += 1
        C += A[x]
print("{} valores positivos".format(int(B)))
print("{:.1f}".format(C/B))