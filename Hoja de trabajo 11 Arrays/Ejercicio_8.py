numeros=[11,22,33,44]
encontrado=False
buscar=332

for n in numeros:
    if n == buscar:
        encontrado = True
        break

if encontrado:
    print("Si esta en la lista")
else:
    print("No se encontro")
