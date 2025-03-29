import xml.etree.ElementTree as ET
from ListaTienda import ListaTienda
from ListaEnvio import ListaEnvio
Tiendas = ListaTienda()

def menu():
    ruta = ""
    while True:
        print("------------Menu-------------------")
        print("1. Ingresar la ruta del XML")
        print("2. Procesar Archivo")
        print("3. Analizar Datos")
        print("4. termianr programa")
        eleccion = int(input("Escribe una opcion: "))
        if eleccion == 1:
            ruta = input("Escribe la ruta del XML: ")
            print(f"Ruta ingresada {ruta}")
        elif eleccion == 2:
            analizarArchivo(ruta)  
        elif eleccion == 3:
            Tiendas.imprimirTiendas()
        elif eleccion == 4:
            break
        else:
            print("Opcion invalida")

def analizarArchivo(ruta):
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        tiendas = root.findall('tiendas')
        for tienda in tiendas:
            nombre = tienda.find('tienda')
            zona = nombre.get('zona')
            envios = tienda.findall('envio')
            lista_envios = ListaEnvio()
            for envio in envios:
                cliente = envio.text
                direccion = envio.get('direccion')
                estado = envio.get('estado')

                lista_envios.AgregarEnvio(cliente, direccion, estado)
            Tiendas.agregarAlFinal(nombre.text, zona, lista_envios)

    except Exception as e:
        print(e)

menu()