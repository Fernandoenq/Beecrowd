A = []
B = 0
for x in range(0,6):
    A.append(float(input()))
    if A[x] > 0: B += 1
print("{} valores positivos".format(int(B)))


