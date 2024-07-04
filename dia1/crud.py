import os
import tabulate
import time

lista_alumnos = [
  {
    'nombre': 'Cesar Mayta',
    'email': 'nataly@gmail.com',
    'celular': '5556565'
  }
]

ANCHO = 50
opcion = 0
while(opcion < 5):
  os.system("clear")
  print("="*ANCHO)
  print("" * 10 + " CRUD alumnos")
  print("="*ANCHO)
  print("""
        [1] REGISTRAR ALUMNO
        [2] MOSTRAR ALUMNO
        [3] ACTUALIZAR ALUMNO
        [4] ELIMINAR ALUMNO
        """)
  print("="*ANCHO)
  opcion = int(input("INGRESE OPCIÓN: "))
  os.system("clear")
  print(f"selecciono opción {opcion}")
  time.sleep(1)