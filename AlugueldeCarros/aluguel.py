aluguel = int(input("Por quantos dias o carro foi alugado? "))
km= float(input("Quantos km rodados? "))
precodia = aluguel*60
precokm = km*0.15
precofinal = precodia + precokm

print("O Total a pagar é de R$", precofinal)

