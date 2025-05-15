from tkinter import *
from tkinter import ttk
from janelas import Janela

class Zapp:
    def __init__(self):
        self.tela = Tk()
        self.tela.configure(background="#31a842")
        self.tela.title("Automação Whatsapp")
        self.tela.geometry("800x500+400+200")
        self.tela.attributes("-alpha",1)
        self.tela.iconbitmap("imagens/whatsapp.ico")
        self.tela.resizable(False,False)

    def janela(self):
        self.frame1 = Janela(self.tela,comp= 0.9,alt=0.5,pos_x=0.05,pos_y=0.48 ,
                             cor_borda="#86b8b1", larg_borda=3, cor_fundo="#15212a")

    def iniciar(self):
        self.janela()
        self.tela.mainloop()


Zapp().iniciar()