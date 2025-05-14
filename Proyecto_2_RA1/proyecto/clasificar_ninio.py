# clasificar_ninio.py
from clasificacion_oms import rangos_oms

def clasificar_valor(valor, minimo, maximo):
    if valor < minimo:
        return "Bajo"
    elif valor > maximo:
        return "Sobre"
    else:
        return "Dentro"

def clasificar_ninio(nino):
    edad = nino.edad
    if edad not in rangos_oms:
        return None  # No hay datos para esa edad

    peso_min, peso_max, talla_min, talla_max, craneo_min, craneo_max = rangos_oms[edad]

    return {
        "peso": clasificar_valor(nino.peso, peso_min, peso_max),
        "talla": clasificar_valor(nino.talla, talla_min, talla_max),
        "craneo": clasificar_valor(nino.craneo, craneo_min, craneo_max),
    }

