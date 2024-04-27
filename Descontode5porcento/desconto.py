preco=float(input("Qual é o preço do produto? R$"))
desconto = preco*0.05
valorfinal=preco-desconto

print("O produto que custava R${}, na promoção com dsconto de 5%, vai custar R$ {:.2f}".format(preco, valorfinal))
