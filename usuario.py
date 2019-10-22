from conexao import Connection
class Usuario:

    def __init__(self):
        bd = Connection()

    def cadastrar_usuario(self, json):
        self.json = json
        self.nome = self.json['Nome']
        self.email = self.json['Email']
        self.CPF = self.json['CPF']

        try:
            self.bd = Connection()
            self.query = "INSERT INTO usuario(nome, email, cpf) VALUES ('{0}','{1}','{2}')".format(self.nome, self.email, self.CPF)
            self.bd.executarSQL(self.query)
            print(f'Cadastro do {self.nome} realizado com sucesso!')
        except:
            print('Erro ao cadastrar usuário')
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()





