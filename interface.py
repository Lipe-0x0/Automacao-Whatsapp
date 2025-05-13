from tkinter import *
from tkinter import ttk

lista_contatos_errados={}
lista_contatos_real={}
entry_perg=""
msg=""
count=0


#---------------------------------EXPLICAR A MECANICA (SOBRE)---------------------------------

# BOTÃO "SOBRE" MENSAGEM
def sob_msg():
    global whats_ico
    sob=Tk()
    sob.configure(bd=4,highlightbackground="#86b8b1",highlightthickness=3,background="#15212a")
    sob.geometry("500x350+570+250")
    sob.iconbitmap("imagens/imagens/whatsapp.ico")
    sob.title("Automação Whatsapp")

    inf_nome=Label(sob,text="Nome:",fg="#009003",font=("arial",12,"bold"),)
    inf_nome.place(relx=0.15,rely=0.2)
    inf_cont=Label(sob,text="Contato:",fg="#009003",font=("arial",12,"bold"))
    inf_cont.place(relx=0.15,rely=0.4)
    inf_msg=Label(sob,text="Mensagem:",fg="#009003",font=("arial",12,"bold"))
    inf_msg.place(relx=0.15,rely=0.6)

    sob.mainloop()

# BOTÃO "SOBRE" ARQUIVO    
def sob_arq():
    sob=Tk()
    sob.geometry("500x350+570+250")
    sob.iconbitmap("imagens/imagens/whatsapp.ico")
    sob.title("Automação Whatsapp")
    sob.mainloop()

#---------------------------------CAIXA P/ PÔR A MENSAGEM E FINALIZAR---------------------------------

def frase():
    fra=Tk()
    fra.configure(background="White")
    fra.attributes("-alpha",1)
    fra.geometry("500x130+680+300")
    fra.iconbitmap("imagens/imagens/whatsapp.ico")
    fra.title("Automação Whatsapp")

    label_fra=Label(fra,text="Insira a mensagem",anchor="center",font=("arial",12))
    label_fra.place(relx=0.35,rely=0.1,relheight=0.15)
    entry_fra=Entry(fra)
    entry_fra.place(relx=0.15,rely=0.4,relwidth=0.7)

    def zap():
        msg=entry_fra.get()
        fra.destroy()

        import pyautogui
        import pyperclip
        import time

        pyautogui.PAUSE=2
        pyautogui.hotkey("Win")
        pyautogui.write("Chrome")
        pyautogui.hotkey("Enter")
        pyautogui.click(x=964, y=601)
        pyautogui.click(x=978, y=84)
        pyautogui.write("https://web.whatsapp.com/")
        pyautogui.hotkey("enter")
        time.sleep(28)
        for i in lista_contatos_real:
            pyautogui.hotkey("ctrl","alt","s")
            pyautogui.click(x=960, y=567)
            pyautogui.write(lista_contatos_real[i])
            pyautogui.hotkey("enter")
            pyautogui.useImageNotFoundException()
            try: 
                botao_erro_location = pyautogui.locateOnScreen("imagens/imagens/botao erro zapp.png")
            except pyautogui.ImageNotFoundException:
                botao_erro_location=None
            if botao_erro_location!=None:
                pyautogui.click(botao_erro_location[0],botao_erro_location[1])
                lista_contatos_errados[i]=lista_contatos_real[i]
                print(lista_contatos_errados)
                pass
            else:
                pyautogui.click(x=1126, y=954)
                pyperclip.copy(msg)
                pyautogui.hotkey("ctrl","v")
                pyautogui.press("Enter")

           

    lemon=Button(fra,command=zap,text="ENVIAR",bd=3,bg="#31a842",font=("verdana",8,"bold"))
    lemon.place(relx=0.43,rely=0.65)

#---------------------------------CAIXA CADASTRAR CONTATOS "SIM OU NAO"---------------------------------

