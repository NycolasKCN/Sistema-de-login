import tkinter as tk
from tkinter.messagebox import showinfo


class Sistema:

    def __init__(self):
        # Definindo variaveis base do Progama
        self.tela_log = tk.Tk()
        self.size = "300x150"
        self.tela_log.geometry(self.size)
        self.tela_log.resizable(width=False, height=False)

        self.user_var = tk.StringVar()
        self.password = tk.StringVar()

    def salvar(self, user="", password=""):
        """Salva os parametos user e password em um arquivo .txt
        Return: None"""
        try:
            dados = open("Dados.txt", "r")
        except FileNotFoundError:
            dados = open("Dados.txt", "w+")
            dados.close()
            print("Arquivo criado pois não existia")


        print(user, password)

    def login(self):
        """Compara os usuarios e as senhas para liberar o acesso
        Return: Retorna o resultado. Avisando que ha um erro na senha ou usuario ou confirmando o acesso"""

    def sair(self):
        self.tela_log.destroy()

    def Iniciar(self):
        """Inicia a interface e o programa

        Return: None"""
        # Texto do usuario
        self.label_user = tk.Label(self.tela_log, text="Usuário: ")
        self.label_user.grid(row=0, column=0, ipady=5, ipadx=5)

        # Entry para a entrada do usuario
        self.entry_user = tk.Entry(self.tela_log)
        self.entry_user.grid(row=0, column=1, ipady=5, ipadx=5)

        # Texto para a senha
        self.label_password = tk.Label(self.tela_log, text="Senha: ")
        self.label_password.grid(row=1, column=0, ipady=5, ipadx=5)

        # Entry para a entrada da senha
        self.entry_password = tk.Entry(self.tela_log)
        self.entry_password.grid(row=1, column=1, ipady=5, ipadx=5)

        self.button_exit = tk.Button(
            self.tela_log, text="Sair", command=self.sair)
        self.button_exit.grid(row=2, column=1, padx=5, pady=5)

        self.tela_log.mainloop()


if __name__ == "__main__":
    sis = Sistema()
    sis.Iniciar()


"""
self.button_save = tk.Button(
self.tela_log, text="Salvar", command=lambda: self.salvar(user=usuario, password=senha))
self.button_save.grid(row=2, column=2, padx=5, pady=5)
"""
