###### Alan Aragón Lancharro
```shell
██████╗      ██╗ █████╗ ███╗   ██╗ ██████╗  ██████╗ 
██╔══██╗     ██║██╔══██╗████╗  ██║██╔════╝ ██╔═══██╗
██║  ██║     ██║███████║██╔██╗ ██║██║  ███╗██║   ██║
██║  ██║██   ██║██╔══██║██║╚██╗██║██║   ██║██║   ██║
██████╔╝╚█████╔╝██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝
╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ 
```
# _Guía básica de instalación/configuración de DJANGO_

-----------------------------------------------------------
Configurar en Visual Studio Code
- Tema (**Monokai**)
- Atajo de teclado
	- (^q)	Des/Comentar 
	- (F1)	Des/Plegar

-----------------------------------------------------------
# INSTALACIÓN

## INSTALAR
### Linux
```shell
# Instalar python
sudo apt install python3 python3-dev
# Instalar pipenv
pip install pipenv
```
### Windows
Descargamos python desde su [web oficial](https://www.python.org/downloads/).
```bash
python -m pip install pipenv
```

## CREAR DIRECTORIO
### Linux y Windows
```shell
mkdir directorio && cd directorio`
```

## CREAR ENTORNO VIRTUAL
### Linux y Windows
```shell
python3 -m venv env
```
##### Nota
_Windows crea el entorno virtual en `.virtualenvs` dentro de la carpeta de usuario._

## ACTIVAR/INICIAR ENTORNO VIRTUAL
### Linux
```shell
source env/bin/activate
```
### Windows
```bash
pipenv shell
:: Exit :: para salir
```

## INSTALAR DJANGO
### Linux y Windows
```shell
pip install django
```

## VERSIÓN INSTALADA
### Linux y Windows
Ver paquetes instalados y su versión
```shell
pip freeze			
```


## NOTA
### Windows
Este comando instala y crea el entorno virtual en Windows.
```bash
pipenv install django
```


-----------------------------------------------------------
# CREAR UN NUEVO [PROYECTO](https://docs.djangoproject.com/es/3.2/intro/tutorial01/#creating-a-project)

### Linux y Windows
```shell
django-admin startproyect nombreDelProyecto
cd nombreDelProyecto
```

-----------------------------------------------------------
# CONFIGURACIÓN

_Son comandos en linux, en windows editar los mismos parámetros con notepad._
## Lenguaje y zona horaria.
### · [Timezone docs](https://docs.djangoproject.com/en/3.2/topics/i18n/timezones/)
```shell
nano learning/settings.py
#>>
LANGUAGE_CODE="es-ES"
TIME_ZONE="Europe/Madrid"
```
## Base de datos [opcional]
### · [SQL Docs](https://www.sqlite.org/about.html)
```shell
nano learning/settings.py
#>>
import os

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}
```
## Crear esquemas y tablas
Está en el directorio anterior, ponemos ( `../` o `..\` ) delante de `manage.py` o subimos un directrorio con `cd ..`

_Migrations are Django's way of updating the database schema according to the changes that you make to your models._

```shell
# Hace la migración sin realizar cambios en la BD.
python manage.py makemigrations
```
### Linux
```shell
./manage.py migrate
```
### Windows
```bash
python manage.py migrate
```


-----------------------------------------------------------
# CREAR [APP](https://docs.djangoproject.com/es/3.2/intro/tutorial01/#creating-the-polls-app)

Dentro del proyecto, esta será la web.
```shell
django-admin startapp nombreDeLaApp
cd nombreDeLaApp
```


-----------------------------------------------------------
# FICHEROS Y DIRECTORIOS

## PROYECTO
### views.py
Funciones que reciben el **request**. Aquí se indica donde está el fichero `.html` (**template**)
```python3
nano views.py
#>>
def miFuncion(request):
	return render(request, "home.html", context="value1": "World!"})
