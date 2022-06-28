A,B = list(map(int,input().split(" ")))
if(A > B):horas = (24 - A) + B
elif(A < B):horas = B - A 
else:horas = 24
print('O JOGO DUROU {} HORA(S)'.format(horas))