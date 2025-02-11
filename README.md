# Instrucciones

## Clonar proyecto
Ejecuten este comando:
```
git clone https://github.com/MauSeptim/FastApiPractica
```

vayanse a esa carpeta en la terminal con el comando cd
```
cd FastApiPractica
```

Una vez clonado y lo tengan en su compu, si quieren ejecutar este proyecto necesitaran modificar los siguientes archivos:

* .env
* alembic.ini

La razon de esto es porque ahi tendran que cambiar ustedes mismos la url de la base de datos, en el caso de ``.env`` la cambian con la db que ustedes crearon, usuario, contraseña etc.
Pero en ``alembic.ini`` tienen que encontrar esta linea: 
```
sqlalchemy.url = mysql+mysqlconnector://usuario_de_sql:contraseña@localhost:puerto_de_sql/nombre_de_db
```
Lo sustituyen con lo mismo que ya pusieron en **.env** y deberia de funcionarles :)


## Crear entorno virtual
Para poder ejecutar el backend y que las dependencias se instalen solo en nuestra carpeta de proyecto necesitamos crear nuestro entorno virtual.
Les creara una carpeta dependiendo del nombre que le pongan, en este caso le ponemos "venv" por convención :)

### crear entorno virtual WINDOWS
```
python -m venv venv
```

### crear entorno virtual LINUX
```
python3 -m venv venv
```

## Activar entorno virtual
Para poder seleccionar el entorno virtual necesitamos ejecutar los siguientes comandos, cabe destacar que si lo hacen en Visual Studio Code es posible
que les pregunte si quieren seleccionarlo o algo asi, le dan que si.

Para poder ejecutar el backend o instalar dependencias SIEMPRE tengan activo el entorno virtual antes de hacerlo pls

### WINDOWS
```
venv\Scripts\activate
```

### LINUX
```
source venv/bin/activate
```

## Instalación de dependencias para el backend FastAPI
Para instalar las dependencias, en el repo pueden ver un archivo "requirements.txt" ahi ya vienen todas las dependencias que ocupamos, y como lo tenemos en un txt
en un solo comando pueden instalarse todo. El cual es este:
```
pip install -r requirements.txt
```

## Cargar las tablas del backend a su MySql
Una vez tengan las dependencias, los archivos configurados y todo correctamente ejecutaran el siguiente comando para cargar las tablas a su db local
```
alembic upgrade head
```

## Correr el backend
finalmente en la terminal vayanse a la carpeta del microservicio, si mal no me equivoco es Usuarios/ y ahi ejecutan el siguiente comando:
```
uvicorn main:app --reload
```


