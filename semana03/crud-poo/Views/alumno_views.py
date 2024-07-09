import os
import time
import tabulate
from DAO.alumno_dao import AlumnoDAO
from Models.alumno_models import Alumno

class AlumnoViews:
    ANCHO = 50

    def __init__(self):
        self.dao = AlumnoDAO()
        self.opcion = 0

    def menu(self):
        while self.opcion != 5:
            os.system("clear")
            print("=" * self.ANCHO)
            print(" " * 10 + "PROGRAMA DE MATRICULA DE ALUMNOS")
            print("=" * self.ANCHO)
            print("""
                  [1] REGISTRAR ALUMNO
                  [2] MOSTRAR ALUMNOS
                  [3] ACTUALIZAR ALUMNO
                  [4] ELIMINAR ALUMNO
                  [5] SALIR
                  """)
            print("=" * self.ANCHO)

            self.opcion = int(input("INGRESE UNA OPCIÓN DEL MENU: "))