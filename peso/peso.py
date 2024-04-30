print("=="*10, end='')
print("Peso das pessoas", end='')
print("=="*10, end='')
print(" ")
pesos =[]
for c in range(1, 6):
    peso = float(input("Digite o peso da {}° pessoa: ".format(c)))
    pesos.append(peso)
maior = max(pesos)
menor = min(pesos)
diferenca = maior - menor

print("O maior peso é de {}kg".format(maior))
print("O menor peso  é de {}kg".format(menor))
print("A diferença entre o maior e o menor peso é de {}".format(diferenca))

    

    