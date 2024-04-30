print("=============", end=' ')
print("Tabuada", end=' ')
print("=============")
numero=int(input("Digite um número: "))
for c in range(1, 11):
    print("{} x {} =".format(numero, c), numero*c)
    
print("==============", end='')
print("======================")