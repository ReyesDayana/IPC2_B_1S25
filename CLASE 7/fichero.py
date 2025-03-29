"""
Ejercicio: Procesar y Analizar un Archivo de Texto
Descripción: Se va a crear un script en Python que:

Abre un archivo de texto llamado datos.txt.
Lee el contenido línea por línea y procesa los datos.
Realiza un análisis del contenido, incluyendo:
Contar cuántas líneas y palabras hay en total.
Identificar la línea más larga (en términos de número de palabras).
Calcular el número promedio de palabras por línea.
Escribe el resultado en un nuevo archivo llamado analisis.txt.
Cierra ambos archivos correctamente.
"""

with open('datos.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()

total_lineas = len(lineas)
total_palabras = 0
longitud_maxima = 0
linea_mas_larga = ""

for linea in lineas:
    palabras = linea.split()
    num_palabras = len(palabras)
    total_palabras += num_palabras


    if num_palabras > longitud_maxima:
        longitud_maxima = num_palabras
        linea_mas_larga = linea.strip()


promedio_palabras = total_palabras/ total_lineas if total_lineas > 0 else 0


with open('analisis.txt', 'w', encoding='utf-8') as archivo_analisis:
    archivo_analisis.write("Analisis del archivo\n")
    archivo_analisis.write(f"Número total de líneas: {total_lineas}\n")
    archivo_analisis.write(f"Número total de palabras: {total_palabras}\n")
    archivo_analisis.write(f"Promedio de palabras por línea: {promedio_palabras:.2f}\n")
    archivo_analisis.write(f"Línea más larga ({longitud_maxima} palabras): {linea_mas_larga}\n")

print("El análisis ha sido escrito en 'analisis.txt'.")