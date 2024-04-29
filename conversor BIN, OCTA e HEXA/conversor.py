numero = int(input("Digite um número que queira converter: "))
print('''escolha uma das bases para converter:
      [ 1 ] converter para BINÁRIO
      [ 2 ] converter para OCTAL
      [ 3 ] converter para HEXADECIMAL''')

opção = int(input("Sua opção: "))
if opção == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(numero, bin(numero)))
if opção ==2:
    print("{} convertido para OCTAL é igual a {}".format(numero, oct(numero)))
if opção == 3:
    print("{} convertido para HEXA é igual a {}".format(numero, hex(numero)))
else:
    print("Opção inválida!")