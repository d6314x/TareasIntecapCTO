def mostrar_datos_registrados():
    from base_datos import obtener_todos_los_ninios
    ninios = obtener_todos_los_ninios()

    if not ninios:
        print("\nNo hay datos registrados.")
        return

    print("\nLista de niños registrados:")
    print("----------------------------------------------------------------------------------------")
    print(f"{'ID':<5}{'Edad (meses)':<15}{'Peso (kg)':<10}{'Talla (cm)':<15}{'Perímetro Craneal (cm)':<25}{'Departamento':<20}")
    print("----------------------------------------------------------------------------------------")

    for n in ninios:
        print(f"{n.id:<5}{n.edad:<15}{n.peso:<10}{n.talla:<15}{n.craneo:<25}{n.departamento:<20}")

    print("----------------------------------------------------------------------------------------")

