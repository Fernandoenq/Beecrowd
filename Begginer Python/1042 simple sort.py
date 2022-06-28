A,B,C = list(map(int,input().split()))
D,E,F = A,B,C
n = 1
while n != 0:
    if((A < B) and (B < C)):
        n = 0
    if(A > B):
        A, B = B, A
    if(A > C):
        A, C = C, A
    if(B > C):
        B, C = C, B
print(f"{A}\n{B}\n{C}")
print(f"\n{D}\n{E}\n{F}")

#Duas formas

A,B,C = map(int,input().split())
list = [A,B,C]
list.sort()
print(f"{list[0]}\n{list[1]}\n{list[2]}")
print(f"\n{A}\n{B}\n{C}")