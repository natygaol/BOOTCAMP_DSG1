import os
import tabulate
import time
import mysql.connector

lista_empresas = []
ANCHO = 50
opcion = 0



def mostrar_menu(ancho):
    print("="*ancho)
    print(" " * 10 + "CRUD DE EMPRESAS")
    print("="*ancho)
    print("""
         [1] REGISTRAR EMPRESAS
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESAS
         [4] ELIMINAR EMPRESAS
         [5] SALIR
          """)
    print("="*ancho)


############### BASE DE DATOS ############
def conectar_bd():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='db_codigo'
    )

def consultar_empresas():
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)
    query = "select id,ruc,razon_social,direccion from tbl_empresa"
    cursor.execute(query)
    empresas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return empresas

def insertar_empresa(ruc,razon_social,direccion):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "insert into tbl_empresa(ruc,razon_social,direccion) values (%s,%s,%s)"
    cursor.execute(query,(ruc,razon_social,direccion))
    conexion.commit()
    cursor.close()
    conexion.close()


def buscar_empresa(valor_busqueda):
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)
    query = "select * from tbl_empresa where razon_social = %s"
    cursor.execute(query,(valor_busqueda,))
    empresa = cursor.fetchone()
    cursor.close()
    conexion.close()
    return empresa

def actualizar_empresa(id,ruc,razon_social,direccion):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "UPDATE tbl_empresa SET ruc = %s,razon_social = %s, direccion = %s where id=%s"
    cursor.execute(query,(ruc,razon_social,direccion,id))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_empresa(id):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = 'DELETE FROM tbl_empresa WHERE id = %s'
    cursor.execute(query,(id,))
    conexion.commit()
    cursor.close()
    conexion.close()

while(opcion < 5):
    os.system("clear")
    mostrar_menu(ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if(opcion == 1):
        print("="*ANCHO)
        print(" " * 10 + "[1] REGISTRAR empresa")
        print("="*ANCHO)
        ruc = input("ruc : ")
        razon_social = input("razon_social : ")
        direccion = input("direccion : ")
        insertar_empresa(ruc,razon_social,direccion)
        print(" empresa REGISTRADO CON EXITO")
    elif(opcion == 2):
        print("="*ANCHO)
        print(" " * 10 + "[2] MOSTRAR empresaS")
        print("="*ANCHO)
        cabeceras = ["ID","ruc","razon_social","direccion"]
        lista_empresas = consultar_empresas()
        tabla = [empresa.values() for empresa in lista_empresas]
        print(tabulate.tabulate(tabla,headers=cabeceras,tablefmt="grid"))
        input("presione ENTER para continuar...")
    elif(opcion == 3):
        print("="*ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR empresa")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE razon_social de la EMPRESA A ACTUALIZAR :')
        empresa = buscar_empresa(valor_busqueda)
        if not empresa:
            print("NO SE ENCONTRO EL empresa SOLICITADO")
        else:
            print(f" empresa A ACTUALIZAR : {empresa['ruc']}")
            nuevo_ruc = input("ruc : ")
            nuevo_razon_social = input("razon_social : ")
            nuevo_direccion = input("direccion : ")
            actualizar_empresa(empresa['id'],nuevo_ruc,nuevo_razon_social,nuevo_direccion)
            print("empresa ACTUALIZADO CON EXITO...")
    elif(opcion == 4):
        print("="*ANCHO)
        print(" " * 10 + "[4] ELIMINAR empresa")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE razon_social de la EMPRESA A ELIMINAR :')
        empresa = buscar_empresa(valor_busqueda)
        if not empresa:
            print("NO SE ENCONTRO la empresa solicitada")
        else:
            eliminar_empresa(empresa['id'])
            print('Empresa ELIMINADO!!!')
    elif(opcion == 5):
        print("="*ANCHO)
        print(" " * 10 + "[5] SALIR")
        print("="*ANCHO)
    else:
        print("="*ANCHO)
        print(" " * 10 + "OPCIÓN INVALIDA!!!")
        print("="*ANCHO)
        
    time.sleep(1)