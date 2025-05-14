from base_datos import obtener_todos_los_ninios
from procesamiento import procesar_clasificaciones, calcular_estadisticas

def generar_informe_general():
    ninios = obtener_todos_los_ninios()
    conteo, total_validos = procesar_clasificaciones(ninios)
    resultados = calcular_estadisticas(conteo, total_validos)

    print("\nResumen General Nacional")
    print("Indicador      Bajo (%)   Dentro (%)  Sobre (%)  Promedio")
    print("---------------------------------------------------------")
    for indicador, data in resultados.items():
        print(f"{indicador.capitalize():<15} {data['Bajo (%)']:<10} {data['Dentro (%)']:<12} {data['Sobre (%)']:<10} {data['Promedio']}")

