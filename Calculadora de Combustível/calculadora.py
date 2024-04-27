distancia=float(input("Insira a quantidade de KM's: "))
consumo= float(input("Qual o consumo do veículo? "))
combustivel = distancia/consumo
print ("Para a distância de {}km's, o consumo aproximado de combustível é de {} litros ".format(distancia, combustivel))