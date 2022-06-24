from tkinter import *
from g_ger_func import GerFuncionarios


class TelaGerente:
    def __init__(self):
        # Cores e fontes
        self.cor1 = "#800000"
        self.cor2 = "#FFFFFF"  # Branco
        self.cor3 = "#000000"  # Preto
        self.fonte = "roboto"

        # Janela
        self.janela = Tk()
        self.janela.title("Gerente")
        self.janela.geometry("500x500")
        self.janela.resizable(False, False)
        self.janela.configure(bg=self.cor1)

        # Logo
        self.logo = Label(self.janela, text="LOGO", font=("bold", 60), bg=self.cor1, fg=self.cor3)
        self.logo.place(x=140, y=80)

        # Label Gerente
        self.gerente = Label(self.janela, text="Gerente", font=(self.fonte, 15), bg=self.cor1, fg=self.cor2)
        self.gerente.place(x=210, y=180)

        # Botão Gerenciamento de funcionários
        self.gr_func_btn = Button(self.janela, text="Gerenciamento de funcionários", relief=FLAT, command=self.gr_func,
                                  font=(self.fonte, 11, "bold"), fg=self.cor1, width=27)
        self.gr_func_btn.place(x=130, y=240)

        # Botão Ordens de serviço
        self.ordem_btn = Button(self.janela, text="Ordens de serviço", relief=FLAT, command=self.ordem, fg=self.cor1,
                                font=(self.fonte, 11, "bold"), width=27)
        self.ordem_btn.place(x=130, y=290)

        # Botão Ver clientes
        self.clientes_btn = Button(self.janela, text="Clientes", relief=FLAT, command=self.clientes, fg=self.cor1,
                                   font=(self.fonte, 11, "bold"), width=27)
        self.clientes_btn.place(x=130, y=340)

        # Botão Sair
        self.sair_btn = Button(self.janela, text="Sair", relief=FLAT, command=self.janela.destroy, fg=self.cor1,
                               font=(self.fonte, 11, "bold"), width=27)
        self.sair_btn.place(x=130, y=390)

        mainloop()

    def gr_func(self):
        GerFuncionarios()

    def ordem(self):
        return

    def clientes(self):
        return
