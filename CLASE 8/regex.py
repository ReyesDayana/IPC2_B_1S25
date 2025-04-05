import re

patron = r"hola"
cadena = "hola mundo"

resultado = re.search(patron, cadena)
if resultado:
    print(f"Se encontró el patron: {resultado}")
else:
    print("No se encontró el patron")

patron_inicio = r"^hola"
cadena = "mundo hola a todos"

if re.search(patron_inicio, cadena):
    print("La cadena empieza con hola")
else:
    print("La cadena no empieza con hola")


patron_final = r"mundo$"
cadena = "hola mundo como estan"
if re.search(patron_final, cadena):
    print("La cadena termina con mundo")
else:
    print("La cadena no termina con mundo")

patron = r"\b\w+\b"
cadena = "El sol brilla y el viento sopla"

resultados =  re.findall(patron, cadena)
print("Palabras encontradas:", resultados)

patron = r"\s+"
cadena = "Esta es una cadena con   espacios   en  blanco"
partes =  re.split(patron, cadena)
print("Partes de la cadena:", partes)

patron = r"mundo"
cadena = "Hola mundo, mundo, mundo!"
nueva_cadena =  re.sub(patron, "Python", cadena)
print("Cadena despues de la sustitución:", nueva_cadena)


patron = r"(\w+)@(\w+\.\w+)"
cadena = "dayanareyes@ejemplo.com"
resultado = re.search(patron, cadena)
if resultado:
    nombre = resultado.group(1)
    dominio = resultado.group(2)
    print(f"Nombre: {nombre}, Dominio: {dominio}")
else:
    print("No se encontró el patron")

# Formato del numero de telefono XXXX-XXXX
patron = r"^\d{4}-\d{4}$"
telefono = "12334-5678"
if re.match(patron, telefono):
    print("Numero de telefono valido")
else:
    print("numero de telefono invalido")


#Validar una contraseña
''''
Explicación del patrón:

Al menos una letra minúscula: (?=.*[a-z])
Al menos una letra mayúscula: (?=.*[A-Z])
Al menos un dígito: (?=.*\d)
Longitud mínima de 8 caracteres: [A-Za-z\d]{8,}
'''
patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
