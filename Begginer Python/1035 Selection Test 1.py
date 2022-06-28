"""
Read 4 integer values A, B, C and D. Then if B is greater than C and D is greater than A and if the sum of C and D is greater than the sum of A and B and if C and D were positives values and if A is even, write the message “Valores aceitos” (Accepted values). Otherwise, write the message “Valores nao aceitos” (Values not accepted).

Input
Four integer numbers A, B, C and D.

Output
Show the corresponding message after the validation of the values​​.
"""

A,B,C,D = list(map(int,input().split()))
val = 0
if B > C:
    val += 1
if D > A:
    val += 1
if (C + D) > (A + B):
    val += 1
if C > 0:
    val += 1
if D > 0:
    val += 1
if (A % 2) == 0:
    val += 1
if(val == 6):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")