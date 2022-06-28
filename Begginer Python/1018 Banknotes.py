"""
In this problem you have to read an integer value and calculate the smallest possible number of banknotes in which the value may be decomposed. The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the list of banknotes.

Input
The input file contains an integer value N (0 < N < 1000000).

Output
Print the read number and the minimum quantity of each necessary banknotes in Portuguese language, as the given example. Do not forget to print the end of line after each line, otherwise you will receive “Presentation Error”.
"""

# -*- coding: utf-8 -*-

N = int(input())
Cem=0
Cinq=0
Vinte=0
Dez=0
Cinc=0
Dois=0
Um=0
print(N)
while N > 0:
    if N >= 100:
        Cem += 1
        N -= 100
    if (N >= 50) and (N < 100):
        Cinq += 1
        N -= 50
    if (N >= 20) and (N < 50):
        Vinte += 1
        N -= 20
    if(N >= 10) and (N < 20):
        Dez += 1
        N -= 10
    if(N >= 5) and (N < 10):
        Cinc += 1
        N -= 5
    if(N >= 2) and (N < 5):
        Dois += 1
        N -= 2
    if(N >= 1) and (N < 2):
        Um += 1
        N -= 1
print("%i nota(s) de R$ 100,00"%Cem)
print("%i nota(s) de R$ 50,00"%Cinq)
print("%i nota(s) de R$ 20,00"%Vinte)
print("%i nota(s) de R$ 10,00"%Dez)
print("%i nota(s) de R$ 5,00"%Cinc)
print("%i nota(s) de R$ 2,00"%Dois)
print("%i nota(s) de R$ 1,00"%Um)