```

### urls.py
Recibe la URL/completa y la asocia con `views.py`
Este fichero está en el directorio del proyecto, pero es recomendable ternerlo en cada directorio de la app, para hacerlo más independiente. Para conseguir esto debemos modificar `urls.py` dentro del proyecto.

```python3
nano url.py
#>>
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
		path('', include('nombreDeLaApp.urls')),
]

```

Y creamos el fichero `urls.py` dentro del `nombreDeLaApp`.
```python
nano url.py
#>>
from django.urls import path
from . import views

urlpatterns=[
	path('', views.home, name="home"),	
]
```

### Pipfile
Se pueden definir comandos para ejecutarlos con `python manage.py`
```bash
[scripts]
server = "python manage.py runserver"
```

### setting.py
Fichero de configuración, que ya hemos modificado más arriba.
```python
# Muestra los errores, por defecto (True).
# * Recomendado poner en False para producción.
DEBUG=True 
```

#### ⚠️ Agregar el proyecto
Añadimos el nombre del proyecto a `INTALLED_APPS`
```shell
nano ../nombreDeLaApp/settings.py
#>>
INTALLED_APPS=[
	'nombreDeLaApp',
]
```


-----------------------------------------------------------
# [Arrancar el servidor](https://docs.djangoproject.com/es/3.2/intro/tutorial01/#the-development-server)

### Linux
```shell
./manage.py runserver
# Start the app - custom port
# python manage.py runserver 0.0.0.0:<your_port>
```
### Windows
```bash
pipenv manage.py runserver
:: Si hemos modificado Pipfile
pipenv run server
```
Ahora abrimos el navegador y revisamos si funciona.


-----------------------------------------------------------
# Ejecutar

### Linux
```shell
# Ir al directorio
source env/bin/activate
.manage.py runserver
```

### Windows
```bash
:: Ir al directorio
pipenv shell
python manager.py runserver
http://127.0.0.1:8000/
```


-----------------------------------------------------------
# [TEMPLATES](https://docs.djangoproject.com/es/3.2/intro/tutorial03/#use-the-template-system)

## Dentro de la app
### `templates`
Directorio que contiene los ficheros `html`.
```html
<!DOCTYPE html>
<html lang="es">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie-edge">
</head>
	<body>
		<h1>{{variable}}!</h1>
		<!-- Bucle 
		{% for blog in blogs %}
		<h3>{{blog.title}}</h3>
		<a href="learn/{{blog.id}}">Leer más</a>
		{% endfor %}
		-->
	</body>
</html>
```


-----------------------------------------------------------
# Trabajar con la BD [models.py](https://docs.djangoproject.com/es/3.2/intro/tutorial02/#creating-models)

- [🌐 Lista desplegable](https://docs.djangoproject.com/en/3.2/ref/models/fields/)
- [🌐 Fields (Tipos)](https://docs.djangoproject.com/en/3.1/ref/models/fields/#module-django.db.models.fields.related)
	- [🌐 imagefield](https://www.geeksforgeeks.org/imagefield-django-models/)
	- [🌐 foreignKey: on_delete](https://docs.djangoproject.com/en/3.1/ref/models/fields/#arguments)

## Configuración de modelo
Para manipular la BD crearemos modelos en el fichero `models.py`.

Modificamos el fichero models.py
```python
class Plant(models.Model):
	title		=models.CharField(max_length=200)
	content	=models.TextField()
```
## makemigrations
Generamos los ficheros SQL que se utilizarán para generar la BD.
```bash
python manage.py makemigrations plants
```
## migrate
Ejecutamos los cambios.
```bash
python manage.py migrate plants
```

Podemos ver la instrucción en SQL.
```bash
python manage.py sqlmigrate learn 0001
```
## Panel de administración
Para que aparezce en el panel de administración tenemos que configurar el fichero `admin.py`.
```python
from django.contrib import admin
from .models import Plants

# Register your models here.
admin.site.register(Plants)
```
## Relaciones ([Relationsship](https://docs.djangoproject.com/en/3.1/ref/models/fields/#module-django.db.models.fields.related))
```python
class nombreClase(models.Model):
	# ...
	claveForanea=models.ForeignKey(
		'campoClave',
		on_delete=models.CASCADE,
	)
	# ...
