from os import error
import tkinter as tk
from tkinter.constants import END
from tkinter.messagebox import showinfo


class Sistema:

    def __init__(self):
        # Definindo variaveis base do Progama
        self.tela_log = tk.Tk()
        self.size = "300x150"
        self.tela_log.geometry(self.size)
        self.tela_log.resizable(width=False, height=False)
        global entry_user, entry_password

    def getString(self, entry):
        """'Puxa' as strings dos entrys
        entry: Se passa o nome da entry na qual você quer a string
        return: Retona a string"""
        return entry.get()

    def arqExiste(self, nome):
        try:
            a = open(nome, 'rt')
            a.close()
        except FileNotFoundError:
            return False
        else:
            return True

    def sair(self):
        """Encerra o programa
        Return: None"""
        self.tela_log.destroy()

    def login(self):
        """Compara os usuarios e as senhas para liberar o acesso
        Return: Retorna o resultado. Avisando que ha um erro na senha ou usuario ou confirmando o acesso"""

    def Iniciar(self):
        """Inicia a interface e o programa

        Return: None"""

        # Texto do usuario
        self.label_user = tk.Label(self.tela_log, text="Usuário: ")
        self.label_user.grid(row=0, column=0, ipadx=5, ipady=5)

        # Entry para a entrada do usuario
        self.entry_user = tk.Entry(self.tela_log)
        self.entry_user.grid(row=0, column=1, ipadx=5, ipady=5)

        # Texto para a senha
        self.label_password = tk.Label(self.tela_log, text="Senha: ")
        self.label_password.grid(row=1, column=0, ipadx=5, ipady=5)

        # Entry para a entrada da senha
        self.entry_password = tk.Entry(
            self.tela_log, show="*")
        self.entry_password.grid(row=1, column=1, ipadx=5, ipady=5)

        # Botão para encerrar o programa
        self.button_exit = tk.Button(
            self.tela_log, text="Sair", command=lambda: self.sair())
        self.button_exit.grid(row=2, column=1, padx=20, pady=5)

        # Botão para registrar
        self.button_register = tk.Button(
            self.tela_log, text="Registrar", command=lambda: self.registrar())
        self.button_register.grid(row=2, column=0, padx=20, pady=5)

        # Botão de login
        self.button_login = tk.Button(
            self.tela_log, text="Login", command=lambda: self.login())
        self.button_login.grid(row=2, column=2, padx=20, pady=5)

        self.tela_log.mainloop()

    def registrar(self):
        """Salva os parametos user e password em um arquivo .txt
        Return: None"""
        self.usuarios = []
        self.arquivo = "Dados.txt"

        if self.arqExiste(self.arquivo):
            with open(self.arquivo, "w+", newline="") as arq:
                
                for linha in arq:
                    linha = linha.strip(";")
                    user = linha.split()
                    



if __name__ == "__main__":
    sis = Sistema()
    sis.Iniciar()
