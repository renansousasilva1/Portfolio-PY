texto=str(input("Digite uma frase: ")).strip().upper()
palavra =texto.split()
junto =''.join(palavra)
inverso = ''
for letra in range(len(junto)- 1, -1 ,-1):
    inverso += junto [letra]
if inverso == junto:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')   

print("Você digitou a frase {}".format(texto))