from NodoTienda import NodoTienda

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
            self.ultimo.next = nueva_tienda
            self.ultimo = nueva_tienda
            nueva_tienda.id = self.tamanio
            self.tamanio += 1

    def agregarAlInico(self, tienda, zona):
        nueva_tienda = NodoTienda(tienda,zona)
        if self.primero is None:
            self.primero = nueva_tienda
            self.ultimo = nueva_tienda
        else:
            nueva_tienda.next = self.primero
            self.primero = nueva_tienda
        

    def imprimirTiendas(self):
        auxiliar: NodoTienda = self.primero
        for tienda in range(self.tamanio):
            print(f"Id: {auxiliar.id} Tienda: {auxiliar.tienda}, Zona: {auxiliar.zona}")
            auxiliar = auxiliar.next

    def BuscarPorInidice(self, indice):
        auxiliar: NodoTienda = self.primero
        if indice >= self.tamanio:
                return None
        else:
            for indices in range(self.tamanio):
           
                if auxiliar.id == indice:
                    return auxiliar
                auxiliar = auxiliar.next

    def len(self):
        print(self.tamanio)
    
lista_tienda = ListaTienda()

lista_tienda.agregarAlFinal("mana","4")
lista_tienda.agregarAlFinal("Manantial", "10")
lista_tienda.imprimirTiendas()
encontrado = lista_tienda.BuscarPorInidice(1)
if encontrado is not None:
    print(encontrado.tienda)
else:
    print("El indice es mayor al tamaño de la lista")
lista_tienda.len()
