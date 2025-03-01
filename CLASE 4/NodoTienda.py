class NodoTienda():
    def __init__(self,tienda, zona):
        self.id = 0
        self.tienda = tienda
        self.zona = zona
        self.siguiente = None
        self.anterior = None