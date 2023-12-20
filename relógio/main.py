from tkinter import *
from datetime import datetime
import locale

import pyglet
pyglet.font.add_file("digital-7.ttf")

def atualizar_tempo():
    tempo_agora = datetime.now()
    hora = tempo_agora.strftime("%H:%M:%S")
    dia_semana = tempo_agora.strftime("%A").capitalize()

    dia = tempo_agora.day
    mes = tempo_agora.strftime("%b")
    ano = tempo_agora.strftime("%Y")
    
    label_hora.config(text=hora)
    label_dia_semana.config(text=f"{dia_semana}, {dia}/{mes}/{ano}")

    # Chama a função novamente após 1000 milissegundos (1 segundo)
    Janela.after(1000, atualizar_tempo)

if __name__ == "__main__":
    locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

    cor_1 = "#1c1c1c" #preta no fundo
    cor_2 = "#ffffff"#Branca para numero
    cor_3 = "#3e438a" #Azul
    cor_4 = "#292929" #Cinza
    cor_5 = "#F28705" # Laranja
    cor_6 = "#404040" #cinza escuro
    cor_7 = "#eb4034" #vermelho
    
    
    Janela = Tk()
    Janela.title("Relógio")
    Janela.geometry("450x200")
    Janela.resizable(width=FALSE, height=FALSE)
    Janela.configure(bg=cor_4)

    label_hora = Label(Janela, font=("digital-7", 102), fg=cor_7, bg=cor_4)
    label_hora.grid(row=0, column=0, sticky=NW, padx=5)

    label_dia_semana = Label(Janela, font=("digital-7", 25), fg=cor_7, bg=cor_4)
    label_dia_semana.grid(row=1, column=0, sticky=NW, padx=5)

    # Chama a função para iniciar o loop de atualização
    atualizar_tempo()

    Janela.mainloop()
