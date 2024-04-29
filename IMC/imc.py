peso=float(input("Insira o seu peso (KG): "))
altura = float(input("Qual a sua altura(cm)? "))
imc = peso / (altura **2)
print("O imc desta pessoa é de {:.1f}.".format(imc), end=' ')

if imc <=18.5:
    print("Ela está abaixo do peso")

elif 18.5 <  imc <= 24.9:
       print("Ela está no seu peso ideal")
       
elif 25 < imc <= 30:
    print("Ela está com sobrepeso")
    
elif 30 < imc <=40:
    print("Ela está com obesidade")
    
elif imc >= 40 :
    print("Ela está com uma obesidade mórbida e precisa emagrecer!")