def sim_nao():
    s_n=Tk()
    s_n.configure(background="White")
    s_n.attributes("-alpha",1)
    s_n.geometry("300x150+680+300")
    s_n.iconbitmap("imagens/imagens/whatsapp.ico")
    s_n.title("Automação Whatsapp")

    # FUNÇÃO "SIM"
    def si():
       s_n.destroy()
       pergunta()
    # FUNÇÃO NÃO
    def sair():
        s_n.destroy()

    label_s_n=Label(s_n,text="Cadastrar novos contatos?",anchor="center")
    label_s_n.place(relx=0.25,rely=0.1,relheight=0.1)

    # BOTÕES DE SIM E NÃO
    s=Button(s_n,command=si,text="SIM",bd=3,bg="#31a842",font=("verdana",8,"bold"))
    n=Button(s_n,command=sair,text="NÃO",bd=3,bg="#31a842",font=("verdana",8,"bold"))
    s.place(relx=0.35,rely=0.5)
    n.place(relx=0.5,rely=0.5)

    s_n.mainloop()

#---------------------------------CAIXA PERGUNTA---------------------------------

def pergunta():
    global entry_perg
    perg=Tk()
    perg.configure(background="White")
    perg.attributes("-alpha",1)
    perg.geometry("300x150+680+300")
    perg.iconbitmap("imagens/imagens/whatsapp.ico")
    perg.title("Automação Whatsapp")

    label_perg=Label(perg,text="Quantos Contatos quer adicionar?",anchor="center")
    label_perg.place(relx=0.2,rely=0.1,relheight=0.1)
    entry_perg=Entry(perg)
    entry_perg.place(relx=0.45,rely=0.25,relwidth=0.1)
    
    # FUNÇÃO "OK" P/ SABER QUANTIDADE DE USUÁRIOS
    def ok():
        global entry_perg
        entry_perg=int(entry_perg.get())
        perg.destroy()
        mensagem()

    botao_perg=Button(perg,command=ok,text="OK",bd=3,bg="#31a842",font=("verdana",8,"bold"))
    botao_perg.place(relx=0.45,rely=0.6)
    
    perg.mainloop()

#---------------------------------TELA ENVIAR MENSAGEM---------------------------------

def mensagem():
    tela_msg=Tk()
    tela_msg.configure(background="#31a842")
    tela_msg.geometry("800x500+400+200")
    tela_msg.iconbitmap("imagens/imagens/whatsapp.ico")
    tela_msg.title("Automação Whatsapp")

    # CRIANDO FRAME P/ ENVIAR MENSAGEM
    frame_env=Frame(tela_msg,bd=4,highlightbackground="#86b8b1",highlightthickness=3)
    frame_env.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)
    lab=Label(frame_env,text="ENVIAR MENSAGEM")
    lab.pack()


    # CRIANDO ENTRADA DE NOME
    nome=Label(frame_env,text="Nome",fg="#009003")
    nome.place(relx=0.3,rely=0.15)
    entrada_nome=Entry(frame_env,width=20,font=("arial 10"))
    entrada_nome.place(relx=0.3,rely=0.19,relwidth=0.5)

    # CRIANDO ENTRADA DE CONTATO
    contato=Label(frame_env,text="Contato",fg="#009003")
    contato.place(relx=0.3,rely=0.28)
    entrada_cont=Entry(frame_env,width=20,font=("arial 10"))
    entrada_cont.place(relx=0.3,rely=0.32,relwidth=0.3)
            
    # FUNÇÃO DO BOTÃO "CONFIRMAR"
    def lista():
        global lista_contatos_real
        global entry_perg
        global count
        while entry_perg!=0:
            count+=1
            lista_contatos={}
            lista_contatos[entrada_nome.get()]=entrada_cont.get()
            lista_contatos_real[entrada_nome.get()]=entrada_cont.get()

            nomes=lista_contatos.keys()
            nomes=list(nomes)
            contato=lista_contatos.values()
            contato=list(contato)
            for i in range(len(lista_contatos)):
                treeview.insert("",END,values=(count,nomes[i],contato[i]))
            entry_perg-=1
            tela_msg.destroy()
            if entry_perg!=0:
                mensagem()

    # FUNÇÃO DE LIMPAR CONTATO
    def limp_cont():
        entrada_cont.delete(0,END)
    # FUNÇÃO DE LIMPAR NOME
    def limp_nome():
        entrada_nome.delete(0,END)

    # BOTÃO CONFIRMAR EM ENVIAR MENSAGEM    
    conf=Button(tela_msg,text="Confirmar",command=lista,bd=3,bg="#31a842",font=("verdana",8,"bold"))
    conf.place(relx=0.45,rely=0.5)
    # BOTÃO LIMPAR NOME
    bot_limp_nome=Button(frame_env,text="Limpar",command=limp_nome,bd=3,bg="#31a842",font=("verdana",8,"bold"))
    bot_limp_nome.place(relx=0.81,rely=0.18)
    # BOTÃO LIMPAR CONTATO
    bot_limp_cont=Button(frame_env,text="Limpar",command=limp_cont,bd=3,bg="#31a842",font=("verdana",8,"bold"))
    bot_limp_cont.place(relx=0.61,rely=0.31)

    tela_msg.mainloop()

