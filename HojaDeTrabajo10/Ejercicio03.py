instrucciones = '''
------------------------------****-------------------------------
En el restaurante de la universidad, el cliente luego 
de ser atendido evalúa la atención recibida presionando 
un botón entre las 5 opciones mostradas.

Opciones:
 5. Excelente
 4. Muy Buena
 3. Buena
 2. Regular
 1. Malo

Realice un algoritmo que registre en un arreglo la 
evaluación para N clientes atendidos, luego deberá tabular 
las respuestas para mostrar:

a) Total de respuestas por tipo
b) La respuesta más frecuente
c) ¿Cuáles clientes respondieron con valores menores al promedio?

Salida
Respuestas
a)  Excelente: 10
    Muy Buena: 20
    Buena: 15
    Regular: 3
    Malo: 2
b) Más frecuente: 4
c) Promedio: 3.66
Porcentaje menor al promedio.:
15%

------------------------------****-------------------------------
'''
opciones = '''
 5. Excelente
 4. Muy Buena
 3. Buena
 2. Regular
 1. Malo
'''
print(instrucciones)

# Inicializar variables
arreglo = []
cliente_cont = 1
size = int(input('Ingrese la cantidad de clientes para evaluación: '))

# Registrar evaluaciones
for i in range(1, size + 1):
    print(opciones)
    opcion = int(input(f'Ingrese una opcion, cliente {cliente_cont}: '))
    arreglo.append(opcion)
    cliente_cont += 1

print("Respuestas registradas:", arreglo)

# Tabular respuestas por tipo
def contar_respuestas(arreglo, tipo):
    #Este código cuenta cuántas veces un valor específico (tipo) aparece en el arreglo.
    return sum(1 for respuesta in arreglo if respuesta == tipo)

print("\nTotal de respuestas por tipo:")
print(f"Excelente: {contar_respuestas(arreglo, 5)}")
print(f"Muy Buena: {contar_respuestas(arreglo, 4)}")
print(f"Buena: {contar_respuestas(arreglo, 3)}")
print(f"Regular: {contar_respuestas(arreglo, 2)}")
print(f"Malo: {contar_respuestas(arreglo, 1)}")

# Determinar la respuesta más frecuente
frecuencias = [contar_respuestas(arreglo, tipo) for tipo in range(1, 6)]
respuesta_mas_frecuente = frecuencias.index(max(frecuencias)) + 1
print(f"\nMás frecuente: {respuesta_mas_frecuente}")

# Calcula el promedio y evalúa valores menores al promedio
promedio = sum(arreglo) / len(arreglo)
menores_promedio = [resp for resp in arreglo if resp < promedio]
porcentaje_menor = (len(menores_promedio) / len(arreglo)) * 100

print(f"\nPromedio: {promedio:.2f}")
print(f"Porcentaje menor al promedio: {porcentaje_menor:.2f}%")

