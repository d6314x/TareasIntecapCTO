instrucciones = '''
Ejercicio 6
Crear una función factorial(n) recursiva

Ejemplo:
factorial(5) → 120

'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Ejemplo
print(factorial(5))
