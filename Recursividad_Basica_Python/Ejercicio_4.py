instrucciones = '''
Ejercicio 4
Crear una función recursiva que imprima los números del 1 hasta n
# Resultado esperado:  cuenta_ascendente(4):
 1
 2
 3
 4
'''


def cuenta_ascendente(n):
    if n == 0:
        return
    cuenta_ascendente(n - 1)
    print(n)

# Ejemplo de uso
cuenta_ascendente(20)
