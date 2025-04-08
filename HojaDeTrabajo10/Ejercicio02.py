instrucciones ='''
----------------------------****--------------------------
Crea 2 vectores (Arrays unidimensionales) que tengan
el mismo tamaño ingresado por el usuario, en uno de
ellos almacenarás nombres de persona, en el otro vector
va almacenando la longitud de los nombres.
Por ejemplo:

Tamaño: 6

Array1=[‘Pedro’,’Pablo’,’Juan’,’Jorge’,’Marcos’,’María’ ]
Longitud=[5,5,4,5,6,5]
----------------------------****--------------------------
'''

print(instrucciones)

arregloA = []
arregloB = []
cont = 1
size = int(input('Ingrese tamaño del arreglo: '))

for i in range(1, size+1):
    nombre = input(f'Ingrese nombre {cont} : ')
    arregloA.append(nombre)
    arregloB.append(len(nombre))
    cont += 1
print(f'Tamaño: {size}')
print(f'Array1 = {arregloA}')
print(f'Longitud = {arregloB}')

