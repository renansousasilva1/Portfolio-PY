cor_amarela = '\033[93m'
cor_azul = '\033[94m'
cor_reset = '\033[0m'
cor_roxa = '\033[95m'
cor_vermelha = '\033[91m'

multa = 280
vel= int(input("Qual é a velocidade do carro atual? "))
if vel <= 80:
    print("Tenha um bom dia! Dirija com cuidado.")
else:
    print("-=-"*20)
    print(cor_vermelha + "Multado! Você excedeu o limite, que é de 80 KM/h " + cor_reset)
    print("Você deve pagar uma multa de R${}".format(multa))
    print(" ")
    print("Tenha um bom dia e não esqueca de ter cuidado ao dirigir")
    print("-=-"*20)