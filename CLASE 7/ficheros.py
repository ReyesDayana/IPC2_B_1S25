"""

Ejercicio: Procesar y Clasificar Contenido de un Archivo de Texto
Descripción: En este ejercicio, se escribirá un script en Python que:

Abre un archivo de texto llamado texto_entrada.txt.
Lee el contenido línea por línea.
Realiza un análisis y clasificación del contenido, incluyendo:
Contar cuántas líneas comienzan con una vocal y cuántas comienzan con una consonante.
Contar el número de líneas que contienen números.
Identificar si hay líneas completamente en mayúsculas.
Escribe un resumen detallado en un nuevo archivo llamado reporte_analisis.txt.
"""

def comienza_con_vocal(linea):
    return linea[0].lower() in "aeiou"

with open('texto_entrada.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()  

lineas_con_vocal = 0
lineas_con_consonante = 0
lineas_con_numeros = 0
lineas_en_mayusculas = []

for linea in lineas: 
    linea_strip = linea.strip()
    if not linea_strip:
        continue

    if comienza_con_vocal(linea_strip):
        lineas_con_vocal += 1
    else:
        lineas_con_consonante += 1

    if any(caracter.isdigit() for caracter in linea_strip):
        lineas_con_numeros += 1

    if linea_strip.isupper():
        lineas_en_mayusculas.append(linea_strip)

    with open('reporte_analisis.txt', 'w', encoding='utf-8') as archivo_reporte:
        archivo_reporte.write("Reporte del Archivo texto entrada\n")
        archivo_reporte.write(f"Numero de lineas que comienzan con una vocal {lineas_con_vocal}\n")
        archivo_reporte.write(f"Numero de lineas que comienzan con una consonante {lineas_con_consonante}\n")
        archivo_reporte.write(f"Número de líneas que contienen números: {lineas_con_numeros}\n")
        archivo_reporte.write("Líneas completamente en mayúsculas:\n")
        for linea in lineas_en_mayusculas:
            archivo_reporte.write(f"- {linea}\n")

print("El reporte ha sido escrito en 'reporte_analisis.txt'.")
        

