maioridade = 0
nomevelho = ''
total_mulhersub20 = 0
for p in range (1, 5):
    print("----- {}° Pessoa  -----".format(p))
    nome = str(input(f'Digite o nome: '))
    idade = int(input("Digite a idade: "))
    sexo =  str(input('Digite [M] para masculino ou [F] para feminino: ')).upper()
    print("Nome: {}".format(nome))
    print("Idade: {} anos".format(idade))
    print("SEXO: [M/F]: {}".format(sexo))
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulhersub20 += 1
    
soma = idade*4
media = soma/4
print("A média de idade do grupo é de {} anos ".format(media))
print("O homem mais velho tem {} anos e se chama {}".format(maioridade, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos de idade".format(total_mulhersub20))