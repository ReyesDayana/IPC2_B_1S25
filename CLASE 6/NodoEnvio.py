class NodoEnvio:
    def __init__(self, cliente, direccion, estado):
        self.cliente = cliente
        self.direccion = direccion
        self.estado = estado
        self.next = None