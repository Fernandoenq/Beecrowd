"""
Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.

Input
The input file contains three double values with one digit after the decimal point.

Output
The output file must contain 5 lines of data. Each line corresponds to one of the areas described above, always with a corresponding message (in Portuguese) and one space between the two points and the value. The value calculated must be presented with 3 digits after the decimal point.
"""

# -*- coding: utf-8 -*-

A,B,C = list(map(float,input().split()))
pi = 3.14159
a = (A*C)/2.0
b = pi*C*C
c = (A+B)/2.0*C
d = B*B
e = A*B
print("TRIANGULO: %0.3lf"%a)
print("CIRCULO: %0.3f"%b)
print("TRAPEZIO: %0.3f"%c)
print("QUADRADO: %0.3f"%d)
print("RETANGULO: %0.3f"%e)