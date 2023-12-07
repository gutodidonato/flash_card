from tkinter import *
import pandas as pd
import random as r
import time
#Pandas--------------------------------------------------------------------#
data = pd.read_csv("data/ingles-pt-cor.csv")
leitura = data.to_dict(orient="records")
#virou lista



#----------------------verificar txt------------------------------------------#
def leitura_de_dados():
    try:
        with open("textos/pontos.txt", "r") as file:
            print(file.load())
    except FileNotFoundError:
        with open("textos/pontos.txt", "w+") as file:
            print("Arquivo criado")
    

        

#variaveis-------------------------------------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
valor_palavra = ""

#Lógica -------------------------------------------------------------------#
def trocar_logica():
    global valor_palavra
    lingua_padrao = lingua_var.get()
    palavra = r.choice(leitura)
    valor_palavra = palavra
    if lingua_padrao == "lingua coreana":
        canvas.itemconfig(lingua, text=lingua_padrao)
        canvas.itemconfig(termo, text=palavra["Coreano"])
    else:
        canvas.itemconfig(lingua, text=lingua_padrao)
        canvas.itemconfig(termo, text=palavra["English"])

def escolher_opcao():
    window.after(3000, mostrar_resultado, valor_palavra)
    
    
def mostrar_resultado(dicionario):
        canvas.itemconfig(frente, image=carta_tras)
        canvas.itemconfig(lingua, text="Portuguesa")
        canvas.itemconfig(termo, text=dicionario["portugues"])
        window.after(3000, voltar_ao_padrao)

def voltar_ao_padrao():
    canvas.itemconfig(frente, image=carta_frente)
    trocar_logica()
    
#Interface Gráfica-------------------------------------------------------------------#
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
carta_frente = PhotoImage(file="images/card_front.png")
carta_tras = PhotoImage(file="images/card_back.png")
frente = canvas.create_image(400, 263 ,image=carta_frente)
lingua = canvas.create_text(400, 150, text="Lingua", font=("ariel", 40, "italic"))
termo = canvas.create_text(400, 263, text="Termo", font=("ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=3)

negacionar = PhotoImage(file="images/wrong.png")
negar = Button(highlightthickness=0, image=negacionar, command=escolher_opcao)
negar.grid(row=1, column=0)


lingua_frame = Frame(background=BACKGROUND_COLOR, highlightthickness=0)
lingua_frame.grid(row=1, column=1)
lingua_var = StringVar()  
lingua_var.set("lingua inglesa")
lingua1 = Radiobutton(lingua_frame, text="Coreano", variable=lingua_var, value="lingua coreana")
lingua2 = Radiobutton(lingua_frame, text="Inglês", variable=lingua_var, value="lingua inglesa")
lingua1.grid(row=0, column=0)
lingua2.grid(row=1, column=0)


concordar = PhotoImage(file="images/right.png")
aceitar = Button(highlightthickness=0, image=concordar, command=escolher_opcao)
aceitar.grid(row=1, column=2)

trocar_logica()
window.mainloop()
