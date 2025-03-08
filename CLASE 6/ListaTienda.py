from NodoTienda import NodoTienda
import os
import webbrowser

class ListaTienda:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0
    
    def agregarAlFinal(self, tienda, zona):
        nueva_tienda = NodoTienda(tienda,zona)
        if self.primero is None:
            self.primero = nueva_tienda
            self.ultimo = nueva_tienda
            nueva_tienda.id = self.tamanio
            self.tamanio += 1
        else:
            nueva_tienda.anterior=self.ultimo
            self.ultimo.siguiente = nueva_tienda
            self.ultimo = nueva_tienda
            self.ultimo.id = self.tamanio
            self.tamanio +=1


    def imprimirTiendas(self):
        auxiliar: NodoTienda = self.primero
        for tienda in range(self.tamanio):
            print(f"Id: {auxiliar.id} Tienda: {auxiliar.tienda}, Zona: {auxiliar.zona}")
            auxiliar = auxiliar.siguiente

    def BuscarPorInidice(self, indice):
        auxiliar: NodoTienda = self.primero
        if indice >= self.tamanio:
                return None
        else:
            for indices in range(self.tamanio):
           
                if auxiliar.id == indice:
                    return auxiliar
                auxiliar = auxiliar.siguiente

    def len(self):
        print(self.tamanio)

    def Graficar(self):
        graficar = "digraph G{ \n"
        graficar += "node[shape=box]\n"
        graficar += 'label =\"Lista de tiendas\" \n'
        auxiliar : NodoTienda = self.primero
        for tiendas in range(self.tamanio):
            nodo = "nodo"+str(auxiliar.id)
            graficar += nodo+"[label=\"Tienda: "+auxiliar.tienda+", Zona: "+str(auxiliar.zona)+"\"]\n"
            auxiliar = auxiliar.siguiente
        aux: NodoTienda = self.primero
        while aux.siguiente is not None:
            nodo = "nodo"+str(aux.id)
            nodosiguiente = "nodo"+str(aux.siguiente.id)
            if aux != self.primero:
                nodoanterior = "nodo"+str(aux.anterior.id)
                graficar += "{"+nodo+" -> "+nodosiguiente+" }\n"
                graficar += "{"+nodo+" -> "+nodoanterior+" }\n"
            else:
                 graficar += "{ "+nodo+" -> "+nodosiguiente+" }\n"
            aux = aux.siguiente

        if aux == self.ultimo:
            nodo = "nodo"+str(aux.id)
            nodoanterior= "nodo"+str(aux.anterior.id)
            graficar += "{ "+nodo+" -> "+nodoanterior+" }\n"
        graficar += "}"
        dot = "Lista_de_tiendas.txt"
        with open(dot, "w") as grafo:
            grafo.write(graficar)
        resultado = "Lista_de_tiendas.jpg"
        os.system("dot -Tjpg "+dot+" -o "+resultado)

    
lista_tienda = ListaTienda()

lista_tienda.agregarAlFinal("mana","4")
lista_tienda.agregarAlFinal("Manantial", "10")
lista_tienda.agregarAlFinal("tienda", "8")
lista_tienda.agregarAlFinal("nueva_tienda", "13")
lista_tienda.imprimirTiendas()
lista_tienda.Graficar()
