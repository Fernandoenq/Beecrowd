"""
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to calculate the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

Input
Read 3 floating-point numbers (double) A, B and C.

Output
Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.
"""

#Versão final
A,B,C = list(map(float,input().split(" ")))
caso = (B*B) - (4*A*C)
if (A == 0.0) or (caso < 0):
    print("Impossivel calcular")
else:
    X1 = ((B * -1) + ((B*B) - (4*A*C)) ** 0.5) / (2 * A)
    X2 = ((B * -1) - ((B*B) - (4*A*C)) ** 0.5) / (2 * A)

    print("R1 = {:.5f}".format(X1))
    print("R2 = {:.5f}".format(X2))
