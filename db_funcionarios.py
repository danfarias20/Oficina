import sqlite3


class Funcionarios:
    def __init__(self, db):
        # Conectando ao banco
        self.con = sqlite3.connect(db)

        # Criando cursor para modificar a tabela
        self.cursor = self.con.cursor()

        # Criando a tabela
        self.sql = """CREATE TABLE IF NOT EXISTS funcionarios (iden INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, 
                      senha TEXT, cpf TEXT, cargo TEXT)"""
        self.cursor.execute(self.sql)
        self.con.commit()

    def add_func(self, nome, senha, cpf, cargo):
        self.cursor.execute("INSERT INTO funcionarios VALUES (NULL, ?, ?, ?, ?)", (nome, senha, cpf, cargo))
        self.con.commit()

    def edit_func(self, iden, nome, senha, cpf, cargo):
        self.cursor.execute("UPDATE funcionarios SET nome=? senha=? cpf=? cargo=? WHERE iden=?", (nome, senha, cpf,
                                                                                                  cargo, iden))
        self.con.commit()

    def del_func(self, iden):
        self.cursor.execute("REMOVE * FROM funcionarios WHERE iden=?", (iden, ))
        self.con.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM funcionarios")
        linhas = self.cursor.fetchall()
        return linhas
