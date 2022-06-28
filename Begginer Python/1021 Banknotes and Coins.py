"""
Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

Input
The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

Output
Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.
"""

N = float(input())
Cem=0
Cinq=0
Vinte=0
Dez=0
Cinc=0
Dois=0
Um=0
CCinq = 0
CVintCinco = 0
CDez = 0
CCinco = 0
CUm = 0
while N > 0.00:
    if N >= 100.00:
        Cem += 1.00
        N -= 100.00
    if (N >= 50.00) and (N < 100.00):
        Cinq += 1
        N -= 50.00
    if (N >= 20.00) and (N < 50.00):
        Vinte += 1
        N -= 20.00
    if(N >= 10.00) and (N < 20.00):
        Dez += 1
        N -= 10.00
    if(N >= 5.00) and (N < 10.00):
        Cinc += 1
        N -= 5.00
    if(N >= 2.00) and (N < 5.00):
        Dois += 1
        N -= 2.00

    if(N >= 1.00) and (N < 2.00):
        N -= 1.00
        Um += 1
    if (N >= 0.50) and (N < 1.00):
        CCinq += 1
        N -= 0.5
    if (N >= 0.25) and (N < 0.50):
        CVintCinco += 1
        N -= 0.25
    if (N >= 0.10) and (N < 0.25):
        CDez += 1
        N -= 0.10
    if(N >= 0.05) and (N < 0.10):
        CCinco += 1
        N -= 0.05
    if(N >= 0.01) and (N < 0.05):
        CUm += 1
        N -= 0.01
    if N < 0.01:
        N = 0


"""  
print("NOTAS:")
print("%i nota(s) de R$ 100.00"%Cem)
print("%i nota(s) de R$ 50.00"%Cinq)
print("%i nota(s) de R$ 20.00"%Vinte)
print("%i nota(s) de R$ 10.00"%Dez)
print("%i nota(s) de R$ 5.00"%Cinc)
print("%i nota(s) de R$ 2.00"%Dois)
print("MOEDAS:")
print("%i moeda(s) de R$ 1.00"%Um)
print("%i moeda(s) de R$ 0.50"%CCinq)
print("%i moeda(s) de R$ 0.25"%CVintCinco)
print("%i moeda(s) de R$ 0.10"%CDez)
print("%i moeda(s) de R$ 0.05"%CCinco)
print("%i moeda(s) de R$ 0.01"%CUm)
"""

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(Cem)))
print('{} nota(s) de R$ 50.00'.format(int(Cinq)))
print('{} nota(s) de R$ 20.00'.format(int(Vinte)))
print('{} nota(s) de R$ 10.00'.format(int(Dez)))
print('{} nota(s) de R$ 5.00'.format(int(Cinc)))
print('{} nota(s) de R$ 2.00'.format(int(Dois)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(Um)))
print('{} moeda(s) de R$ 0.50'.format(int(CCinq)))
print('{} moeda(s) de R$ 0.25'.format(int(CVintCinco)))
print('{} moeda(s) de R$ 0.10'.format(int(CDez)))
print('{} moeda(s) de R$ 0.05'.format(int(CCinco)))
print('{} moeda(s) de R$ 0.01'.format(int(CUm)))