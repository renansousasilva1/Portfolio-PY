carteiraatual=float(input("Quanto você tem na sua carteira? R$ "))
dolar= 5.17
euro= 5.53
rublo= 0.056
yuhan= 0.72
bitcoin = 321.374

print("Seu valor atual de {}, consegue comprar:".format(carteiraatual))
print("Você consegue comprar {:.2f} Dólares".format(carteiraatual / dolar))
print("Você consegue comprar {:.2f} Euros".format(carteiraatual/euro))
print("Você consegue comprar {:.2f} Rublos".format(carteiraatual/rublo))
print("Você consegue comprar {:.2f} Yuhans".format(carteiraatual/yuhan))
print("Você consegue comprar {:.5f} Sathoshis".format(carteiraatual/bitcoin))