```
-----------------------------------------------------------
# ADMIN panel

Una vez tenemos todo lo anterior configurado podemos acceder al panel de administrador.

· http://127.0.0.1:8000/admin

#### Crear el usuario superuser
```bash
python manage.py createsuperuser
```
Introducir el nombre de usuario, correo y contraseña

-----------------------------------------------------------
# [SHELL](https://docs.djangoproject.com/es/3.2/intro/tutorial02/#playing-with-the-api)

```bash
python manage.py shell
>>>
```
```python
# Imports
from plants.models import Plant
# Muestra todos los registros
Post.objects.all()
# Muestra el primer registro
Post.objects.first()
# Por ID
Post.object.get(id=1)

# ADD # Añadir nuevo objeto
post=Post.objects.create(title="Tercer blog", content="Este es el contenido del tercer blog")

# MODIFY # Modificar
post.title="Tercer, el tercero"
# Guardar
post.save()

# DEL # Borrar
post.delete()

# EXIT # Salir
quit()
exit()
```
-----------------------------------------------------------
# Eliminar/Renovar migrations
- 🌐 [Resetting Django Migrations](https://www.techiediaries.com/resetting-django-migrations/)

Podemos hacerlo de dos formas.
## 1. Borrando la BD
Con esta forma nos aseguramos que ha funcionado porque creará todo de nuevo.

~~Eliminamos~~ **renombramos** la base de datos`db.sqlite3`. _Aconsejo renombrar para no perder los datos en ningún caso._

```shell
mv db.sqlite3 db.sqlite_old
```

## 2. Manteniendo la BD
```shell
python .\manage.py migrate --fake plants zero
```

Eliminamos los ficheros de migrations
```shell
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```

## Creamos nuevamente las migraciones y BD.
Una vez terminemos alguno de los dos pasos anteriores podemos continuar.
```shell
python manage.py makemigrations
python manage.py migrate
```
#### Nota
Si hemos borrado la BD tenemos que crear la [contraseña de administrador](#ADMIN-panel) nuevamente.

-----------------------------------------------------------
# [static](https://docs.djangoproject.com/es/3.2/intro/tutorial06/#customize-your-app-s-look-and-feel)

## CSS
Se crea la carpeta `static` dentro del proyecto y luego la hoja de estilos dentro.

`styles.css` Una hoja de estilos normal.

Para incluir el CSS en el template añadimos esta línea en la etiqueta `<head>`.
```html
	{% load static %}
	<link rel="stylesheet" href="{% static 'style.css' %}" />
```


-----------------------------------------------------------
# ❌ ERRORES

## Modelos
❌ Tras añadir campos a un modelo y añadirlos a la migración aparece el siguiente error.

`python manage.py makemigrations plants`
```python
You are trying to add a non-nullable field 'nameComun' to plant without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
```
### ✔ Solución
Depende el caso te conviene hacer alguna de estas opciones: 
- Provide a default value in your model.
- Provide a default during the migration process.
- Enable null values for that field.


-----------------------------------------------------------
# URLGRAFÍA

- [Primeros pasos DJANGO](https://medium.com/@devsar)
- [Curso DJANGO](https://www.udemy.com/course/curso-practico-django/learn/lecture/16468900?start=165#overview)
- [Guía rápida](https://www.codewithharry.com/blogpost/django-cheatsheet)
- [Plantillas](https://www.creative-tim.com/blog/django-templates/django-cheat-sheet-free-samples/)
- [Resetting Django Migrations](https://www.techiediaries.com/resetting-django-migrations/)

## Cheatsheets
- [Django Models Cheat Sheet by lewiseason](https://cheatography.com/lewiseason/cheat-sheets/django-models/)
- [Cheatsheet for Django Models by Jack Linke](https://jacklinke.com/cheatsheet-for-django-models)