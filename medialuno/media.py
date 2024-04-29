nota1=float(input("Digite a 1° nota: "))
nota2=float(input("Digite a 2° nota: "))
nota3=float(input("Digite a 3° nota: "))
nota4=float(input("Digite a 4° nota: "))

media = nota1+nota2+nota3+nota4
mediafinal= media/4

if mediafinal > 8:
    print("A nota do aluno foi {} e o aluno foi aprovado".format(mediafinal))
    
else:
    print("A nota do aluno foi {} e o aluno foi reprovado".format(mediafinal))