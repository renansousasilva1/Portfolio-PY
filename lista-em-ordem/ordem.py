from random import shuffle
nome1=input("Digite o nome do primeiro aluno(a): ")
nome2=input("Digite o nome do segundo aluno(a): ")
nome3=input("Digite o nome do terceiro aluno(a): ")
nome4=input("Digite o nome do quarto aluno(a): ")
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print("A ordem selecionada foi: ")
print(lista)