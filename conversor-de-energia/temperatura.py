joule = int(input("Insira a quantidade de Joules: "))
caloria= joule* 0.239
kwh= joule/3600000
eV =  joule * 1.602176565
print("A quantidade de {} joules equivale a {} calorias, {} kwh e {}eV".format(joule, caloria, kwh, eV))
