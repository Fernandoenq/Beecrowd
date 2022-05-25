A,C,B,D = list(map(int,input().split(" ")))
mintotal=(  (( B * 60 ) + D) - (( A * 60 ) + C)  ) #bota tudo em min
if(mintotal<=0):mintotal+=24*60
horas=mintotal//60#Divisão int 
min=mintotal%60#resto da divisão
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas,min))