from NodoEnvio import NodoEnvio

class ListaEnvio:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.tamanio = 0
    
    def AgregarEnvio(self, cliente, direccion, estado):
        nuevo_envio = NodoEnvio(cliente, direccion, estado)
        if self.cabeza is None:
            self.cabeza = nuevo_envio
            self.ultimo = nuevo_envio
            self.tamanio += 1
        else:
            self.ultimo.next = nuevo_envio
            self.ultimo = nuevo_envio
            self.tamanio += 1
        self.ultimo.next = self.cabeza
    

    def ImprimirLista(self):
        aux: NodoEnvio = self.cabeza
        for envio in range(self.tamanio):
            print(f"Cliente {aux.cliente}, Direccion: {aux.direccion}, Estado: {aux.estado}, siguiente: {aux.next.cliente}")
            aux = aux.next


lista = ListaEnvio()

lista.AgregarEnvio("Dayana","zona 10", "pagado")
lista.AgregarEnvio("Lucia","zona 5", "No pagado")
lista.ImprimirLista()

