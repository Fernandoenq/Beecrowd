list = list(map(float,input().split(" ")))
C,B,A = sorted(list)
if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if (A*A) == ((B*B)+(C*C)):print("TRIANGULO RETANGULO")
    if (A*A) > ((B*B)+(C*C)):print("TRIANGULO OBTUSANGULO")
    if (A*A) < ((B*B)+(C*C)):print("TRIANGULO ACUTANGULO")
    if A == B and A == C:print("TRIANGULO EQUILATERO")
    if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):print("TRIANGULO ISOSCELES")