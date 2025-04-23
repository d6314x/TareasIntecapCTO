instrucciones = '''Ejercicio 7
Mínimo en lista (sin min())
Crear una función recursiva minimo(lista) que devuelva el valor más pequeño de una lista de números.

Ejemplo:
minimo([5, 3, 8, 1, 2]) → 1
'''

def minimo(lista):
    if len(lista) == 1:
        return lista[0]

    actual = lista[0]
    resto = lista[1:]
    min_resto = minimo(resto)
    if actual < min_resto:
        return actual
    else:
        return min_resto

# Ejemplo de uso
lista_numeros = [5, 2, 9, 1, 5, 6]
minimo_en_lista = minimo(lista_numeros)
print(f"El mínimo de la lista {lista_numeros} es: {minimo_en_lista}")
