from tkinter import *

ventana = Tk()
ventana.title("Marcos")
ventana.geometry("700x700")
marco_padre =  Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="blue"
)
marco_padre.pack(side=BOTTOM, fill=X, expand=YES, anchor=S)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd=5,  #borde
    relief="solid"  #relieve: flat, goove, raised, ridge,  solid
)
#side = right, left, top, bottom
marco.pack(side=LEFT, anchor=SW)

marco1 = Frame(marco_padre, width=250, height=250)
marco1.config(
    bg="green",
    bd=5,  #borde
    relief="groove"  #relieve: flat, goove, raised, ridge,  solid, sunken
)
marco1.pack(side=RIGHT, anchor=SE)


marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    #bg="light blue",
)
marco_padre.pack(side=TOP, fill=X, expand=YES, anchor=N)

marco2 = Frame(marco_padre, width=250, height=250)
marco2.config(
    bg="blue",
    bd=5,  #borde
    relief="groove"  #relieve: flat, goove, raised, ridge,  solid, sunken
)
marco2.pack(side=LEFT)

marco2 = Frame(marco_padre, width=250, height=250)
marco2.config(
    bg="orange",
    bd=5,  #borde
    relief="groove"  #relieve: flat, goove, raised, ridge,  solid, sunken
)
marco2.pack(side=RIGHT)

ventana.mainloop()