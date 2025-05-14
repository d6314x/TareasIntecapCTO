# base_datos.py
ninios = []
conteo_departamentos = {}

def registrar_nino(nino):
    from modelo import Nino
    if isinstance(nino, Nino):
        ninios.append(nino)
        
        # Registrar el niño por departamento
        depto = nino.departamento
        if depto in conteo_departamentos:
            conteo_departamentos[depto].append(nino)
        else:
            conteo_departamentos[depto] = [nino]
    else:
        print("Error: objeto inválido, se esperaba una instancia de Nino")

def obtener_todos_los_ninios():
    return ninios

def obtener_ninios_por_departamento(departamento):
    """
    Devuelve la lista de niños registrados en un departamento.
    """
    return conteo_departamentos.get(departamento, [])

def obtener_conteo_por_departamento():
    """
    Devuelve el número de niños por departamento.
    """
    return {depto: len(lista) for depto, lista in conteo_departamentos.items()}

