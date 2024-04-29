from colorama import init, Fore
init()
print("=="*11, end=' ')
print("Supermercado Exemplo", end=' ')
print("=="*11, end='')
print(" ")
compra = float(input(Fore.GREEN + "Digite o valor da compra: R$ " +Fore.RESET))
print("FORMAS DE PAGAMENTO:")
print(''' 
      [1] à vista dinheiro/pix
      [2] à vista no cartão de crédito
      [3] à vista  no débito
      [4] 2x no cartão
      [5] 3x ou mais no cartão
      ''')
opção = int(input ("Qual é a opção? "))
if opção == 1:
    desconto = compra *0.10
    print("Sua compra de R$ {} vai custar {} no final".format(compra, compra - desconto))

elif opção == 2:
    print("Sua compra de R$ {} vai custar {:.2f} no cartão de crédito". format(compra, compra)) 
    
elif opção == 3:
    print("Sua compra de R$ {} vai custar {:.2f} no cartão de débito".format (compra, compra))   

elif  opção == 4:
    parcela = compra /  2
    print("Sua compra de R${:.2f} será dividida em duas parcelas de R$ {:.2f} cada.".format(compra, parcela))
    
elif opção == 5:
    parcelas  = int(input("Quantas parcelas? "))
    juros = parcelas + compra * 0.12
    compra_final = juros * parcelas
    print("Sua compra será parcelada em {}x de R${} COM JUROS".format(parcelas, juros))
    print("Sua compra de R${} vai custar R${} no final".format(compra, compra_final))