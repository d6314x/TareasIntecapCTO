instrucciones = '''
Ejercicio 5
Crear una función suma_hasta(n) que devuelva la suma de 1 + 2 + ... + n

Ejemplo:
suma_hasta(4) → 10

'''

def suma_hasta(n):
    if n < 1:
        return 0  # Caso base para n = 0 o negativo
    else:
        return n + suma_hasta(n-1)

print(suma_hasta(4))
