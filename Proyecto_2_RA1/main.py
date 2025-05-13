def ingresar_datos():
    while True:
        try:
            edad = int(input("Ingrese la edad del paciente (en meses, de 0 a 24): "))
            if 0 <= edad <= 24:
                break
            else:
                print("ERROR: La edad debe estar entre 0 y 24 meses.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    paciente = {
        "Genero": input("Ingrese el género del paciente (Masculino/Femenino): "),
        "Edad": edad,
        "Peso": float(input("Ingrese el peso del paciente (en kg): ")),
        "Talla": float(input("Ingrese la talla del paciente (en cm): ")),
        "Perimetro_craneal": float(input("Ingrese el perímetro craneal (en cm): ")),
        "Departamento": input("Ingrese el departamento de origen: "),
    }
    return paciente

def generar_reporte(pacientes):
    print("\n--- REPORTE DE TODOS LOS PACIENTES ---")
    if not pacientes:
        print("No hay pacientes registrados aún.")
        return

    # Encabezado de la tabla
    encabezado = ["# ", "Genero", "Edad (meses)", "Peso (kg)", "Talla (cm)", "Perimetro craneal (cm)", "Departamento"]

    # Formato de la tabla
    print(f"{encabezado[0]:<5}{encabezado[1]:<10}{encabezado[2]:<15}{encabezado[3]:<15}{encabezado[4]:<15}{encabezado[5]:<25}{encabezado[6]:<20}")
    print("-" * 100)  # Línea divisoria

    # Mostrar cada paciente en formato tabla
    for idx, paciente in enumerate(pacientes, 1):
        print(f"{idx:<5}{paciente['Genero']:<10}{paciente['Edad']:<15}{paciente['Peso']:<15}{paciente['Talla']:<15}{paciente['Perimetro_craneal']:<25}{paciente['Departamento']:<20}")

def main():
    pacientes = []

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ingresar datos de un paciente")
        print("2. Mostrar reporte de todos los pacientes")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nuevo_paciente = ingresar_datos()
            pacientes.append(nuevo_paciente)
            print("✅ Paciente registrado con éxito.")
        elif opcion == "2":
            generar_reporte(pacientes)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

main()

