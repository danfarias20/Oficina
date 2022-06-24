from tkinter import *
from tkinter import ttk
from db_funcionarios import Funcionarios


class GerFuncionarios:
    def __init__(self):
        # Definindo a tabela
        self.db = Funcionarios("banco/funcionarios.db")

        # Cores e fontes
        self.cor1 = "#800000"
        self.cor2 = "#FFFFFF"  # Branco
        self.cor3 = "#000000"  # Preto
        self.cor4 = "#A52A2A"
        self.fonte = "roboto"

        # Janela
        self.janela = Tk()
        self.janela.title("Gerenciamento de funcionários")
        self.janela.geometry("1200x600")
        self.janela.resizable(False, False)

        # Variáveis
        self.nome = StringVar()
        self.senha = StringVar()
        self.cpf = StringVar()
        self.cargo = StringVar()
        self.id = StringVar()

        # Frames
        self.f1 = Frame(self.janela, width=400, height=60, bg=self.cor1)
        self.f1.grid(row=0, column=0)
        self.f2 = Frame(self.janela, width=800, height=60, bg=self.cor1)
        self.f2.grid(row=0, column=1)
        self.f3 = Frame(self.janela, width=400, height=540, bg=self.cor4)
        self.f3.grid(row=1, column=0)
        self.f4 = Frame(self.janela, width=800, height=540)
        self.f4.grid(row=1, column=1)

        # Título
        self.titulo = Label(self.f1, text="Gerenciamento de funcionários", font=("bold", 15), bg=self.cor1,
                            fg=self.cor2)
        self.titulo.place(x=10, y=15)

        # Campo nome
        self.nome_lb = Label(self.f3, text="Nome:", font=("bold", 15), bg=self.cor4, fg=self.cor2)
        self.nome_lb.place(x=10, y=20)
        self.nome_en = Entry(self.f3, width=40, relief=FLAT, textvariable=self.nome, font=15)
        self.nome_en.place(x=13, y=55)

        # Campo senha
        self.senha_lb = Label(self.f3, text="Senha:", font=("bold", 15), bg=self.cor4, fg=self.cor2)
        self.senha_lb.place(x=10, y=90)
        self.senha_en = Entry(self.f3, width=40, relief=FLAT, textvariable=self.senha, font=15)
        self.senha_en.place(x=13, y=125)

        # Campo cpf
        self.cpf_lb = Label(self.f3, text="CPF:", font=("bold", 15), bg=self.cor4, fg=self.cor2)
        self.cpf_lb.place(x=10, y=160)
        self.cpf_en = Entry(self.f3, width=40, relief=FLAT, textvariable=self.cpf, font=15)
        self.cpf_en.place(x=13, y=195)

        # Campo cargo
        self.cargo_lb = Label(self.f3, text="Cargo:", font=("bold", 15), bg=self.cor4, fg=self.cor2)
        self.cargo_lb.place(x=10, y=230)
        self.cargo_en = Entry(self.f3, width=40, relief=FLAT, textvariable=self.cargo, font=15)
        self.cargo_en.place(x=13, y=265)

        # Botão cadastrar
        self.cadastrar_btn = Button(self.f3, text="Cadastrar", width=10, font=("bold", 15), relief=FLAT, bg=self.cor2,
                                    fg=self.cor4, command=self.cadastrar)
        self.cadastrar_btn.place(x=50, y=315)

        # Botão editar
        self.editar_btn = Button(self.f3, text="Editar", width=10, font=("bold", 15), relief=FLAT, bg=self.cor2,
                                 fg=self.cor4, command=self.editar)
        self.editar_btn.place(x=50, y=370)

        # Botão remover
        self.remover_btn = Button(self.f3, text="Remover", width=10, font=("bold", 15), relief=FLAT, bg=self.cor2,
                                  fg=self.cor4, command=self.remover)
        self.remover_btn.place(x=50, y=425)

        # Pesquisar id
        self.id_en = Entry(self.f3, width=15, relief=FLAT, textvariable=self.id, font=15)
        self.id_en.place(x=200, y=315)
        self.id_btn = Button(self.f3, text="Pesquisar ID", width=12, font=("bold", 15), relief=FLAT, bg=self.cor2,
                             fg=self.cor4, command=self.pesquisar)
        self.id_btn.place(x=200, y=350)

        mainloop()

    def cadastrar(self):
        return

    def editar(self):
        return

    def remover(self):
        return

    def pesquisar(self):
        return


tela = GerFuncionarios()
