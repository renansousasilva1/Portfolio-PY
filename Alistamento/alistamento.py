from datetime import date

sexo=input("Digite o seu sexo: ")
if sexo.lower() == "feminino":
    print("Você não precisa se alistar")

elif  sexo.lower() == "Feminino":
    print("Você não precisa se alistar")
    
else:
    ano_atual = date.today().year
    ano=int(input("Digite o ano de nascimento: "))
    idade =  ano_atual - ano
    print("Quem nasceu em {} tem {} anos de idade. ".format(ano, idade ))

    if idade == 18:
        print("Você deve alistar-se imediatamente!")
    
    elif idade < 18:
        tempo = 18 - idade
        print("Ainda faltam {} anos para você se alistar." .format(tempo) )
        print("Seu alistamento será em {}".format(2023 + tempo) )
    
    elif idade > 18:
        tempo = idade - 18
        print("O candidato tem {} anos e deveria se alistar há {} anos atrás".format(idade, tempo))
        print("O ano do seu alistamento foi {}".format(ano_atual - tempo))