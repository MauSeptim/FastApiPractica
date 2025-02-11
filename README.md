# Instrucciones

En el caso de quieran clonar este proyecto y ejecutarlo necesitaran modificar los siguientes archivos:

* .env
* alembic.ini

La razon de esto es porque ahi tendran que cambiar ustedes mismos la url de la base de datos, en el caso de ``.env`` la cambian con la db que ustedes crearon, usuario, contraseña etc.
Pero en ``alembic.ini`` tienen que encontrar esta linea: 
```
sqlalchemy.url = mysql+mysqlconnector://usuario_de_sql:contraseña@localhost:puerto_de_sql/nombre_de_db
```
Lo sustituyen con lo mismo que ya pusieron en **.env** y deberia de funcionarles :)
