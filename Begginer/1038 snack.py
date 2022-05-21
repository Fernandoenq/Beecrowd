X,Y = list(map(int,input().split(" ")))
if(X == 1):
    res = Y * 4.00
elif(X == 2):
    res = Y * 4.50
elif(X == 3):
    res = Y * 5.00
elif(X == 4):
    res = Y * 2.00
elif(X == 5):
    res = Y * 1.50
print("Total: R$ {:.2f}".format(res))