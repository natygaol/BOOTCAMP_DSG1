import mysql.connector

connection = mysql.connector.connect(user='root',password='root',host='localhost',database='db_codigo')
print('estas conectado a la bd')

#utiliza la sesion que he creado y abre una nueva ventana
alumnos_cursor = connection.cursor()

# alumnos_cursor.execute("insert into tbl_alumno(nombre,email,celular) values('ana garcia', 'ana@gmail.com', '59697')")
# connection.commit()
# print('alumno insertado')

alumnos_cursor.execute('select * from tbl_alumno')
# fetchall captura el resultado y lo guarda en una variable
resultado = alumnos_cursor.fetchall()
print(resultado)

for registro in resultado:
  print('*'*50)
  print(f"Nombre: {registro[1]}")
  print(f"Email: {registro[2]}")

connection.close()