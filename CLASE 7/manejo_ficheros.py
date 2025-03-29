"""
Ejercicio: Buscar y Eliminar Archivos Duplicados en un Directorio
Recorre todos los archivos en un directorio y subdirectorios.
Identifica archivos duplicados basándose en su contenido.
Mueve los archivos duplicados a un subdirectorio llamado duplicados.

"""
import hashlib
from pathlib import Path


def obtener_hash_archivo(archivo_path):
    hasher = hashlib.sha256()
    with open(archivo_path, 'rb') as archivo:
       for bloque in iter(lambda: archivo.read(4096), b""):
            hasher.update(bloque)
    return hasher.hexdigest()

def buscar_y_eliminar_duplicados(directorio):
    ruta_base = Path(directorio)
    if not ruta_base.exists() or not ruta_base.is_dir():
        print(f"El directorio {directorio} no existe o no es valido")
        return
    hash_dict = {}
    duplicados_dir = ruta_base / "duplicados"
    duplicados_dir.mkdir(exist_ok=True)


    for archivo in ruta_base.rglob("*"):
        if archivo.is_file():
            archivo_hash = obtener_hash_archivo(archivo)
            if archivo_hash in hash_dict:
                print(f"Archivo duplicado encontrado {archivo.name}")
                archivo.rename(duplicados_dir / archivo.name)
            else:
                hash_dict[archivo_hash] = archivo
            print(f"Los archivos duplicados han sido movidos a {duplicados_dir}")

buscar_y_eliminar_duplicados('archivos')