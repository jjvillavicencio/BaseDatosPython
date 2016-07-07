#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# Establecemos la conexión con la base de datos
bd = MySQLdb.connect("localhost","root","root","prueba_db" )

# Preparamos el cursor que nos va a ayudar a realizar las operaciones con la base de datos
cursor = bd.cursor()

# Preparamos el query SQL para insertar un registro en la BD
sql = "INSERT INTO EMPLEADO (\
		NOMBRE, APELLIDO, EDAD, SEXO, SALARIO)\
		VALUES ('John', 'Villavicencio', 22, 'M', 2000)"
try:
   # Ejecutamos el comando
   cursor.execute(sql)
   # Efectuamos los cambios en la base de datos
   bd.commit()
except:
   # Si se genero algún error revertamos la operación
   bd.rollback()

# Nos desconectamos de la base de datos
bd.close()
