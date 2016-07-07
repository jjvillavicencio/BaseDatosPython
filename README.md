# Python (Conectividad a Base de Datos)

**Integrantes:**
- Jackson Masache
- Vanessa Sotomayor
- John Villavicencio

> Indice
> 1. [¿Qué es Python?](#1.-¿qué-es-python?)
> 2. [Características del lenguaje](#2.-características-del-lenguaje)
> 3. [¿Python y bases de datos?](#3.-¿python-y-bases-de-datos?)
> 4. [Conectividad con MySQL](#4.-conectividad-con-mysql)
> 5. [Pasos para instalar MySQLbd](#5.-pasos-para-instalar-mysqlbd)
> 6. [Conexión a Postgres con Python](#6.-conexión-a-postgres-con-python)

## 1. ¿Qué es Python?
Es un lenguaje de programación de alto nivel, interpretado y multipropósito. En los últimos años su utilización ha ido constantemente creciendo y en la actualidad es uno de los lenguajes de programación más empleados para el desarrollo de software.

Python puede ser utilizado en diversas plataformas y sistemas operativos, entre los que podemos destacar los más populares, cómo Windows, Mac OS X y Linux. Pero, además, Python también puede funcionar en smartphones, Nokia desarrolló un intérprete de esté lenguaje para su sistema operativo Symbian.

**¿Tiene Python un ámbito específico?** Algunos lenguajes de programación sí que lo tienen. Por ejemplo, PHP fue ideado para desarrollar aplicaciones Web. Sin embargo, esté no es el caso de Python. Con este lenguaje podemos desarrollar software para aplicaciones científicas, para comunicaciones de red, para aplicaciones de escritorio con interfaz gráfica de usuario (GUI), para crear juegos, para smartphones y por supuesto, para aplicaciones web.

## 2. Características del lenguaje
- Propósito general
- Multiplataforma
- Interpretado
- Interactivo
- Funciones y librerías
- Sintaxis clara

## 3. ¿Python y bases de datos?

El estándar de Python para las interfaces de bases de datos es el Python DB-API. La mayoría de las interfaces de bases de datos de Python se adhieren a este estándar, por lo que dicho API es compatible con una amplia gama de servidores de bases de datos, entre ellos:

- GadFly
- **MySQL**
- **PostgreSQL**
- Microsoft SQL Server 2000
- Informix
- Interbase
- Oracle
- Sybase

## 4. Conectividad con MySQL

Python utiliza una interfaz MySQLdb para la conexión a un servidor de base de datos MySQL.
Con este API de Python podremos crear tablas, insertar, obtener, modificar y eliminar registros de la base de datos.

## 5. Pasos para instalar MySQLbd

a) Confirmamos que no tenemos instalado MySQLdb en nuestras máquinas. Creemos un script con lo siguiente y lo ejecutamos:

![Imgur](http://i.imgur.com/lp0mV85.png)

b) Si se produce el siguiente error entonces significa que el módulo de MySQLdb no está instalado en nuestra máquina:

![Imgur](http://i.imgur.com/UGynNrY.png)

c) La manera más sencilla para instalar el módulo de MySQLdb es ejecutando el siguiente comando:

![Imgur](http://i.imgur.com/mTtCqqq.png)

d) Conexión con la base de datos: Antes de conectarnos a una base de datos en MySQL asegúrate de cumplir con lo siguiente:

- Haber creado una base de datos llamada prueba_db.
- Haber creado un usuario de conexión que posea las siguientes características:usuario: root y clave: root.

![Imgur](http://i.imgur.com/7zrIU3a.png)

Observemos que un objeto de conexión fue retornado una vez que se estableció una conexión exitosa con la base de datos, este objeto se asignó a la variable bd. Luego, esta variable bd es usada para crear un cursor, el cual es el medio por donde podemos ejecutar queries SQL. En nuestro caso ejecutamos SELECT VERSION(), dicho Query retorna la versión de la base de datos. Por último, cerramos la sesión establecida con la base de datos para así no gastar recursos.

e) Crear una tabla
Una vez que sabemos cómo establecer una conexión con la base de datos, estamos listos para crear tablas en la base de datos utilizando el método execute del cursor que creamos anteriormente. Veamos cómo crear una tabla denominada empleado dentro de nuestra base de datos:

![Imgur](http://i.imgur.com/AmaARPp.png)

Observemos que a través del método execute del cursor podemos ejecutar cualquier tipo de query que deseemos, en este caso un CREATE.

f) Insertar Datos:

![Imgur](http://i.imgur.com/owLHhF4.png)

Observemos que para que los cambios sean efectuados en la base de datos es necesario usar `bd.commit()`. Si queremos reversar los cambios efectuados podemos usar `bd.rollback()`.

g) Realizar consultas: Veamos los métodos mas usados a la hora de ejecutar un lectura en la base de datos desde Python:

fetchone() - Este método obtiene la primera fila de un conjunto de resultados de una consulta a la BD.
fetchall() - Este método obtiene todos los registros de un conjunto de resultados de una consulta a la BD.
rowcount - Este es un atributo de sólo lectura y devuelve el número de filas afectadas por el método execute.

![Imgur](http://i.imgur.com/30lD0if.png)

h) Actualizar Datos: La operación actualización significa actualizar uno o más registros que ya están disponibles en la base de datos

![Imgur](http://i.imgur.com/8YgT3S8.png)

i) Eliminar datos: La operación eliminar es necesario si desea eliminar uno o varios registros de la base de datos.

![Imgur](http://i.imgur.com/0PC8kGz.png)

## 6. Conexión a Postgres con Python

a) Importar librerías
Importamos las librerías que nos permiten trabajar con postgres.
Hacemos una conexión a la base de datos, usando la librería importada.

![Imgur](http://i.imgur.com/ch3k1xH.png)

b) Consultas a la base

- Creamos el cursor para poder obtener y hacer la consulta de datos.
- Creamos las sentencias para las consultas hacia la base de datos.

![Imgur](http://i.imgur.com/6akNRIt.png)

c) Presentar consultas

![Imgur](http://i.imgur.com/L8fZ5Ot.png)

Creamos la sentencia para la presentación de las consultas.
Ejecutamos nuestro script de python en la consola y podremos observar los resultados.

![Imgur](http://i.imgur.com/Vqc5qv8.png)
