num = float(input())
if(num <= 400): porc = 0.15
elif((num > 400) and (num <= 800)):porc = 0.12
elif((num > 800) and (num <= 1200)):porc = 0.10
elif((num > 1200) and (num <= 2000)):porc = 0.07
else:porc = 0.04
print("Novo salario: {:.2f}".format(num + (num*porc)))
print("Reajuste ganho: {:.2f}".format(num*porc))
print("Em percentual: {} %".format(int(porc*100)))
