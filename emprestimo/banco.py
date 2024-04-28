valor1=float(input("Qual o valor da casa? "))
salario = float(input("Qual o salário do comprador? "))
tempo = int(input("Quantos anos de financiamento? "))

tempo2 = tempo*12
parcela= valor1/tempo2

limite = salario * 0.30

if parcela > limite:
    print("Emprestimo negado")
else:
    print("Emprestimo concedido! O montante da prestação mensal é de R${:.2f}. ".format(parcela))
    