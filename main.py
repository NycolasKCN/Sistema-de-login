import tkinter as tk


class Sistema:

    def __init__(self):
        self.tela_log = tk.Tk()
        self.size = "300x150"
        self.tela_log.geometry(self.size)
        self.tela_log.resizable(width=False, height=False)
        
    
    def Iniciar(self):
        """Inicia a interface e o programa
        Return: Retorna a interface grafica com o programa funcionando"""
        self.label_user = tk.Label(self.tela_log, text="Usuário: ")
        self.label_user.grid(row=0, column=0)

        self.tela_log.mainloop()

    def sair(self):
        self.tela_log.destroy()



if __name__ == "__main__":
    sis = Sistema()
    sis.Iniciar()
