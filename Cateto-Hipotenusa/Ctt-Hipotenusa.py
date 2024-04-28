import math
catetooposto=float(input("Digite o valor do cateto oposto: "))
catetoadjacente=float(input("Digite o valor do cateto adjacente: "))


hipotenusa = math.hypot(catetooposto, catetoadjacente)
print ("A hipotenusa é: {:.2f} ".format(hipotenusa))