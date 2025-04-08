instrucciones = '''
-----------------------------****-----------------------------
Solicita al usuario el tamaño del arreglo (array)
unidimensional e inicialízalo con dicho tamaño.

Pide al usuario un número base para generar los múltiplos.
Crea una función que rellene el arreglo con los primeros
múltiplos del número ingresado por el usuario.

Por ejemplo:

Si el tamaño del arreglo es 6 y el número base es 8,
el contenido del arreglo debe ser:

[8, 16, 24, 32, 40, 48].
---------------------------****-------------------------------
'''

print(instrucciones)

arreglo = []
size = int(input('Ingrese tamaño del arreglo: '))
base = int(input('Ingrese base para generar multiplos: '))
print('\n')

for i in range(1, size+1):
    resultado = base*i
    arreglo.append(resultado)
print(arreglo)

