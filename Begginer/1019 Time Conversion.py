"""
Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.
"""

# -*- coding: utf-8 -*-

N = int(input())
H = 0
M = 0
S = 0
while N >= 3600:
    H += 1
    N -= 3600
while N >= 60:
    M += 1
    N -= 60
while N >= 1:
    S += 1
    N -= 1
print(H,M,S, sep=':')