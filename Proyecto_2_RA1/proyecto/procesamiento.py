# procesamiento.py
from clasificar_ninio import clasificar_ninio

def procesar_clasificaciones(ninios):
    """
    Recibe una lista de niños, y retorna un diccionario con:
    - conteo por categoría (Bajo, Dentro, Sobre) para cada indicador
    - sumas acumuladas de cada indicador (para calcular promedios)
    """
    conteo = {
        "peso": {"Bajo": 0, "Dentro": 0, "Sobre": 0, "total": 0.0},
        "talla": {"Bajo": 0, "Dentro": 0, "Sobre": 0, "total": 0.0},
        "craneo": {"Bajo": 0, "Dentro": 0, "Sobre": 0, "total": 0.0}
    }
    total_validos = 0

    for nino in ninios:
        clasificacion = clasificar_ninio(nino)
        if not clasificacion:
            continue  # Saltar niños no válidos
        total_validos += 1
        for indicador in ["peso", "talla", "craneo"]:
            categoria = clasificacion[indicador]
            conteo[indicador][categoria] += 1
            conteo[indicador]["total"] += getattr(nino, indicador)
    
    return conteo, total_validos

def calcular_estadisticas(conteo, total_validos):
    """
    A partir del conteo, devuelve porcentajes y promedios para cada indicador.
    """
    resultados = {}
    for indicador in ["peso", "talla", "craneo"]:
        total = sum(conteo[indicador][cat] for cat in ["Bajo", "Dentro", "Sobre"])
        if total == 0:
            bajo = dentro = sobre = 0
        else:
            bajo = (conteo[indicador]["Bajo"] / total) * 100
            dentro = (conteo[indicador]["Dentro"] / total) * 100
            sobre = (conteo[indicador]["Sobre"] / total) * 100
        promedio = conteo[indicador]["total"] / total_validos if total_validos > 0 else 0
        resultados[indicador] = {
            "Bajo (%)": f"{bajo:.0f}%",
            "Dentro (%)": f"{dentro:.0f}%",
            "Sobre (%)": f"{sobre:.0f}%",
            "Promedio": f"{promedio:.1f}"
        }
    return resultados