#---------------------------------TELA ENVIAR ARQUIVO-----------------------------------

def diretorio():
    tela_dic=Tk()
    tela_dic.configure(background="White")
    tela_dic.attributes("-alpha",1)
    tela_dic.geometry("500x130+680+300")
    tela_dic.iconbitmap("imagens/imagens/whatsapp.ico")
    tela_dic.title("Automação Whatsapp")

    label_dic=Label(tela_dic,text="Insira o caminho do arquivo",anchor="center",font=("arial",12))
    label_dic.place(relx=0.3,rely=0.1,relheight=0.15)
    entry_dic=Entry(tela_dic)
    entry_dic.place(relx=0.15,rely=0.4,relwidth=0.7)

    def arquivo():
        arq=entry_dic.get()
        caminho=""
        nome_arq=""
        contagem_de_barra=arq.count("/")
        cont=0
        for i in arq:
            if i=="/":
                cont+=1
            if cont!=contagem_de_barra:
                caminho+=i
            if cont==contagem_de_barra:
                nome_arq+=i
        nome_arq=nome_arq.strip("/")
            
        tela_dic.destroy()

        import pyautogui
        import pyperclip
        import time

        pyautogui.PAUSE=2
        pyautogui.hotkey("Win")
        pyautogui.write("Chrome")
        pyautogui.hotkey("Enter")
        pyautogui.click(x=964, y=601)
        pyautogui.click(x=978, y=84)
        pyautogui.write("https://web.whatsapp.com/")
        pyautogui.hotkey("enter")
        time.sleep(28)
        for i in lista_contatos_real:
            pyautogui.hotkey("ctrl","alt","s")
            pyautogui.click(x=960, y=567)
            pyautogui.write(lista_contatos_real[i])
            pyautogui.hotkey("enter")
            pyautogui.useImageNotFoundException()
            try: 
                botao_erro_location = pyautogui.locateOnScreen("imagens/imagens/botao erro zapp.png")
            except pyautogui.ImageNotFoundException:
                botao_erro_location=None
            if botao_erro_location!=None:
                pyautogui.click(botao_erro_location[0],botao_erro_location[1])
                lista_contatos_errados[i]=lista_contatos_real[i]
                print(lista_contatos_errados)
                pass
            else:
                botao_adi_location=pyautogui.locateOnScreen("imagens/imagens/botao documento adicionar.png")
                pyautogui.click(botao_adi_location[0],botao_adi_location[1])
                botao_doc_location=pyautogui.locateOnScreen("imagens/imagens/botao documento zapp.png")
                pyautogui.click(botao_doc_location[0],botao_doc_location[1])
                pyautogui.click(x=203, y=65)
                pyperclip.copy(caminho)
                pyautogui.hotkey("ctrl","v")
                pyautogui.hotkey("ctrl","f")
                pyperclip.copy(nome_arq)
                pyautogui.hotkey("ctrl","v")
                pyautogui.doubleClick(x=370, y=226)
                pyautogui.press("enter")

    
    botao_env_arq=Button(tela_dic,command=arquivo,text="Enviar",bd=3,bg="#31a842",font=("verdana",8,"bold"))
    botao_env_arq.place(relx=0.45,rely=0.6)


            

