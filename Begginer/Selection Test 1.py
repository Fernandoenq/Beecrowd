    # -*- coding: utf-8 -*-

T = int(input()).split(" ")
A,B,C,D = T
if B > C:
    if D > A:
        if (C + D) > (A + B):
            if (C%2 == 0) & (D%2 == 0):
                print("Valores nao aceitos")