import random
from time import sleep
cor_amarela = '\033[93m'
cor_azul = '\033[94m'
cor_reset = '\033[0m'
cor_roxa = '\033[95m'
cor_vermelha = '\033[91m'

print(cor_amarela + "-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-" + cor_reset)
print(cor_azul +"Vou pensar em um número entre 0 e 5. Tente advinhar..." + cor_reset)
print(cor_amarela + "-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-" + cor_reset)

#Gerar número
lista=random.randint(0, 5)
chute=int(input("Digite o seu número: "))

print("Em que número eu pensei? {}".format(chute))
print("Eu pensei no número {}".format(lista))
print(cor_roxa + "Processando..." + cor_reset)
sleep(2)
print(" ")
if lista == chute:
    print(cor_amarela + "Parabéns! Você acertou!" + cor_reset)
else:
    print(cor_vermelha + "Eu ganhei! Você pensou no número errado." + cor_reset)