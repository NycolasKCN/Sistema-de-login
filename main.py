from os import close, error
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import END, S
from tkinter.messagebox import showinfo
from typing import Text


class Sistema:

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
        self.entry_user = tk.Entry(self.tela_log)
        self.entry_user.grid(row=0, column=1, ipadx=5, ipady=5)

        # Texto para a senha
        label_password = tk.Label(self.tela_log, text="Senha: ")
        label_password.grid(row=1, column=0, ipadx=5, ipady=5)

        # Entry para a entrada da senha
        self.entry_password = tk.Entry(
            self.tela_log, show="*")
        self.entry_password.grid(row=1, column=1, ipadx=5, ipady=5)

        # Botão para registrar
        button_register = tk.Button(
            self.tela_log, text="Registrar", command=lambda: self.registrar())
        button_register.grid(row=2, column=0, padx=20, pady=5)

        # Botão para encerrar o programa
        button_exit = tk.Button(
            self.tela_log, text="Sair", command=lambda: self.sair())
        button_exit.grid(row=2, column=1, padx=20, pady=5)

        # Botão de login
        button_login = tk.Button(
            self.tela_log, text="Login", command=lambda: self.login())
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

    def usuarioExiste(self):
        """Verifica se o usuario que foi digitado existe, caso exista retorna true

        return: True ou False"""
        usuarios = {
            "user": self.pegueString(self.entry_user),
            "password": self.pegueString(self.entry_password)}

        if self.arquivoExiste(self.arquivo):
            count = 0
            with open(self.arquivo, "r",) as dados:
                for linha in dados:
                    linha = linha.strip(";")
                    user = linha.split()

                    if user[0] == usuarios["user"]:
                        count += 2
                        break
                dados.close()

            if count > 0:
                return "Existe"
            elif count == 0:
                return "não existe"

        else:
            open(self.arquivo, "w").close()

    def sair(self):
        """Encerra o programa
        Return: None"""
        self.tela_log.destroy()

    def login(self):
        """Compara os usuarios e as senhas para liberar o acesso
        Return: Retorna o resultado. Avisando que ha um erro na senha ou usuario ou confirmando o acesso"""

    def registrar(self):
        """Salva os parametos user e password em um arquivo .txt

        Return: None"""
        usuarios = {
            "user": self.pegueString(self.entry_user),
            "password": self.pegueString(self.entry_password)}

        if self.usuarioExiste() == "não existe":
            registrar = open("Dados.txt", "a")
            registrar.write("{} ; {}\n".format(
                usuarios["user"], usuarios["password"]))

        elif self.usuarioExiste() == "Existe":
            showinfo(title="Usuario já cadastrado",
                     message="Usuario já cadastrado porfavor entrar com login")


if __name__ == "__main__":
    sis = Sistema()
    sis.Iniciar()
