"""
Ejercicio: Organizar Archivos en Directorios Basados en la Fecha de Modificación

Lee todos los archivos en un directorio especificado.
Clasifica los archivos en subdirectorios según su fecha de modificación (año y mes).
Crea estos subdirectorios si no existen y mueve los archivos a las carpetas correspondientes.
"""
import os
from pathlib import Path
from datetime import datetime

def organizar_archivos_por_fecha(directorio_base):
    # Crear un objeto Path del directorio base
    ruta_base = Path(directorio_base)

    if not ruta_base.exists() or not ruta_base.is_dir():
        print(f"El directorio '{directorio_base}' no existe o no es válido.")
        return

    # Iterar sobre todos los archivos en el directorio base
    for archivo in ruta_base.iterdir():
        if archivo.is_file():
            # Obtener la fecha de modificación del archivo
            fecha_modificacion = datetime.fromtimestamp(archivo.stat().st_mtime)
            anio = fecha_modificacion.strftime('%Y')
            mes = fecha_modificacion.strftime('%m')

            # Crear el nombre del subdirectorio basado en año y mes
            subdirectorio = ruta_base / f"{anio}-{mes}"
            subdirectorio.mkdir(exist_ok=True)  # Crear el subdirectorio si no existe

            # Mover el archivo al subdirectorio correspondiente
            archivo.rename(subdirectorio / archivo.name)

    print(f"Archivos en '{directorio_base}' organizados por fecha de modificación.")

# Ejemplo de uso
organizar_archivos_por_fecha('../CLASE 6')
