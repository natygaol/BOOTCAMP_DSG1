def mostrar_menu(ancho):
    print("="*ancho)
    print(" " * 10 + "CRUD DE ALUMNOS")
    print("="*ancho)
    print("""
         [1] REGISTRAR ALUMNO
         [2] MOSTRAR ALUMOS
         [3] ACTUALIZAR ALUMNO
         [4] ELIMINAR ALUMNO
         [5] SALIR
          """)
    print("="*ancho)

def buscar_alumno(valor_busqueda, listado):
    posicion_busqueda = -1
    for posicion in range(len(listado)):
        dic_alumno = listado[posicion]
        if valor_busqueda in dic_alumno.values():
            posicion_busqueda = posicion
            break
    return posicion_busqueda