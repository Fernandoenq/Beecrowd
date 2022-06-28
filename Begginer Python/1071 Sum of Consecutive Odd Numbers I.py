A = int(input())
B = int(input())
maior = A if A > B else B
menor = A+1 if A < B else B+1
res = 0
while menor < maior: #enquanto o menor valor colocado ainda for menor que o maior valor vai somando
    if(menor%2 != 0):res += menor #Vai somando os impares se o menor numero for impar
    menor +=1
print(res)