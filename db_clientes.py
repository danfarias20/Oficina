import sqlite3


class Funcionarios:
    def __init__(self, db):
        # Conectando ao banco
        self.con = sqlite3.connect(db)

        # Criando cursor para modificar a tabela
        self.cursor = self.con.cursor()

        # Criando a tabela
        self.sql = """CREATE TABLE IF NOT EXIST clientes (iden INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cpf TEXT, 
                      email TEXT, telefone TEXT, placa TEXT, endereco TEXT)"""
        self.cursor.execute(self.sql)
        self.con.commit()

    def add_cli(self, nome, cpf, email, telefone, placa, endereco):
        self.cursor.execute("INSERT INTO clientes VALUES (NULL, ?, ?, ?, ?, ?, ?)", (nome, cpf, email, telefone, placa,
                                                                                     endereco))
        self.con.commit()

    def edit_cli(self, iden, nome, cpf, email, telefone, placa, endereco):
        self.cursor.execute("UPDATE clientes SET nome=? cpf=? cpf=? email=? telefone=? placa=? endereco=? WHERE iden=?",
                            (nome, cpf, email, telefone, placa, endereco, iden))
        self.con.commit()

    def del_cli(self, iden):
        self.cursor.execute("REMOVE * FROM clientes WHERE iden=?", (iden, ))
        self.con.commit()
