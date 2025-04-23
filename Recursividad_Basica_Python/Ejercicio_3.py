instrucciones = '''
Ejercicio 3:
Cuenta regresiva: Crea una función recursiva cuenta_regresiva(n) que imprima desde n hasta 0.
Ejemplo:
cuenta_regresiva(3)
→ 3
→ 2
→ 1
→ 0
→ ¡Despegue!
'''

'''
def cuenta_regresiva(n):
    if n<0:
        print("¡Despegue!")
    else:
        print(n)
        cuenta_regresiva(n-1)

#Ejemplo de uso:
cuenta_regresiva(5)
'''

def cuenta_regresiva(n):
    if n >= 0:
        print(f"→ {n}")
        cuenta_regresiva(n - 1)
    else:
        print("→ ¡Despegue!")
# Ejemplo de uso
cuenta_regresiva(5)
