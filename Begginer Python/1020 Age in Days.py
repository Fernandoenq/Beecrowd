"""
Read an integer value corresponding to a person's age (in days) and print it in years, months and days, followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”.

Note: only to facilitate the calculation, consider the whole year with 365 days and 30 days every month. In the cases of test there will never be a situation that allows 12 months and some days, like 360, 363 or 364. This is just an exercise for the purpose of testing simple mathematical reasoning.

Input
The input file contains 1 integer value.

Output
Print the output, like the following example.
"""

# -*- coding: utf-8 -*-

X = int(input())
A = 0
M = 0
D = 0

while X >= 365:
    A += 1
    X -= 365
while X >= 30:
    M += 1
    X -= 30
while X >= 1:
    D += 1
    X -= 1
print("%i ano(s)"%A)
print("%i mes(es)"%M)
print("%i dia(s)"%D)