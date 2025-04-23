instrucciones = '''
Ejercicio 2:
Crea una función suma_lista(lista) que reciba una lista de números y devuelva la suma total.
Ejemplo:
suma_lista([1, 2, 3]) → 6
'''


def suma_lista(lista):
    suma=0
    #suma = sum(lista)
    for num in lista:
        suma += num
    print(suma)

suma_lista([5,10,15,20])
