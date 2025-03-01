from NodoNuevo import NodoNuevo

class ListaNuevoNodo:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0
    
    def AgregarAlFinal(self, nombre):
        nuevo_nodo = NodoNuevo(nombre)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.tamanio += 1
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.tamanio += 1

    def ImprimirNodos(self):
        auxiliar = self.primero
        for nodo in range(self.tamanio):
            print(f"nombre: {auxiliar.nombre}")
            auxiliar = auxiliar.siguiente

    




