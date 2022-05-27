A = input().split(" ")
B1,B2,B3 = list(map(int,input().split(" : ")))
C = input().split(" ")
D1,D2,D3 = list(map(int,input().split(" : ")))
D = int(C[1]) - int(A[1])
H = D1 - B1
M = D2 - B2
S = D3 - B3
if(S < 0):
    S += 60
    M -= 1
if(M < 0):
    M += 60
    H -= 1
if(H < 0):
    H += 24
    D -= 1
print("{} dia(s)".format(D))
print("{} hora(s)".format(H))
print("{} minuto(s)".format(M))
print("{} segundo(s)".format(S))