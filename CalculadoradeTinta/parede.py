largura_parede=float(input("Digite a largura da parede: "))
altura_parede=float(input("Digite a altura da parede: "))
area= largura_parede*altura_parede
tinta= area/2
print("Sua parede tem a dimensão de {}m x {}m e sua área final é de {}m²". format(largura_parede, altura_parede, area))
print("Para pintar essa parede você precisa de {} litros de tinta ".format(tinta))
