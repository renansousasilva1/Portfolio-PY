distancia=float(input("Qual a distância da sua viagem? "))
print("Você está prestes a realizar uma viagem de {} Km.".format(distancia))
preco1=distancia*0.50
preco2= distancia*0.45

if distancia <= 200:
    print("E o preço da sua viagem será de R${}".format(preco1))

else:
    print("E o preço da sua viagem será de R${}".format(preco2))