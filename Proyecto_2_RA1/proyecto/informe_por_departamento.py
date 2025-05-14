from base_datos import obtener_conteo_por_departamento, obtener_ninios_por_departamento
from procesamiento import procesar_clasificaciones, calcular_estadisticas

def generar_informe_por_departamento():
    print("\nInforme por Departamento")
    print("Departamento     Indicador     Bajo (%)   Dentro (%)  Sobre (%)")
    print("--------------------------------------------------------------")
    conteo_departamentos = obtener_conteo_por_departamento()
    for depto in conteo_departamentos:
        ninios = obtener_ninios_por_departamento(depto)
        total = len(ninios)
        conteo, total_validos = procesar_clasificaciones(ninios)
        resultados = calcular_estadisticas(conteo, total_validos)
        for indicador, data in resultados.items():
            print(f"{depto:<17} {indicador.capitalize():<13} {data['Bajo (%)']:<10} {data['Dentro (%)']:<12} {data['Sobre (%)']}")

