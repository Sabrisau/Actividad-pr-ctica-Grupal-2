# Proyecto Autenticación y Autorización

Este proyecto es una aplicación web desarrollada en Django que permite gestionar tareas. Los usuarios pueden registrarse, iniciar sesión, crear nuevas tareas y visualizar el contenido de las mismas. La aplicación también incluye permisos personalizados y protección contra ataques CSRF.

# Requisitos previos
Antes de comenzar, asegúrate de tener instalados las siguientes herramientas:

-Python: En su version 3.10
-Git: Para clonar el repositorio remoto, asegúrate de tener Git instalado.

## Instrucciones de instalación

### 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local. En una ubicación deseada, abre una terminal y ejecuta el siguiente comando:

`git clone <URL_DEL_REPOSITORIO>`

Se va a crear una carpeta practica-modelos dentro, que contendra el proyecto.

### 2. Crear y activar un entorno virtual

En una carpeta aparte del proyecto, ejecutar este comando:

`python -m venv env`

Para activar el entorno virtual:

En Windows: `env\Scripts\activate`
En Linux/macOS: `source env/bin/activate`

### 3. Instalar las dependencias

Moverse con el entorno virtual activado a la carpeta practica-modelos descargada del repositorio remoto, e instalar las dependencias del proyecto en el entorno virtual ejecutando el siguiente comando: 

`pip install -r requirements.txt`

### 4. Migraciones de base de datos

Ejecutar inmediatamente este comando para ejecutar la migración inicial:

`python manage.py migrate`

### 5. Ejecuta el servidor de desarrollo:

python manage.py runserver


## Características

-Autenticación de Usuarios: Los usuarios pueden registrarse e iniciar sesión en el sistema.
-Gestión de Tareas: Los usuarios con permisos pueden crear nuevas tareas.
-Protección CSRF: Se utiliza el token CSRF en los formularios para proteger las solicitudes POST y evitar ataques de falsificación.
-Permisos Personalizados: Los permisos de creación están restringidos a ciertos roles.
