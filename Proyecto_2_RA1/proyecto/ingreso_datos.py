# ingreso_datos.py
#Este modulo nos permite ingresar y validar datos
from modelo import Nino
from base_datos import registrar_nino
from departamentos import mostrar_departamentos, obtener_departamento

def ingresar_datos():
    print("\n[Ingreso de Datos]")#Definimos la funcion de los datos

    # Edad
    while True:
        try:
            edad = int(input("Edad (en meses, 0 a 24): "))
            #if edad >= 0 and edad <= 24:
            if 0 <= edad <= 24:
                break]#Si se cumplen los parametros termina y pasa a solicita el siguiente dato.
            else:
                print("Edad inválida. Debe estar entre 0 y 24 meses.")#Si se ingresa un dato invalido solicita ingresar el dato nuevamente
        except ValueError:
            print("Entrada inválida. Ingresa un número entero para la edad.")#Solicitas ingresar un numero entero para continuar.

    # Peso
    while True:
        try:
            peso = float(input("Peso (kg): "))#Solicitamos ingresar el peso en un numero entero
            if peso > 0:
                break#Si el peso es mayor a 0 entonces pasa al siguinte paso.
            else:
                print("Peso inválido. Debe ser un valor positivo.")#Valida si el dato ingresado es positivo
        except ValueError:
            print("Entrada inválida. Ingresa un número válido para el peso.")#De lo contrario solicita ingresar un valor positivo

    # Talla
    while True:
        try:
            talla = float(input("Talla (cm): "))#Solicitamos ingresar la talla del nino
            if talla > 0:
                break#Si la talla es mayor a 0 entnces pasar al siguinte paso 
            else:
                print("Talla inválida. Debe ser un valor positivo.")#Valida si el dato ingresado es positivo
        except ValueError:
            print("Entrada inválida. Ingresa un número válido para la talla.")#De lo contrario solicita ingresar un valor positivo

    # Perímetro craneal
    while True:
        try:
            craneo = float(input("Perímetro craneal (cm): "))#Solicitamnos ingresar el perimetro craneal del nino
            if craneo > 0:
                break#Si el valor ingresado es mayor a 0 entonces pasar al siguinte paso 
            else:
                print("Perímetro craneal inválido. Debe ser un valor positivo.")#Valida si el dato ingresado es positivo
        except ValueError:
            print("Entrada inválida. Ingresa un número válido para el perímetro craneal.")#De lo contrario solicita ingresar un valor positivo

    # Departamento
    departamento = None
    while departamento is None:
        mostrar_departamentos()#Desplegamos el menu de los departamentos
        opcion = input("Ingrese el número del departamento: ")#Solicitar al usuario que ingrese el numero del departamento al que corresponda
        departamento = obtener_departamento(opcion)
        if departamento is None:
            print("Opción inválida. Selecciona un número del listado.")#En caso de que se ingrese una opcion invalida solicitar nuevamente

    # Registrar al niño
    nino = Nino(edad, peso, talla, craneo, departamento)
    registrar_nino(nino)#Despues de validar los datos guardamos los datos
    print("\n✅ Niño registrado exitosamente.")

