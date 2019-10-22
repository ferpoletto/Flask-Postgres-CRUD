from conexao import Connection


class Usuario:

    def cadastrar_usuario(self, json):
        self.json = json
        self.nome = self.json['Nome']
        self.email = self.json['Email']
        self.CPF = self.json['CPF']

        try:
            self.bd = Connection()
            self.bd.executarSQL("INSERT INTO usuario(nome, email, cpf) VALUES ('{0}','{1}','{2}')".format(self.nome, self.email, self.CPF))
        except:
            print('Erro ao cadastrar usuário')
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

    def deletar_usuario(self, id):
        try:
            self.bd = Connection()
            self.bd.executarSQL("DELETE from usuario WHERE id = {0}".format(id))
        except:
            print("Erro ao deletar usuario")
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

    def atualizar_usuario(self, id, json):
        try:
            self.bd = Connection()
            self.nome, self.email, self.CPF = json["Nome"], json["Email"], json["CPF"]
            self.bd.executarSQL("UPDATE usuario set nome = '{0}', email = '{1}', cpf = '{2}' where id = {3}".format(self.nome, self.email, self.CPF, id))
        except:
            print("Erro ao atualizar usuario")
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

    def mostrar_usuario(self, id):
        try:
            self.bd = Connection()
            if id == None:
                self.query = "select * from usuario"
            else:
                self.query = "SELECT * FROM usuario WHERE id = {0}".format(id)
            self.data = self.bd.executarSQLRetorno(self.query)
            return self.data
        except:
            print("Erro ao mostrar")
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()
