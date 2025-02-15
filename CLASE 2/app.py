from empleado import Empleado
from persona import Persona

def Menu():
    print("-----------------Menu principal --------------------")
    print("1. Registrar persona")
    print("2. Registrar Empleado")
    print("3. Mostrar informacion")
    print("4. Opcion administrador")
    print("5. Salir")
    print("----------------------------------------------------")

if __name__ == '__main__':
    
    listado = []
    while True:
        Menu()
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            nombre = input('Ingrese el nombre: ')
            edad = int(input('Ingrese la edad: '))

            personaCreada = Persona(nombre, edad)
            listado.append(personaCreada)

        elif opcion == 2:
            nombre = input('Ingrese el nombre: ')
            edad = int(input('Ingrese la edad: '))
            salario = int(input("Ingrese su salario: "))
            empleadoCreado = Empleado(nombre,edad,salario)
            listado.append(empleadoCreado)

        elif opcion == 3:
            print("------IMPRESION DE DATOS--------")
            for elemento in listado:
                print(f'Nombre: {elemento.nombre}, edad: {elemento.edad}')
                if isinstance(elemento, Empleado):
                    print(elemento.trabajar())
                    print(elemento.cobrar())
                print("==========================")
        
        elif opcion== 4:
            print("Opcion administrador")
            print("Ingrese su usuario y contraseña")
            user = input("Ingrese su usuario ")
            password = input("Ingrese su contraseña ")

            if user == 'admin' and password == '1234':
                print("Bienvenido administrador")

                if len(listado) == 0:
                    print("no hay registros")
                    break
                else:
                    for obj in listado:
                        if isinstance(obj, Empleado):
                            userEmpl = input(f'Ingrese el usuario para {obj.nombre} ')
                            obj.setUserEmployee(userEmpl)
                            print("Asignacion completa")
                            print(obj.getUserEmployee())
            else:
                print("Usuario o contraseña incorrecta")
        elif opcion == 5:
            print("Gracias por usar el programa")
            break

        else:
            print("Opcion no valida")
                            