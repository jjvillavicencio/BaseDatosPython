#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# Establecemos la conexión con la base de datos
bd = MySQLdb.connect("localhost","root","root","prueba_db" )

# Preparamos el cursor que nos va a ayudar a realizar las operaciones con la base de datos
cursor = bd.cursor()

# Preparamos el query SQL para eliminar al empleado
sql = "DELETE FROM EMPLEADO WHERE APELLIDO='Villavicencio'"
try:
   # Ejecutamos el comando
   cursor.execute(sql)
   # Efectuamos los cambios en la base de datos
   bd.commit()
   print "Cambios realizados!"
except:
   # Si se genero algún error revertamos la operación
   bd.rollback()
   print "Error al realizar cambios!"

# Nos desconectamos de la base de datos
bd.close()