#---------------------------------TELA PRINCIPAL---------------------------------

# CRIANDO TELA DE INTERFACE (PRINCIPAL)
tela=Tk()
tela.configure(background="#31a842")
tela.title("Automação Whatsapp")
tela.geometry("800x500+400+200")
tela.attributes("-alpha",1)
tela.iconbitmap("imagens/imagens/whatsapp.ico")

# CRIANDO FRAMES NA TELA PRINCIPAL
frame=Frame(tela,bd=4,highlightbackground="#86b8b1",highlightthickness=3,background="#15212a")
frame.place(relx=0.05,rely=0.02,relheight=0.45,relwidth=0.9)

frame2=Frame(tela,bd=4,highlightbackground="#86b8b1",highlightthickness=3,background="#15212a")
frame2.place(relx=0.05,rely=0.48,relheight=0.5,relwidth=0.9)

frame_msg=Frame(frame,bd=4,highlightbackground="#86b8b1",highlightthickness=3,takefocus=0.5)
frame_msg.place(relx=0.002,rely=0.05,relheight=0.9,relwidth=0.5)
Label(frame_msg,text="ENVIAR MENSAGEM").pack()

frame_arq=Frame(frame,bd=4,highlightbackground="#86b8b1",highlightthickness=3,takefocus=0.5)
frame_arq.place(relx=0.519,rely=0.05,relheight=0.9,relwidth=0.48)
Label(frame_arq,text="ENVIAR ARQUIVO").pack()

# BOTÃO DE EXPLICAR NA TELA PRINCIPAL (FRAME 1)
sob=Button(frame_msg,text="Sobre",command=sob_msg,bd=3,bg="#31a842",font=("verdana",8,"bold"))
sob.place(relx=0.42,rely=0.6,relwidth=0.15)
sob=Button(frame_arq,text="Sobre",command=sob_arq,bd=3,bg="#31a842",font=("verdana",8,"bold"))
sob.place(relx=0.42,rely=0.6,relwidth=0.15)
# BOTÃO DE ENVIAR MENSAGEM NA TELA PRINCIPAL
men=Button(frame_msg,text="Enviar",command=frase,bd=3,bg="#31a842",font=("verdana",8,"bold"))
men.place(relx=0.42,rely=0.2,relwidth=0.15)
men_cont=Button(frame_msg,text="Inserir Contatos",command=sim_nao,bd=3,bg="#31a842",font=("verdana",8,"bold"))
men_cont.place(relx=0.32,rely=0.4,relwidth=0.35)
# BOTÃO DE ENVIAR ARQUIVO NA TELA PRINCIPAL
arq=Button(frame_arq,text="Enviar",command=diretorio,bd=3,bg="#31a842",font=("verdana",8,"bold"))
arq.place(relx=0.42,rely=0.2,relwidth=0.15)
arq_cont=Button(frame_arq,text="Inserir Contatos",command=sim_nao,bd=3,bg="#31a842",font=("verdana",8,"bold"))
arq_cont.place(relx=0.32,rely=0.4,relwidth=0.35)
# CRIANDO TREEVIEW NA TELA PRINCIPAL (FRAME 2)
treeview=ttk.Treeview(frame2,columns=("col1","col2","col3"))
treeview.heading("#0",text="")
treeview.heading("#1",text="ID")
treeview.heading("#2",text="Nome")
treeview.heading("#3",text="Contato")

treeview.column("#0",width=1)
treeview.column("#1",width=1)
treeview.column("#2",width=200)
treeview.column("#3",width=100)


treeview.place(relx=0.002,rely=0.01,relheight=0.98,relwidth=0.958)

scroll=Scrollbar(frame2,orient="vertical")
treeview.configure(yscroll=scroll)
scroll.place(relx=0.96,rely=0.01,relheight=0.98,relwidth=0.043)

tela.mainloop()

print(lista_contatos_real)