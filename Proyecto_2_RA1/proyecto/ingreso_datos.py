# ingreso_datos.py

from modelo import Nino
from base_datos import registrar_nino
from departamentos import mostrar_departamentos, obtener_departamento

def ingresar_datos():
    print("\n[Ingreso de Datos]")

    # Edad
    while True:
        try:
            edad = int(input("Edad (en meses, 0 a 24): "))
            #if edad >= 0 and edad <= 24:
            if 0 <= edad <= 24:
                break
            else:
                print("Edad inválida. Debe estar entre 0 y 24 meses.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero para la edad.")

    # Peso
    while True:
        try:
            peso = float(input("Peso (kg): "))
            if peso > 0:
                break
            else:
                print("Peso inválido. Debe ser un valor positivo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido para el peso.")

    # Talla
    while True:
        try:
            talla = float(input("Talla (cm): "))
            if talla > 0:
                break
            else:
                print("Talla inválida. Debe ser un valor positivo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido para la talla.")

    # Perímetro craneal
    while True:
        try:
            craneo = float(input("Perímetro craneal (cm): "))
            if craneo > 0:
                break
            else:
                print("Perímetro craneal inválido. Debe ser un valor positivo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número válido para el perímetro craneal.")

    # Departamento
    departamento = None
    while departamento is None:
        mostrar_departamentos()
        opcion = input("Ingrese el número del departamento: ")
        departamento = obtener_departamento(opcion)
        if departamento is None:
            print("Opción inválida. Selecciona un número del listado.")

    # Registrar al niño
    nino = Nino(edad, peso, talla, craneo, departamento)
    registrar_nino(nino)
    print("\n✅ Niño registrado exitosamente.")

