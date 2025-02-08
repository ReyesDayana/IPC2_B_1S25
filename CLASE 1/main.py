# Funciones:
# Función Suma:

def funcDummy():
    print("hola")

def sumaFunc(num1, num2):
    return num1 + num2

def restaFunc(num1, num2):
    return num1 - num2

def divisionFunc(num1, num2):
    return num1 / num2

def multiplicacionFunc(num1, num2):
    return num1 * num2

def Menu():
    print('¿Qué operación quieres hacer?')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')
    print('5. Salir')
    opcion = input()
    return opcion


if  __name__ == '__main__':
    print('Hola, estoy en el main')

    # Este es un comentario de 1 línea.

    '''
    Hola
    este
    es
    un
    comentario
    multilínea.
    '''

    # Variables:

    stringLargo = '''
    soy
    un
    string
    largo
    '''

    print(stringLargo)

    a = -1 # entero
    b = 3 # entero

    c = 1.0 # flotante
    d = 2.0 # flotante

    e = "Dobles"
    f = 'simple'

    # Booleans:
    g = True # Boolean
    h = False # Boolean

    # Operaciones
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a/b

    # impresiones:
    print(suma)
    print(resta)
    print(multiplicacion)
    print(division)

    print('Ingrese su nombre: ')
    nombre = input()

    edad = input("Ingrese su edad: ")

    print('Hola ' + nombre + ' su edad es:', int(edad))

    # Condicionales:
    # IF:
    if a == 1:
        print('Si, "a" si posee el valor de 1.')
    else:
        print("No, 'a' no posee el valor de 1.")

    # Operadores lógicos:
    # Python: and, or, not ------------------ Java: &&, ||, !

    if a == 1 and b == 2:
        print("Se cumple con las condiciones")
    elif a == 2 or int(edad)== 23:
        print("Se cumple alguna de las condiciones")
    elif not a == 1:
        print("Se cumple con que 'a' NO es 1")
    else:
        print("Ninguna de las condiciones se cumple")

    # Operadores de comparación:
    # ==, !=, <, >, <=, >=
    # igual que, no es igual, menor qué, mayor qué, menor igual qué, mayor igual qué:

    if int(edad) >= 18:
        print("MAYOR DE EDAD")
    else:
        print("MENOR DE EDAD")
    
    #Ciclos:
    # FOR:
    for i in range(1, 11):
        print(i, "HOLA")

    for i in range(0, 10, 2):
        print(i)

    '''
    for(int i=0; i<10; i+=2){
    
    }

    '''

    #WHILE:
    print("CONTADOR CON WHILE: ")
    contador = 0
    while contador < 10:
        print(contador)
        contador+=1
    
    # FUNCIONES
    print('SUMA', sumaFunc(1,22))
    print('RESTA', restaFunc(7,1))
    print('MULTIPLICACIÓN', multiplicacionFunc(4,4))
    print('DIVISIÓN', divisionFunc(6,2))

    funcDummy()

    # Saltos de Línea:
    print()
    print('\n')

    # Listas:
    listaEjemplo = [1,2,3]
    listaEjemplo2 = []
    listaEjemplo2 = [1, "a", True]

    for elemento in listaEjemplo:
        print(elemento)

    for i in range(0, len(listaEjemplo)):
        print(listaEjemplo[i])

    opcionSeleccionada = Menu()
    while opcionSeleccionada != 5:
        num1 = int(input('Ingrese el primer número: '))
        num2 = int(input('Ingrese el segundo número: '))

        if opcionSeleccionada == '1':
            print(" La suma es: "+ str(sumaFunc(num1, num2)))
        elif opcionSeleccionada == '2':
            print(" La resta es: "+ str(restaFunc(num1, num2)))
        elif opcionSeleccionada == '3':
            print(" La multiplicación es: "+ str(multiplicacionFunc(num1, num2))) 
        elif opcionSeleccionada == '4':
            print(" La división es: "+ str(divisionFunc(num1, num2))) 
        else:
            print("Opción no válida.")

        opcionSeleccionada = Menu()
    print("Adiós, gracias por usar la calculadora")  