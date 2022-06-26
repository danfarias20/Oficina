from tkinter import *
from tkinter import ttk
from tkinter import messagebox
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
        self.cadastrar_btn.place(x=13, y=315)

        # Botão editar
        self.editar_btn = Button(self.f3, text="Editar", width=10, font=("bold", 15), relief=FLAT, bg=self.cor2,
                                 fg=self.cor4, command=self.editar)
        self.editar_btn.place(x=13, y=370)

        # Botão remover
        self.remover_btn = Button(self.f3, text="Remover", width=10, font=("bold", 15), relief=FLAT, bg=self.cor2,
                                  fg=self.cor4, command=self.remover)
        self.remover_btn.place(x=13, y=425)

        # Botão limpar
        self.limpar_btn = Button(self.f3, text="Limpar", width=10, font=("bold", 15), relief=FLAT, bg=self.cor2,
                                 fg=self.cor4, command=self.limpar)
        self.limpar_btn.place(x=13, y=480)

        # Treeview
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=15)
        self.style.configure("mystyle.Treeview.Heading", font=15)

        self.tv = ttk.Treeview(self.f4, height=6, columns=("col1", "col2", "col3", "col4", "col5"),
                               style="mystyle.Treeview")

        self.tv.heading("#0", text="ID")
        self.tv.heading("#1", text="Nome")
        self.tv.heading("#2", text="Senha")
        self.tv.heading("#3", text="CPF")
        self.tv.heading("#4", text="Cargo")

        self.tv.column("#0", width=30)
        self.tv.column("#1", width=240)
        self.tv.column("#2", width=180)
        self.tv.column("#3", width=150)
        self.tv.column("#4", width=190)

        self.tv.place(x=0, y=0, width=800, height=540)

        self.scroll = Scrollbar(self.f4, orient="vertical")
        self.tv.config(yscrollcommand=self.scroll.set)
        self.scroll.place(x=780, y=1, height=538, width=20)

        mainloop()

    def get_data(self):
        selected_row = self.tv.focus()
        data = self.tv.item(selected_row)
        global row
        row = data["values"]
        self.nome.set(row[1])
        self.senha.set(row[2])
        self.cpf.set(row[3])
        self.cargo.set(row[4])

    def display_all(self):
        self.tv.delete(*self.tv.get_children())
        for i in self.db.fetch():
            self.tv.insert("", END, values=i)

    def cadastrar(self):
        if self.nome_en.get() == "" or self.senha_en.get() == "" or self.cpf_en.get() == "" \
                or self.cargo_en.get() == "":
            messagebox.showerror("Erro na entrada", "Por favor, preencha todos os campos")
        else:
            self.db.add_func(self.nome_en.get(), self.senha_en.get(), self.cpf_en.get(), self.cargo_en.get())
            self.limpar()
            self.display_all()

    def editar(self):
        if self.nome_en.get() == "" or self.senha_en.get() == "" or self.cpf_en.get() == "" \
                or self.cargo_en.get() == "":
            messagebox.showerror("Erro na entrada", "Por favor, preencha todos os campos")
        else:
            self.db.edit_func(self.nome_en.get(), self.senha_en.get(), self.cpf_en.get(), self.cargo_en.get())
            self.limpar()
            self.display_all()

    def remover(self):
        self.db.del_func([0])
        self.limpar()
        self.display_all()

    def pesquisar(self):
        return

    def limpar(self):
        self.nome_en.delete(0, END)
        self.senha_en.delete(0, END)
        self.cpf_en.delete(0, END)
        self.cargo_en.delete(0, END)


tela = GerFuncionarios()
