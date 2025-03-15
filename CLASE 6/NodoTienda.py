class NodoTienda():
    def __init__(self,tienda, zona, listatienda):
        self.id = 0
        self.tienda = tienda
        self.zona = zona
        self.envios = listatienda
        self.siguiente = None
        self.anterior = None