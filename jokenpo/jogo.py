import random
from time import sleep
print("Suas opções:")
print(''' 
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA
      
      ''')

jogada=int(input("Digite a sua jogada: "))
sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print(" ")

jogadapc= random.randint(0,2)
print("-="*20)

if jogadapc == 0 and jogada == 2:
    print("A máquina escolheu PEDRA e você TESOURA")
    print("A máquina  venceu!")

if jogadapc == 0 and jogada == 1:
    print("A máquina escolheu PEDRA e você PAPEL")
    print("Parabéns! Você ganhou!")    
    
if jogadapc == 0 and jogada == 0:
    print("A máquina escolheu PEDRA e você também!")
    print("Jogue novamente!")
    
if jogadapc == 1 and jogada == 2:
    print("A máquina escolheu PAPEL e você TESOURA")
    print("Parabéns! Você ganhou!")

if jogadapc == 1 and jogada == 1:
    print("A máquina escolheu PAPEL e você também")
    print("Jogue novamente!")

if jogadapc == 1 and jogada == 0:
    print("A máquina escolheu PAPEL e você PEDRA")
    print("A máquina ganhou!")
    
if jogadapc == 2 and jogada == 0:
    print("A máquina escolheu TESOURA e você PEDRA")
    print("Parabéns! Você ganhou!")

if jogadapc == 2 and jogada == 1:
    print("A máquina escolheu TESOURA e você PAPEL")
    print("Parabéns! Você ganhou!")  
    
if jogadapc == 2 and jogada == 2:
    print("A máquina escolheu TESOURA e você TESOURA")
    print("Jogue Novamente")

print("-="*20)
