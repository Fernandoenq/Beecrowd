A,B = list(map(int,input().split(" ")))
if(A > B):print('Sao Multiplos') if A % B == 0 else print('Nao sao Multiplos')
else:print('Sao Multiplos') if B % A == 0 else print('Nao sao Multiplos')
 