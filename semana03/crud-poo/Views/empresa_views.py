import os
import time
import tabulate
from DAO.empresa_dao import EmpresaDAO
from Models.empresa_models import Empresa

class EmpresaViews:
    ANCHO = 50

    def __init__(self):
        self.dao = EmpresaDAO()
        self.opcion = 0

    def menu(self):
        while self.opcion != 5:
            os.system("clear")
            print("=" * self.ANCHO)
            print(" " * 10 + "PROGRAMA DE REGISTRO DE EMPRESAS")
            print("=" * self.ANCHO)
            print("""
                  [1] REGISTRAR EMPRESA
                  [2] MOSTRAR EMPRESAS
                  [3] ACTUALIZAR EMPRESA
                  [4] ELIMINAR EMPRESA
                  [5] SALIR
                  """)
            print("=" * self.ANCHO)

            self.opcion = int(input("INGRESE UNA OPCIÓN DEL MENU: "))

            os.system("clear")
            if self.opcion == 1:
                self.registrar_empresa()
            elif self.opcion == 2:
                self.mostrar_empresas()
            elif self.opcion == 3:
                self.actualizar_empresa()
            elif self.opcion == 4:
                self.eliminar_empresa()
            elif self.opcion == 5:
                print("=" * self.ANCHO)
                print(" " * 10 + "SALIENDO DEL SISTEMA....")
                print("=" * self.ANCHO)
            else:
                print("=" * self.ANCHO)
                print(" " * 10 + "OPCIÓN INVÁLIDA!!!!")
                print("=" * self.ANCHO)

            time.sleep(1)

    def registrar_empresa(self):
        print("=" * self.ANCHO)
        print(" " * 10 + "[1] REGISTRAR EMPRESA")
        print("=" * self.ANCHO)
        ruc = input("RUC : ")
        rs = input("RAZON SOCIAL :")
        direccion = input("DIRECCIÓN :")

        nueva_empresa = Empresa(ruc,rs,direccion)
        self.dao.registrar_empresa(nueva_empresa)

        print("=" * self.ANCHO)
        print(" " * 10 + "EMPRESA REGISTRADO CON ÉXITO")
        print("=" * self.ANCHO)

    def mostrar_empresas(self):
        print("=" * self.ANCHO)
        print(" " * 10 + "[2] MOSTRAR EMPRESAS")
        print("=" * self.ANCHO)
        empresas = self.dao.mostrar_empresas()
        cabeceras = ["RUC","RAZON SOCIAL","DIRECCION"]
        data = [[empresa.nombre,empresa.email,empresa.celular] for empresa in empresas]
        print(tabulate.tabulate(data,headers=cabeceras,tablefmt="grid"))
        input("presione ENTER para continuar...")

    def actualizar_empresa(self):
        print("=" * self.ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR EMPRESA")
        print("=" * self.ANCHO)
        rs = input('INGRESE LA RAZON SOCIAL DEL EMPRESA A ACTUALIZAR :')
        empresas = self.dao.mostrar_empresas()
        empresa_encontrada = None
        posicion_empresa = -1
        for i ,empresa in enumerate(empresas):
            if empresa.rs == rs:
                empresa_encontrada = empresa
                posicion_empresa = i
                break

        if not empresa_encontrada:
            print("NO SE ENCONTRO EL EMPRESA")
        else:
            print(f'EMPRESA A ACTUALIZAR {empresa_encontrada.ruc}')
            print('INGRESE LOS NUEVOS DATOS DE LA EMPRESA(SI PRESIONA ENTER NO SE ACTUALIZARÁ EL VALOR)')
            ruc = input(f'RUC ({empresa_encontrada.ruc}) :')
            if ruc == "":
                ruc = empresa_encontrada.ruc
            rs = input(f'RAZON SOCIAL ({empresa_encontrada.rs}) :')
            if rs == "":
                rs = empresa_encontrada.rs
            direccion = input(f'DIRECCION ({empresa_encontrada.direccion}) :')
            if direccion == "":
                direccion = empresa_encontrada.direccion

            empresa_actualizar = Empresa(ruc,rs,direccion)
            
            self.dao.actualizar_empresa(empresa_actualizar,posicion_empresa)
            print("=" * self.ANCHO)
            print(" " * 10 + "EMPRESA ACTUALIZADA CON ÉXITO!!!")
            print("=" * self.ANCHO)

        

    def eliminar_empresa(self):
        print("=" * self.ANCHO)
        print(" " * 10 + "[4] ELIMINAR EMPRESA")
        print("=" * self.ANCHO)
        rs = input('INGRESE LA RAZON SOCIAL DE LA EMPRESA A ELIMINAR :')
        posicion_empresa = -1
        for i ,empresa in enumerate(self.dao.mostrar_empresas()):
            if empresa.rs == rs:
                posicion_empresa = i
                break

        if posicion_empresa == -1:
            print("NO SE ENCONTRO EL EMPRESA A ELIMINAR")
        else:
            self.dao.eliminar_empresa(posicion_empresa)
            print("EMPRESA ELIMINADA!!!")