import tkinter as tk
from tkinter.messagebox import ERROR, showinfo


class Autenticador:

    def __init__(self):
        # Definindo variaveis base do Progama
        self.tela_log = tk.Tk()
        self.size = "300x150"
        self.tela_log.geometry(self.size)
        self.tela_log.resizable(width=False, height=False)
        self.arquivo = "Dados.txt"

    def Iniciar(self):
        """Inicia a interface e o programa

        Return: None"""

        # Texto do usuario
        label_user = tk.Label(self.tela_log, text="Usuário: ")
        label_user.grid(row=0, column=0, ipadx=5, ipady=5)

        # Entry para a entrada do usuario
        entry_user = tk.Entry(self.tela_log)
        entry_user.grid(row=0, column=1, ipadx=5, ipady=5)

        # Texto para a senha
        label_password = tk.Label(self.tela_log, text="Senha: ")
        label_password.grid(row=1, column=0, ipadx=5, ipady=5)

        # Entry para a entrada da senha
        entry_password = tk.Entry(
            self.tela_log, show="*")
        entry_password.grid(row=1, column=1, ipadx=5, ipady=5)

        # Botão para registrar
        button_register = tk.Button(self.tela_log, text="Registrar",
                                    command=lambda: self.registrar(user=self.pegueString(entry_user),
                                                                   password=self.pegueString(entry_password)))
        button_register.grid(row=2, column=0, padx=20, pady=5)

        # Botão para encerrar o programa
        button_exit = tk.Button(
            self.tela_log, text="Sair", command=lambda: self.sair())
        button_exit.grid(row=2, column=1, padx=20, pady=5)

        # Botão de login
        button_login = tk.Button(self.tela_log, text="Login",
                                 command=lambda: self.login(user=self.pegueString(entry_user),
                                                            password=self.pegueString(entry_password)))
        button_login.grid(row=2, column=2, padx=20, pady=5)

        self.tela_log.mainloop()

    def pegueString(self, entry=""):
        """'Puxa' as strings da entry
        entry: Se passa o nome da entry na qual você quer a string
        return: Retona a string"""
        return entry.get()

    def arquivoExiste(self, nome):
        try:
            a = open(nome, 'rt')
            a.close()
        except FileNotFoundError:
            return False
        else:
            return True

    def usuarioExiste(self, usuario):
        """Verifica se o usuario que foi digitado existe, caso exista retorna true

        usuairo: recebe o nome de usuario

        return: True ou False"""

        if self.arquivoExiste(self.arquivo):
            count = 0
            with open(self.arquivo, "r",) as dataBase:
                for linha in dataBase:
                    linha = linha.strip(";")
                    user = linha.split()

                    if user[0] == usuario:
                        count += 2
                        break
                dataBase.close()

            if count > 0:
                return True
            elif count == 0:
                return False

        else:
            open(self.arquivo, "w").close()

    def sair(self):
        """Encerra o programa
        Return: None"""
        self.tela_log.destroy()

    def login(self, user, password):
        """Compara os usuarios e as senhas para liberar o acesso
        user: Usuario
        password: Senha 
        Return: Retorna o resultado. Avisando que ha um erro na senha ou usuario ou confirmando o acesso"""
        usuarios = {
            "user": user,
            "password": password}

        if not self.usuarioExiste(usuarios["user"]):
            showinfo(title="Usuário não existe",
                     message="Usuário digitado não existe, porfavo registrar!")

        elif self.usuarioExiste(usuarios["user"]):

            with open(self.arquivo, "r") as dataBase:
                for linha in dataBase:
                    usuario = linha.split()

                    if usuario[0] == user:  # esse bloco verifica se o usuario e a senha são as mesmas
                        if usuario[2] == password:
                            showinfo(title="Acesso liberado",
                                     message="Usuário e senha estão corretos!")
                        else:
                            showinfo(title="Erro",
                                     message="Usuário ou senha está errada!")

    def registrar(self, user, password):
        """Salva os parametos user e password em um arquivo .txt
        user: Usuario
        password: Senha 
        Return: None"""
        usuarios = {
            "user": user,
            "password": password}

        if not self.usuarioExiste(usuarios["user"]):
            try:
                with open(self.arquivo, "a") as dataBase:
                    dataBase.write("{} ; {}\n".format(
                        usuarios["user"], usuarios["password"]))
                    dataBase.close()
                    showinfo(title="Usuário Cadastrado",
                             message="Usuário cadastrado com sucesso!")
            except:
                print(f"Um erro desonhecido ocorreu. cod.: {ERROR}")
        elif self.usuarioExiste(usuarios["user"]):
            showinfo(title="Usuário já cadastrado",
                     message="Usuário já cadastrado porfavor entrar com login.")


if __name__ == "__main__":
    sis = Autenticador()
    sis.Iniciar()
