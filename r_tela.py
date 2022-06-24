from tkinter import *


class TelaRecepcionista:
    def __init__(self):
        # Cores e fontes
        self.cor1 = "#800000"
        self.cor2 = "#FFFFFF"  # Branco
        self.cor3 = "#000000"  # Preto
        self.fonte = "roboto"

        # Janela
        self.janela = Tk()
        self.janela.title("Recepcionista")
        self.janela.geometry("500x500")
        self.janela.resizable(False, False)
        self.janela.configure(bg=self.cor1)

        # Logo
        self.logo = Label(self.janela, text="LOGO", font=("bold", 60), bg=self.cor1, fg=self.cor3)
        self.logo.place(x=140, y=80)

        # Label Recepcionista
        self.recepcionista = Label(self.janela, text="Recepcionista", font=(self.fonte, 15), bg=self.cor1, fg=self.cor2)
        self.recepcionista.place(x=195, y=180)

        # Botão cadastrar clientes
        self.cadastrar_btn = Button(self.janela, text="Cadastrar clientes", relief=FLAT, command=self.cadastrar,
                                    font=(self.fonte, 11, "bold"), fg=self.cor1, width=27)
        self.cadastrar_btn.place(x=130, y=240)

        # Botão orçamentos
        self.orcamento_btn = Button(self.janela, text="Orçamentos", relief=FLAT, command=self.orcamento, fg=self.cor1,
                                    font=(self.fonte, 11, "bold"), width=27)
        self.orcamento_btn.place(x=130, y=290)

        # Botão Sair
        self.sair_btn = Button(self.janela, text="Sair", relief=FLAT, command=self.janela.destroy, fg=self.cor1,
                               font=(self.fonte, 11, "bold"), width=27)
        self.sair_btn.place(x=130, y=340)

        mainloop()

    def cadastrar(self):
        return

    def orcamento(self):
        return
