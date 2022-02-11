###### Alan Aragón Lancharro
```shell
██████╗      ██╗ █████╗ ███╗   ██╗ ██████╗  ██████╗
██╔══██╗     ██║██╔══██╗████╗  ██║██╔════╝ ██╔═══██╗
██║  ██║     ██║███████║██╔██╗ ██║██║  ███╗██║   ██║
██║  ██║██   ██║██╔══██║██║╚██╗██║██║   ██║██║   ██║
██████╔╝╚█████╔╝██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝
╚═════╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝

Preview markdown (^k + v)
```
# _Guía básica de instalación/configuración de DJANGO_

-----------------------------------------------------------
Configurar en Visual Studio Code, opcional.

### Extensiones
- [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)
- [Markdown Preview Github Styling](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-preview-github-styles)
- [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)
- [Monokai Pro](https://marketplace.visualstudio.com/items?itemName=monokai.theme-monokai-pro-vscode)

### `^_P` Preferencias
- **Métodos abreviados de teclado**
	- `^q`	Des/Comentar
	- `F1`	Des/Plegar
- **Abrir atajos de teclado (JSON)**
	- _Pasar de **pestañas** en modo normal._
		- Añadir al final.
		```JSON
		[
	    // ...
    	{
        	"key": "ctrl+tab",
        	"command": "workbench.action.nextEditor"
    	},
    	{
        	"key": "ctrl+shift+tab",
        	"command": "workbench.action.previousEditor"
    	}
		]
		```

#### **Leyenda**
_Esto lo uso para mis apuntes, no tiene nada que ver con el código._
- `^` Control
- `_` Shift
- `~` Alt
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
python .\manage.py tailwind start

# Go to http://127.0.0.1:8000/
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
# Con el usuario en el comando.
python manage.py createsuperuser --username admin
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

python manage.py createsuperuser --username admin
```
#### Nota
Si hemos borrado la BD tenemos que crear la [contraseña de administrador](#ADMIN-panel) nuevamente.

-----------------------------------------------------------
# [static](https://docs.djangoproject.com/es/3.2/intro/tutorial06/#customize-your-app-s-look-and-feel)

## CSS
Se crea la carpeta `static` dentro del proyecto y luego la hoja de estilos dentro de `static/css/style.css`.
Para incluir el CSS en el template añadimos esta línea en la etiqueta `<head>`.
```django
	<!-- Con esta línea incluimos los ficheros estáticos -->
	{% load static %}

	<!-- Des esta forma accedemos a ellos -->
	<link rel="stylesheet" href="{% static 'css/style.css' %}" />
```

## TAILWIND
- [Docs](https://pypi.org/project/django-tailwind/#description)
- [Guía de instalación](https://django-tailwind.readthedocs.io/en/latest/installation.html)

Gesión de CSS mediante clases.
### 1. Instalar
```shell
pip install django-tailwind
```
### 2. `settings.py`
Añadir a `INSTALLED_APPS`.
```python
INSTALLED_APPS=[
	# ...
	'tailwind',
]
```
### 3. Crear Tailwind CSS compatible Django.
```shell
python manage.py tailwind init
# Nombre de la aplicación (theme, por defecto).
theme
# Modo. Se puede cambiar después.
1 - just in time (jit)
```
### 4. `settings.py` Añadir aplicación.
Agregamos `theme` a `INSTALLED_APPS`.
```python
INSTALLED_APPS = [
	# ...
	'tailwind',
	'theme'
]
```
### 5. `settings.py` Añadir el nombre de la app en tailwind.
Registramos el tema en la configuración de django.
```python
TAILWIND_APP_NAME='theme'
```
### 6. `settings.py` IP
```python
INTERNAL_IPS=[
	"127.0.0.1",
]
```
### 7. Instalar en nuestro proyecto.
```shell
python manage.py tailwind install
```

#### ❌ Posible error
```bash
CommandError: 
It looks like node.js and/or npm is not installed or cannot be found.
```
#### ✔ Solución
Debe estar instalado `npm` y definido en el `PATH` o bien en el fichero `settings.py`.
- [Guía instalación NPM](https://parzibyte.me/blog/2018/09/27/instalar-npm-node-js-windows/)

```python
# Linux
NPM_BIN_PATH='/usr/local/bin/npm'

# Windows
NPM_BIN_PATH=r"C:\Program Files\nodejs\npm.cmd"
```
### 8. `base.html` Template.
Tailwind instala una plantilla en la ruta `tailwind_app_name/templates/base.html`.
### 9. Si no usas `base.html` que incluye tailwind en tus ficheros.
Añade `{% tailwind_css %}` a tu fichero `base.html`.
```django
{% load tailwind_tags %}
...
<head>
   ...
   {% tailwind_css %}
   ...
</head>
```
### 10. Ejecutar
Una vez seguimos todos los pasos ejecutamos con.
```shell
python manage.py tailwind start
```
#### ❌ Posible error
```bash
"npm" no reconocido como comando interno o externo.
```
#### ✔ Solución
- [Variable de entorno](https://bertofern.wordpress.com/2019/01/08/solucion-node-js-npm-no-reconocido-como-comando-interno-o-externo/)
-----------------------------------------------------------
# 🏷 TAG
Dentro de nuestros ficheros html podremos introducir **tag** de django.
Algo similar a `<?php ... ?>`

## `{% comment %} ... {% endcomment %}`
Comentario

## `{% load static  %}`
Para cargar los ficheros estáticos (css, img, j, ...)

## `{% static 'css/style.css' %}`
Devuelve la ruta del fichero indicado, previemante se debe cargar con el tag anterior (`load`)
```html
<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
```

## `{% extends 'plantillaBase.html' %}`
Hereda la plantilla. Se introduce antes de `block` a la hora de definir el contenido.
_Siempre es la primera etiqueta_

## `{% block blockName %}{% endblock blockName %}`
Según donde los usemos, definen o cargan el contenido del bloque.
- `plantillaBase.html`, indica donde irá el contenido.
- `Templates`, que se mostrará.

## `{% url 'nameUrls' %}`
Ruta de la URL, obtine el atributo `name` del fichero `urls.py`

## `{% for ... %}`
```django
{% for line in listado %}
	{{line.value}}
{% endfor %}
```

## `{% if user.is_authenticated %}`
Mostrar diferente contenido si un usuario ha iniciado sesión.

## `{% csrf_token %}`
Dentro de un formulario, parsea los valores.

Luego los recepcionamos en la `view.py`.
```python
if form.is_valid():
	print(_form.cleaned_data)
	print(_form.cleaned_data.get("campo"))
```

-----------------------------------------------------------
# ✉️ Configurar envío EMAIL
En este ejemplo se configura un formulario de contacto.

## GMAIL
### 1. `settings.py` Configurar la cuenta de correo.
```python
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='Correo@gmail.com'
EMAIL_HOST_PASSWORD='Contraseña'
EMAIL_PORT=587
EMAIL_USE_TLS=True
```
### 2. `models.py` Crear el modelo.
```python
from django.db import models
from django.forms.fields import EmailField

MOTIVOS=[
	('REC','Recomendación'),
	('PET','Petición'),
	('ERR','Error'),
]
class Contact(models.Model):
	name=models.CharField(max_length=200, null=True, blank=True)
	email=models.EmailField(max_length=254, null=False, blank=False)
	motivo=models.CharField(max_length=3,choices=MOTIVOS)
	msg=models.TextField(null=False, blank=False)
```
### 3. `forms.py` Formulario basado en el modelo.
```python
from .models import *

class ContactFormWEB(forms.Form):
  name=forms.CharField(max_length=200, required=False)
  email=forms.EmailField()
  motivo=forms.CharField(
    max_length=3,
    widget=forms.Select(choices=MOTIVOS)
  )
  mensaje=forms.CharField(widget=forms.Textarea)
```
### 4. `views.py` Aquí valida, envía email y guarda en la BD.
```python
def contact(request):
	context={"title_":"CONTACT"}
	form=ContactFormWEB(request.POST or None)
	context.update({'form_':form})
	if form.is_valid():
		form_data=form.cleaned_data
		Contact.objects.create(
			name=form_data.get('name'),
			email=form_data.get('email'),
			motivo=form_data.get('motivo'),
			msg=form_data.get('mensaje'))

		msg="{} ({})\n\n{}".format(
			form_data.get('name'),
			form_data.get('email'),
			form_data.get('mensaje'),
		)
		send_mail(
			"Plantnet 🌿 "+form_data.get('motivo'),					# Asunto
			msg,																						# Cuerpo del mensaje
			settings.EMAIL_HOST_USER,												# From
			[settings.EMAIL_HOST_USER],											# To
			fail_silently=False
		)

		context.update({'send_':"✔ Mensaje enviado"})
		return render(request, "contact.html", context=context)
	return render(request, "contact.html", context=context)
```
### 5. `contact.html` Web html que mostrará el formulario
```django
{% extends 'base.html' %}
{% block title %}{{title_}}{% endblock title %}
{% block content %}

<h1>Formulario de contacto</h1>
<h2>{{send_}}</h2>
<form method="POST">
{{form_.as_p}}
{% csrf_token %}
<input type="submit" value="Enviar"/>
</form>

{% endblock content %}
```
### 6. `url.py`
```python
urlpatterns=[
	url(r'^contact/',						views.contact,				name="contact"),
]
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
- [Login & Logout](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
- [Forms0](https://www.webforefront.com/django/formfieldtypesandvalidation.html)
- [Forms1](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/)
- [DJANGO GMAIL](https://dev.to/abderrahmanemustapha/how-to-send-email-with-django-and-gmail-in-production-the-right-way-24ab)

# Cheatsheets
## [DJANGO](https://docs.djangoproject.com/en/3.2/)
- [Django Models Cheat Sheet by lewiseason](https://cheatography.com/lewiseason/cheat-sheets/django-models/)
- [Cheatsheet for Django Models by Jack Linke](https://jacklinke.com/cheatsheet-for-django-models)ema Configurar EMAIL

## [TAILWIND](https://tailwindcss.com/docs)
- [cheatsheet0](https://tailwindcomponents.com/cheatsheet/)
- [cheatsheet1](https://nerdcave.com/tailwind-cheat-sheet)