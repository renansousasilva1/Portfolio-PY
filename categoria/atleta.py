from datetime import date

ano_atual = date.today().year
ano = int(input("Ano de Nascimento: "))
idade = ano_atual - ano

categoria = ""
if idade <= 9:
    categoria = "Mirim"
    print("Mirim")
    
elif 9 < idade <= 14:  # Condição corrigida aqui
    categoria = "Infantil"  
    print("Infantil")
    
elif 14 < idade <= 19:  # Condição corrigida aqui
    categoria = "Junior"
    print("Junior")
    
elif 19 < idade <= 25:  # Condição corrigida aqui
    categoria = "Sênior"
    print("Sênior")
    
elif idade > 25:
    categoria = "Master"
    print("Master")

print("O atleta tem {} anos e é classificado como {}".format(idade, categoria))
