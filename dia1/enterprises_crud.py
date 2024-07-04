import os
import tabulate
import time

lista_empresas = [
    {
        'ruc':'1045551110',
        'razonSocial':'Nataly Garcia',
        'direccion':'pokedex xD'
    }
]
ANCHO = 50
opcion = 0
while(opcion < 5):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "CRUD DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESA
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("="*ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if(opcion == 1):
        print("="*ANCHO)
        print(" " * 10 + "[1] REGISTRAR EMPRESA")
        print("="*ANCHO)
        ruc = input("RUC : ")
        razonSocial = input("Razon Social : ")
        direccion = input("direccion : ")
        dic_nueva_empresa = {
            'ruc':ruc,
            'razonSocial':razonSocial,
            'direccion':direccion
        }
        lista_empresas.append(dic_nueva_empresa)
        print(" EMPRESA REGISTRADO CON EXITO")
    elif(opcion == 2):
        print("="*ANCHO)
        print(" " * 10 + "[2] MOSTRAR EMPRESAS")
        print("="*ANCHO)
        cabeceras = ["RUC","RAZON SOCIAL","DIRECCION"]
        tabla = [empresa.values() for empresa in lista_empresas]
        print(tabulate.tabulate(tabla,headers=cabeceras,tablefmt="grid"))
        input("presione ENTER para continuar...")
    elif(opcion == 3):
        print("="*ANCHO)
        print(" " * 10 + "[3] ACTUALIZAR EMPRESA")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE RAZON SOCIAL DEL EMPRESA A ACTUALIZAR :')
        posicion_busqueda = -1
        for posicion in range(len(lista_empresas)):
            dic_empresa = lista_empresas[posicion]
            if valor_busqueda in dic_empresa.values():
                posicion_busqueda = posicion
                break
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO EL EMPRESA SOLICITADO")
        else:
            print(f' EMPRESA A ACTUALIZAR : {lista_empresas[posicion_busqueda].get("razonSocial")}')
            nuevo_ruc = input("RUC : ")
            nueva_rs = input("RAZON SOCIAL : ")
            nueva_direccion = input("DIRECCION : ")
            dic_actualizar_empresa = {
                'ruc': nuevo_ruc,
                'razonSocial': nueva_rs,
                'direccion': nueva_direccion
            }
            lista_empresas[posicion_busqueda] = dic_actualizar_empresa
        print("EMPRESA ACTUALIZADO CON EXITO...")
    elif(opcion == 4):
        print("="*ANCHO)
        print(" " * 10 + "[4] ELIMINAR EMPRESA")
        print("="*ANCHO)
        valor_busqueda = input('INGRESE RAZON SOCIAL DEL EMPRESA A ELIMINAR :')
        posicion_busqueda = -1
        for posicion in range(len(lista_empresas)):
            dic_empresa = lista_empresas[posicion]
            if valor_busqueda in dic_empresa.values():
                posicion_busqueda = posicion
                break
        if posicion_busqueda == -1:
            print("NO SE ENCONTRO EL EMPRESA SOLICITADO")
        else:
            lista_empresas.pop(posicion_busqueda)
            print('EMPRESA ELIMINADA!!!')
    elif(opcion == 5):
        print("="*ANCHO)
        print(" " * 10 + "[5] SALIR")
        print("="*ANCHO)
    else:
        print("="*ANCHO)
        print(" " * 10 + "OPCIÓN INVALIDA!!!")
        print("="*ANCHO)
        
    time.sleep(1)