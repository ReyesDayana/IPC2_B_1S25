

from ListaNuevoNodo import ListaNuevoNodo



mi_lista = ListaNuevoNodo()
while True:
    print("1. Ingresar un nuevo nodo")
    print("2. Ver la lista")
    print("3. Salir")
    print("Selecciones una opcion")
    opcion = int(input())

    if opcion == 1:
        print("Ingrese el nombre")
        nombre= input()
        mi_lista.AgregarAlFinal(nombre)

    elif opcion == 2:
        mi_lista.ImprimirNodos()

    elif opcion == 3:
        break
    else:
        print("Opcion incorrecta")