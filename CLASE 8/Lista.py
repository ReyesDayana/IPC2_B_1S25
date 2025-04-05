from Nodo import Nodo
import os
import webbrowser
from graphviz import Digraph

class Lista:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0
    def AgregarNodo(self, valor):
    
        nuevo_nodo = Nodo(valor)
       
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.tamanio += 1
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.tamanio +=1
    
    def ImprimirLista(self):
        auxiliar = self.primero
        for i in range(self.tamanio):
            print(f"Valor: {auxiliar.valor} ")
            auxiliar = auxiliar.siguiente
    
    def Graficar(self):
        graficarlista = "digraph G{ \n"
        graficarlista += "node[shape=box] \n"
        graficarlista += "label= \"Lista Simple\" \n"
        auxiliar: Nodo = self.primero
        for nodos in range(self.tamanio):
            nodo = "nodo"+str(auxiliar.valor)
            graficarlista += nodo + "[label = \"Valor: "+str(auxiliar.valor)+"\"]\n"
            auxiliar = auxiliar.siguiente
        
        aux: Nodo = self.primero
        while aux.siguiente is not None:
            nodo = "nodo"+str(aux.valor)
            nodosiguiente = "nodo"+str(aux.siguiente.valor)
            graficarlista += "{rank=same; " +nodo+ "->"+nodosiguiente+"}\n"
            aux = aux.siguiente
        graficarlista += "}"
        dot ="Nodos.txt"
        with open(dot, 'w') as grafo:
            grafo.write(graficarlista)
        result = "Nodos.pdf"
        os.system("dot -Tpdf "+dot+" -o "+result)
        webbrowser.open(result)
    
    def GraficarLista(self):
        dot = Digraph()
        auxliar: Nodo = self.primero
        for nodos in range(self.tamanio):
            dot.node(str(auxliar.valor), label= f"Valor: {str(auxliar.valor)}")
            auxliar= auxliar.siguiente
        aux: Nodo = self.primero
        while aux.siguiente is not None:
            dot.edge(str(aux.valor), str(aux.siguiente.valor))
            aux= aux.siguiente
        
        dot.render('Lista', format='png', cleanup=True, view=True)
        print("Grafico generado")
