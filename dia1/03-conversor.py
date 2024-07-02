def casa_de_cambio():
    print("Hola! Bienvenido a casa de cambio García, por favor elige una de estas opciones:")
    print("Opción 1: cambiar de soles a dólares (TC: 3.818)")
    print("Opción 2: cambiar de dólares a soles (TC: 3.852)")
    
    opcion = input("Elige una opción (1 o 2): ")
    
    if opcion == "1":
        soles = float(input("Cuántos soles vas a enviar? "))
        dolares = soles / 3.818
        print(f"El total en dólares es {dolares:.2f}")
    elif opcion == "2":
        dolares = float(input("Cuántos dólares vas a enviar? "))
        soles = dolares * 3.852
        print(f"El total en soles es {soles:.2f}")
    else:
        print("Opción no válida.")
    
    print("Muchas gracias por confiar en casa de cambio García")

casa_de_cambio()
