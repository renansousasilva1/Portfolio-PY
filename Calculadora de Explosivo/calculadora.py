def calcular_carga_explosiva(porta, explosivo):
    #Tabela de explosivos
    cargas={
        'Madeira':{'tnt': 1000, 'petn':800, 'c4':700},
        'Aço': {'tnt': 1500, 'petn':1300, 'c4':1000},
        'Ferro': {'tnt':2000,'petn':1600,'c4':1400},
        'Alumínio':{'tnt':800, 'petn':600, 'c4':500}
    }

#Verificador de tipo de porta
    if porta in cargas and explosivo in cargas[porta]:
        carga=cargas[porta][explosivo]
        return carga

    else:
        return print("Porta ou Explosivo não encontrado")
    
porta = input("Escolha o tipo de porta que deseja explodir: (Madeira, Aço, Alumínio ou Ferro)")
explosivo= input("Escolha qual o tipo de explosivo (tnt, petn ou c4):")

carga = calcular_carga_explosiva(porta,explosivo)
if carga is not None:
    print("-------------------------------------")
    print("Tabela de carga explosiva:")
    print(" ")
    print("A carga explosiva necessária para explodir uma porta de {} usando o explosivo {} é de {} gramas".format(porta,explosivo,carga))
    print(" ")
    print("-------------------------------------")
    
else:
    print("Porta ou explosivo inválido. Tente novamente.")
    
    