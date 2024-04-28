salariobase=float(input("Qual o salário do funcionário? "))
aumento1 = salariobase*0.15
aumento2 = salariobase*0.10

if salariobase >= 1251:
    print("Quem ganhava R${} passa a ganhar R${:.2f} agora".format(salariobase, salariobase+aumento2))
    
else:
    print("Quem ganhava R${} passa a ganhar R${:.2f} agora".format(salariobase, salariobase+aumento1))