# menu.py
from ingreso_datos import ingresar_datos
from informe_por_departamento import generar_informe_por_departamento
from informe_general import generar_informe_general
from mostrar_datos import mostrar_datos_registrados

def ejecutar_menu():
    while True:
        print("\n===== Sistema de Monitoreo de Crecimiento Infantil =====")
        print("1. Ingresar datos de un niño")
        print("2. Generar informe por departamento")
        print("3. Generar informe general por indicador")
        print("4. Mostrar todos los niños registrados")
        print("0. Salir")
        print("===== INTECAP CTO =====")
        print("Alejandra Hidalgo")
        print("Lisandro Tzunux")
        print("Daniel Camey")
        print("===== =====")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ingresar_datos()
        elif opcion == '2':
            generar_informe_por_departamento()
            #print("en construccion")
        elif opcion == '3':
            generar_informe_general()
            #print("en construccion")
        elif opcion == '4':
            mostrar_datos_registrados()
        elif opcion == '0':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

