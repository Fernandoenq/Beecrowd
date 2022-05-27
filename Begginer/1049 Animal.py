A = input()
B = input()
C = input()
if(A == 'vertebrado'):
    if(B == 'ave'):
        if(C == 'carnivoro'):
            res = 'aguia'
        else:
            res = 'pomba'
    else:
        if(C == 'onivoro'):
            res = 'homem'
        else:
            res = 'vaca'
else:
    if(B == 'inseto'):
        if(C == 'hematofago'):
            res = 'pulga'
        else:
            res = 'lagarta'
    else:
        if(C == 'hematofago'):
            res = 'sanguessuga'
        else:
            res = 'minhoca'
print(res)

#   or


A = input()
B = input()
C = input()
if A == 'vertebrado' and B == 'ave' and C == 'carnivoro': print('aguia')
if A == 'vertebrado' and B == 'ave' and C == 'onivoro': print('pomba') 
if A == 'vertebrado' and B == 'mamifero' and C == 'onivoro': print('homem') 
if A == 'vertebrado' and B == 'mamifero' and C == 'herbivoro': print('vaca') 
if A == 'invertebrado' and B == 'inseto' and C == 'hematofago': print('pulga') 
if A == 'invertebrado' and B == 'inseto' and C == 'herbivoro': print('lagarta') 
if A == 'invertebrado' and B == 'anelideo' and C == 'hematofago': print('sanguessuga') 
if A == 'invertebrado' and B == 'anelideo' and C == 'onivoro': print('minhoca')  
