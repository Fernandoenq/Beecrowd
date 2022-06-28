A,B,C = list(map(float,input().split()))
if( ((B - C) < A) and (A < (B + C)) and (((A - C) < B) and (B < (A + C))) and (((A - B) < C) and (C < (A + B))) ):
    print('Perimetro = {:.1f}'.format(A+B+C))
else:
    print('Area = {:.1f}'.format(((A+B)*C)/2))
        



