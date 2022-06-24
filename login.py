from tkinter import *
from g_tela import TelaGerente
from r_tela import TelaRecepcionista
from m_tela import TelaMecanico
from db_funcionarios import Funcionarios


class Login:
    def __init__(self):
        # definindo tabela
        self.db = Funcionarios("banco/funcionarios.db")

        # Cores e fontes
        self.cor1 = "#800000"
        self.cor2 = "#FFFFFF"  # Branco
        self.cor3 = "#000000"  # Preto
        self.fonte = "roboto"

        # Janela
        self.janela = Tk()
        self.janela.title("Login")
        self.janela.geometry("500x500")
        self.janela.resizable(False, False)
        self.janela.configure(bg=self.cor1)

        # Logo
        self.logo = Label(self.janela, text="LOGO", font=("bold", 50), bg=self.cor1, fg=self.cor3)
        self.logo.place(x=150, y=80)

        # Campo nome
        self.nome_lb = Label(self.janela, text="Nome:", font=(self.fonte, 10), bg=self.cor1, fg=self.cor2)
        self.nome_lb.place(x=150, y=200)
        self.nome_en = Entry(self.janela, width=30, relief=FLAT)
        self.nome_en.place(x=153, y=225)

        # Campo senha
        self.senha_lb = Label(self.janela, text="Senha:", font=(self.fonte, 10), bg=self.cor1, fg=self.cor2)
        self.senha_lb.place(x=150, y=255)
        self.senha_en = Entry(self.janela, width=30, relief=FLAT, show="*")
        self.senha_en.place(x=153, y=280)

        # Botão entrar
        self.entrar = Button(self.janela, text="Entrar", width=15, relief=FLAT, command=self.login)
        self.entrar.place(x=190, y=330)

        mainloop()

    def login(self):
        nome = self.nome_en.get()
        senha = self.senha_en.get()
        global tela
        if nome == "adm" and senha == "123":
            tela = TelaGerente()
        if nome == "recep" and senha == "123":
            tela = TelaRecepcionista()
        if nome == "mec" and senha == "123":
            tela = TelaMecanico()


tela = Login()
