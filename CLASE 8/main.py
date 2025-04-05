import tkinter as tk
from Lista import Lista

mi_lista= Lista()


def agregar_a_lista():
    valor = entrada.get()
    if valor:
        try:
            mi_lista.AgregarNodo(valor)
            entrada.delete(0, tk.END)
            actualizar_label()
        except Exception as e:
            resultado_label.config(text = "Por favor ingresa un valor.")


def actualizar_label():
    texto = ""
    aux = mi_lista.primero
    if aux is None:
        texto="La lista esta vacia"
    else:
        while aux is not None:
            texto += f"{aux.valor} -> "
            aux = aux.siguiente
        texto+= "None"
    resultado_label.config(text=texto)

#Interfaz
ventana = tk.Tk()
ventana.title("Lista enlazada y Tkinter")
ventana.geometry("400x250")

tk.Label(ventana, text="Ingresa un valor: ").pack(pady=5)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

tk.Button(ventana, text="Agregar a la lista", command=agregar_a_lista).pack(pady=5)

tk.Label(ventana, text="Contenido de la lista: ").pack(pady=5)
resultado_label = tk.Label(ventana, text="La lista esta vacia", wraplength=350, justify="left")
resultado_label.pack(pady=10)
ventana.mainloop()