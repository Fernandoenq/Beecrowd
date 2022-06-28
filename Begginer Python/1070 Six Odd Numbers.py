A = int(input())
if(A%2 == 0):B = A + 11
else:B = A + 10
while A <= B:
    if(A%2 != 0):print(A)
    A += 1