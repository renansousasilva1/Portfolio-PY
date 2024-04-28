import random
nome1=input("Digite o nome do primeiro aluno(a): ")
nome2=input("Digite o nome do segundo aluno(a): ")
nome3=input("Digite o nome do terceiro aluno(a): ")
nome4=input("Digite o nome do quarto aluno(a): ")

nomes= [nome1, nome2, nome3, nome4]
print("A pessoa selecionada foi: ", random.choice(nomes))