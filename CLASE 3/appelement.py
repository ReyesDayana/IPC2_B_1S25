import xml.etree.ElementTree as ET
from libros import biblioteca as librosescribir

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
            escribirArchivo()
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
            autor = libro.get('author')
            print(f'------- Libro: {titulo}, autor: {autor}-------')
            for capitulo in libro.findall('Chapter'):
                nombrecap = capitulo.text
                pagina = capitulo.get('page')
                print(f'\t Capitulo: {nombrecap}, pagina: {pagina}')
    except Exception as e:
        print(f'Error al leer el archivo {e}')

def escribirArchivo():
    escribirxml = "<?xml version='1.0' encoding='utf-8'?>\n"
    escribirxml += "<books>\n"
    root = ET.Element('books')

    for libro in librosescribir['books']:
        escribirxml += "\t<book title=\""+libro['title']+"\" author=\""+libro['author']+"\">\n"
        book = ET.SubElement(root, 'book', title=libro['title'], author=libro['author'])
        for capitulo in libro['chapters']:
            escribirxml += "\t\t<Chapter page=\"" + capitulo['page'] + "\">" + capitulo['title'] + "</Chapter>\n"
            ET.SubElement(book, 'Chapter', page=str(capitulo['page'])).text = capitulo['title']
        escribirxml += "\t</book>\n"
    tree = ET.ElementTree(root)
    escribirxml += "</books>\n"
    with open('escrituraelement.xml', 'wb') as f:
        tree.write(f, encoding='utf-8', xml_declaration=True)
    with open('escrituraelement2.xml', 'w', encoding='utf-8') as f:
        f.write(escribirxml)

menu()