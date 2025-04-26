# Comandos para django
## Entorno virtual
Usamos un entorno virtual para evitar conflictos entre las versiones de los paquetes de python que estemos utilizando.

```bash
python -m venv entorno
```
### Activar entorno
1. En la carpeta de entorno entrar a Scripts
2. Abrir una terminal
3. Utilizar el comando
```bash
activate
```
4. Entre parentesis saldra el nombre del entorno

## Instalar django
Con el entorno activado regresar a la carpeta prinicpal e instalar django
```bash
cd ..
cd ..
pip install django
```

## Iniciar proyecto en django
```bash
django-admin startproject clase10
```

## Ejecutar proyecto en django
```bash
cd clase10
python manage.py runserver
```
## Crear una app
```bash
python manage.py startapp usuarios
```
## Hacer migraciones
Estos comandos sirven para guardar y crear el modelo
```bash
python manage.py makemigrations
python manage.py migrate
```

## Agregar Productos desde la shell
```bash
python manage.py shell

from productos.models import Producto

producto1 = Producto(nombre='Laptop', precio=1000.00)
producto1.save()

producto2 = Producto(nombre='Smartphone', precio=500.00)
producto2.save()

producto3 = Producto(nombre='Tablet', precio=300.00)
producto3.save()

```