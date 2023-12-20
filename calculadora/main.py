from tkinter import *
from tkinter import ttk

    #cores
cor_1 = "#1c1c1c" #preta no fundo
cor_2 = "#ffffff"#Branca para numero
cor_3 = "#3e438a" #Azul
cor_4 = "#828282" #Cinza
cor_5 = "#F28705" # Laranja
cor_6 = "#404040" #cinza escuro

janela = Tk()
janela.title("Calculadora")
janela.geometry("500x460")
janela.config(bg=cor_1)

frame_tela = Frame(janela, width=500, height=100, bg=cor_6) #frame do resultado
frame_tela.grid(row=0, column=0)

frame_tela2 = Frame(janela, width=500, height=400, bg=cor_2) #frame do corpo
frame_tela2.grid(row=1, column=0)

#Função de botão
todos_valores = ""

#CRIANDO LABEL
valor_texto = StringVar()

#Criando função de resultado
def entrar_valor(event):
    
    global todos_valores
    todos_valores = todos_valores + str(event)
    
    #passando valor para a calculadora
    
    valor_texto.set(todos_valores)
    
    #função de calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

#função de limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


app_label = Label(frame_tela, textvariable=valor_texto, width=17, height=2, padx=9, relief=FLAT, anchor="e", justify = RIGHT, font=('Ivy 36 '), bg= cor_6, fg=cor_2)
app_label.place(x=0, y=0)


#Criando Botão

#BOTÃO DE APAGAR
b_1 = Button(frame_tela2, text="CE", command= limpar_tela, width=25, height=3, bg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)


#BOTÃO DE %
b_2 = Button(frame_tela2, command= lambda:entrar_valor("%"), text="%", width=13, height=3, bg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=225, y=0)


#botão de /
b_3 = Button(frame_tela2, command= lambda:entrar_valor("/"), text="/", width=15, height=3, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=370, y=0)


#botão *
b_4 = Button(frame_tela2, command= lambda:entrar_valor("*"), text="*", width=16, height=3, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=370, y=72)


#Botão -
b_5 = Button(frame_tela2, command= lambda:entrar_valor("-"),  text="-", width=15, height=3, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=370, y=144)

#Botão +
b_6 = Button(frame_tela2, command= lambda:entrar_valor("+"), text="+", width=15, height=3, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=370, y=216)

#Botão =
b_7 = Button(frame_tela2, command= calcular, text="=", width=15, height=3, bg=cor_5, fg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=370, y=288)


#BOTÃO DE 9
b_8 = Button(frame_tela2, command= lambda:entrar_valor("9"), text="9", width=13, height=3, bg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=225, y=72)


#BOTÃO DE 6
b_10 = Button(frame_tela2, command= lambda:entrar_valor("6"),  text="6", width=13, height=3, bg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=225, y=144)

#BOTÃO DE 3
b_12 = Button(frame_tela2, text="3", command= lambda:entrar_valor("3"),  width=13, height=3, bg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=225, y=216)

#BOTÃO DE apagar
b_13 = Button(frame_tela2, text="C", width=13, height=3, bg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=225, y=288)



#BOTÃO DE ZERO
b_15 = Button(frame_tela2, command= lambda:entrar_valor("0"), text="0", width=10, height=3, bg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=0, y=288)

#BOTÃO DE 1
b_16 = Button(frame_tela2, command= lambda:entrar_valor("1"), text="1", width=10, height=3, bg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=216)

#BOTÃO QUATRO
b_17 = Button(frame_tela2, command= lambda:entrar_valor("4"), text="4", width=10, height=3, bg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=0, y=144)

#BOTÃO QUATRO
b_18 = Button(frame_tela2, command= lambda:entrar_valor("7"), text="7", width=10, height=3, bg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=0, y=72)


#BOTÃO DE VÍRGULA
b_14 = Button(frame_tela2, command= lambda:entrar_valor(","), text=",", width=10, height=3, bg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=110, y=288)

#BOTÃO DE DOIS
b_19 = Button(frame_tela2, command= lambda:entrar_valor("2"), text="2", width=10, height=3, bg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_19.place(x=110, y=216)

#BOTÃO DE CINCO
b_20 = Button(frame_tela2, command= lambda:entrar_valor("5"), text="5", width=10, height=3, bg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_20.place(x=110, y=144)

#BOTÃO DE OITO
b_21 = Button(frame_tela2, command= lambda:entrar_valor("8"), text="8", width=10, height=3, bg=cor_2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_21.place(x=110, y=72)

janela.mainloop()

