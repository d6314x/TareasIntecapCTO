departamentos = [
    "Alta Verapaz", "Baja Verapaz", "Chimaltenango", "Chiquimula",
    "El Progreso", "Escuintla", "Guatemala", "Huehuetenango",
    "Izabal", "Jalapa", "Jutiapa", "Petén", "Quetzaltenango",
    "Quiché", "Retalhuleu", "Sacatepéquez", "San Marcos",
    "Santa Rosa", "Sololá", "Suchitepéquez", "Totonicapán", "Zacapa"
]

def mostrar_departamentos():
    print("\nSeleccione un departamento:")
    for i, depto in enumerate(departamentos, start=1):
        print(f"{i}. {depto}")

def obtener_departamento(opcion):
    try:
        indice = int(opcion) - 1
        if 0 <= indice < len(departamentos):
            return departamentos[indice]
    except ValueError:
        pass
    return None

