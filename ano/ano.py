import datetime

ano_input = input("Que ano você quer analisar? Coloque 'atual' para o Ano Atual: ")

# Verificar se o input é "Atual" ou numérico
if ano_input.lower() == "atual":
    ano = datetime.date.today().year
elif ano_input.isdigit():  # Verificar se o input é numérico
    ano = int(ano_input)
else:
    print("Por favor, insira um ano válido ou 'Atual' para o ano atual.")
    exit()

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))
