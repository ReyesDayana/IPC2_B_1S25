from tkinter import *

class Programa:
    def __init__(self):
        self.title = "Titulo de la ventana"
        self.icono = "icono.ico"
        self.size = "600x600"
        self.resizable = False
        self.ventana = Tk()
    
    def cargar(self):
        self.ventana.title(self.title)
        self.ventana.iconbitmap(self.icono)
        self.ventana.geometry(self.size)
        if self.resizable is True:
            self.ventana.resizable(True, True)
        else:
            self.ventana.resizable(False, False)

    def addTextoBlanco(self, texto):
        texto = Label(self.ventana, text=texto)
        texto.config(
            fg="white",
            bg="black",
            padx = 10,
            pady =10,
            font=("Arial", 14, "bold"),
            cursor="spider"

        )
        texto.pack()
    
    def addTextoNegro(self, texto):
        texto = Label(self.ventana, text=texto)
        texto.config(
   
            padx = 10,
            pady =10,
            font=("Arial", 14, "bold"),
            cursor="spider"

        )
        texto.pack()
    
    def mostrar(self):
        self.ventana.mainloop()

programa =  Programa()
programa.cargar()
programa.addTextoBlanco("Hola mundo")
programa.addTextoNegro("Como estan")
programa.mostrar()
