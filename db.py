import mysql.connector

miDb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Boldt1234',
    database='prueba'
)

cursor = miDb.cursor()

# cursor.execute('select * from usuario')  # query basica para traer todo
# cursor.execute('select * from usuario limit 1')  # query basica para traer todo
# resultado = cursor.fetchall()  # nos trae todos
# resultado2 = cursor.fetchone()  # nos trae el primero
# print(resultado)
# print(resultado2)

#cursor.execute('show create table usuario')
# resultado = cursor.fetchall()  # nos trae todos
# print(resultado)
#sql = 'insert into usuario (email, user_name, edad) values (%s, %s, %s)'
#values = ('micorreo@correo.com.nz', 'nombreusuario', 45)
#cursor.execute(sql, values)
# miDb.commit()  # toma los datos y ejecuta la consulta sql
# print(cursor.rowcount)

# actualizar
#sql = 'update usuario set email = %s where id= %s'
#values = ('minuevocorreo@gmail.com', 4)
#cursor.execute(sql, values)
# miDb.commit()

# eliminar
sql = 'delete from usuario where id = %s'
values = (2, )  # IMPORTANTE DEJAR LA COMA Y UN ESPACIO!
cursor.execute(sql, values)
miDb.commit()
