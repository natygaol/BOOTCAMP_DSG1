#ENTRADA
print("mi calculadora")
numero1 = input("numero 1: ")
numero2 = input("numero 2: ")
operacion = input("Ingrese el tipo de operación (suma|resta): ")
#PROCESO
if (operacion == 'suma'):
  resultado = int(numero1) + int(numero2)
elif (operacion == 'resta'):
  resultado = int(numero1) - int(numero2)
else:
  print(f"la operación {operacion} no existe")
  resultado = None
#SALIDA
if resultado is not None:
    print(f"El resultado es {resultado}")