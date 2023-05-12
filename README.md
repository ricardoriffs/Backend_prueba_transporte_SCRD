
# Ejecución del proyecto

## 1. Entorno virtual
    - Crear entrono virtual
    py -m venv venv
    - Activar entorno virtual
    .\venv\Scripts\activate

## 2. instalación de librerías con requirements.txt

    pip install -r requirements.txt

## 3. Modificar settings.py para conexión de base de datos

    Ir a la carpeta "transporte/transporte"
    Abrir el archivo "settings.py" y buscar la variable "DATABASE"
    modificar variables "name, user, password, host, port" de acuerdo a su base de datos

    Ejemplo: Archivo settings.py
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prueba-transporte',
        'USER': 'nombre usuario',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
    }
**Nota:** Django y su ORM se encargan de crear toda la estructura de la base de datos, y ya tiene definidas unas tablas para su control, debido a esto, no se genera un script sql a parte para generar la estructura de la base de datos, solo para crear la base de datos donde se va hacer la estructura dada por los modelos y Django


## 4. Hacer la migraciones de los modelos
    Ingresar a la carpeta transporte (principal), donde se encuentra el archivo manage.py
    py manage.py makemigrations

## 5. Correr las migraciones 
    py manage.py migrate

## 6. Correr servidor

    py manage.py runserver
 

# Librerías usadas

- Django: es un framework de alto nivel que fomenta el desarrollo rápido y el diseño limpio y pragmático
- Django rest framework:  es un potente y flexible conjunto de herramientas para construir APIs Web.
- psycopg2: Es la librería que nos ayuda a comunicarnos con la base de datos postgres
- django-cors-headers: nos ayuda a controlar los cors de una petición hecha por el cliente

### versiones
- asgiref==3.6.0
- Django==4.2.1
- django-cors-headers==4.0.0
- django-filter==23.2
- djangorestframework==3.14.0
- gunicorn==20.1.0
- psycopg2==2.9.6
- pytz==2023.3
- sqlparse==0.4.4
- tzdata==2023.3
- whitenoise==6.4.0


# Proceso de desarrollo 
- Se trabajo con Django y Django rest framework enfocado a clases para tener un código mas organizado y escalable. nos permiten tener mayor flexibilidad al momento de manejar las solicitudes y respuestas http. También nos favorece en aplicar el principio de responsabilidad única donde la clase o modulo solo debe tener una sola responsabilidad.   

## Requerimientos dados por el cliente
- Registrar los vehículos que se tienen disponibles para realizar los pedidos.
- Registrar los conductores que estan contratados por la empresa.
- Asociar un conductor a uno o varios vehículos. En este punto se espera que al tener un conductor seleccionado solo cargue los vehículos que NO tiene asignados para realizar la asignación.
- Desasociar un conductor de un vehículo. En este punto se espera que al tener un conductor seleccionado solo cargue los vehículos que YA han sido asignados previamente para quitar la asociación.
## Restricciones implícitas del dominio
- Un conductor no puede tener duplicidad de identificación
- Un vehículo no puede tener duplicidad en la placa
- Para asociar o desasociar un conductor a un vehículo, el conductor debe ser validado en la base de datos 
- Para asociar o desasociar un conductor de un vehículo, el vehículo debe ser validado en la base de datos 
