# Código Python

import pymysql
from pymysql import*
from tkinter import*
from tkinter import messagebox
from tkinter import ttk


conexao = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="eleicoes",
    cursorclass=pymysql.cursors.DictCursor
)
cursor = conexao.cursor()


cor1 = "#000000"  #pretin
cor2 = "#ffffff"  #brankin
cor3 = "#c7bebd"  #cinza
cor4 = "#eb280e"  #laranja
cor5 = "#121212"  #cinzin


janela = Tk()
janela.title("Urna Eletrônica")
janela.geometry("1000x600")
valor_texto = StringVar()


#Frames da tela
frame_maquina = Frame(janela, width=1000, height=600, bg="#c7bebd")
frame_maquina.place(x=0, y=0)
frame_tela = Frame(janela, width=500, height=400)
frame_tela.place(x=50, y=100)
visor_numeros = Label(frame_tela, font="calibri 30", textvariable=valor_texto)
visor_numeros.place(x=100, y=175)

frame_corpo = Frame(janela, width=300, height=245, bg=cor1)
frame_corpo.place(x=600, y=150)


#funcões
numeros = ""

def exibir(num):
    global numeros
    numeros = numeros + num
    valor_texto.set(numeros)



def confirmar():

    numero_candidato = valor_texto.get()

    if numero_candidato == "13":
        sql = "insert into urna (voto) values (%s)"
        cursor.execute(sql,(numero_candidato))
        conexao.commit()

    if numero_candidato == "22":
        sql = "insert into urna (voto) values (%s)"
        cursor.execute(sql,(numero_candidato))
        conexao.commit()

    else:
        sql = "insert into urna (voto) values (%s)"
        cursor.execute(sql, ("nulo"))
        conexao.commit()


def apagar():
    global numeros
    valor_texto.set("")
    numeros = ""

def branco():
    sql = "insert into urna (voto) values (%s)"
    cursor.execute(sql, "branco")
    conexao.commit()


#botões
b1 = Button(frame_corpo, text="1", fg="white" ,width="10", height="2", bg=cor5, command=lambda: exibir("1"))
b1.place(x=5, y=5)

b2 = Button(frame_corpo, text="2", fg="white", width="10", height="2", bg=cor5, command=lambda: exibir("2"))
b2.place(x=100, y=5)
#
b3 = Button(frame_corpo, text="3", fg="white", width="10", height="2", bg=cor5, command=lambda: exibir("3"))
b3.place(x=200, y=5)

b4 = Button(frame_corpo, text="4", fg="white", width="10", height="2", bg=cor5, command=lambda: exibir("4"))
b4.place(x=5, y=50)
#
b5 = Button(frame_corpo, text="5", fg="white", width="10", height="2", bg=cor5, command=lambda: exibir("5"))
b5.place(x=100, y=50)
#
b6 = Button(frame_corpo, text="6", fg="white", width="10", height="2", bg=cor5, command=lambda: exibir("6"))
b6.place(x=200, y=50)
#
b7 = Button(frame_corpo, text="7", fg="white", width="10", height="2", bg=cor5, command=lambda: exibir("7"))
b7.place(x=5, y=95)
#
b8 = Button(frame_corpo, text="8", fg="white", width="10", height="2", bg=cor5, command=lambda: exibir("8"))
b8.place(x=100, y=95)
#
b9 = Button(frame_corpo, text="9", fg="white", width="10", height="2", bg=cor5, command=lambda: exibir("9"))
b9.place(x=200, y=95)
#
b0 = Button(frame_corpo, text="0", fg="white", width="10", height="2", bg=cor5, command=lambda: exibir("0"))
b0.place(x=100, y=140)
#
bcv = Button(frame_corpo, text="Confirma", width="12", height="3", bg="green", command=lambda: confirmar())
bcv.place(x=200, y=187)

bcl = Button(frame_corpo, text="Corrige", width="12", height="2", bg=cor4, command=lambda:apagar())
bcl.place(x=100, y=191)

bcb = Button(frame_corpo, text="Branco", width="12", height="2", bg="white", command=lambda:branco())
bcb.place(x=3, y=191)



janela.mainloop()