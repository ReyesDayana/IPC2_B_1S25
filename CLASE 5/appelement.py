import xml.etree.ElementTree as ET
from ListaNuevoNodo import ListaNuevoNodo
lista = ListaNuevoNodo()
def menu():
    ruta = ""
    while True:
        print("------------Menu-------------------")
        print("1. Ingresar la ruta del XML")
        print("2. Imprimir XML")
        print("3. Procesar Archivo")
        print("4. Escribir Archivo")
        print("5. Salir")
        eleccion = int(input("Escribe una opcion: "))

        if eleccion == 1:
            ruta = input("Ingrese ruta del archivo xml: \n")
            print(f'Ruta ingresada {ruta}')
        elif eleccion == 2:
            try:
                imprimir_xml(ruta)
            except Exception as e:
                print(f'Error al leer el archivo {e}')
        elif eleccion == 3:
            AnalizarArchivo(ruta)
        elif eleccion == 4:
           pass
        elif eleccion == 5:
            print("Saliendo...")
            break
        else:
            print("Opcion invalida")


def imprimir_xml(ruta):
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        ET.dump(root)
    except Exception as e:
        print(f'Error al leer el archivo {e}')

def AnalizarArchivo(ruta):
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        libros = root.findall('book')
        for libro in libros:
            titulo = libro.get('title')
            lista.AgregarAlFinal(titulo)
        lista.ImprimirNodos()
                
    except Exception as e:
        print(f'Error al leer el archivo {e}')



menu()