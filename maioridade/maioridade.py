from datetime import datetime

anoatual = datetime.today().year
cont = 0
cont_menores = 0

for c in range(1, 7):
    ano = int(input("Em que ano a {}° pessoa nasceu? ".format(c)))
    idade = anoatual - ano
 
    if  idade >= 18:
        cont +=1
    else:
        cont_menores +=1

print("Ao todo tivemos {} pessoas maiores de idade.".format(cont))
print("Ao todo tivemos {} pessoas menores de idade.".format(cont_menores))