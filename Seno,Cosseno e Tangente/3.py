import math
ang1= float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(ang1))
angulo_radianos = math.radians(ang1)
cosseno = math.cos(angulo_radianos)
tangente =  math.tan(math.radians(ang1))

print("O ângulo de {}° tem o seno de {:.2f}".format(ang1, seno))
print("O ângulo de {}° tem o cosseno de {:.2f}".format(ang1, cosseno))
print("O ângulo de {}° tem a tangente de {:.2f}".format(ang1, tangente))