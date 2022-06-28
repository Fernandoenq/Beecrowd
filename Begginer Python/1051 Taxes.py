A = float(input())
if A > 0 and A <= 2000:print("Isento")
else:
    if A > 2000 and A <= 3000: res = (A - 2000) * 0.08
    elif A > 3000 and A <= 4500: res = (1000*0.08) + ((A - 3000) * 0.18)
    else: res = (1000*0.08) + (1500 * 0.18) +  ((A - 4500)*0.28)
    print("$ {:.2f}".format(res))