instrucciones = '''
Dado un numero de 02 cifras convertir su equivalente a texto

22 veintidós
99 noventa y nueve
30 treinta

'''
numeros_en_texto = [
    "cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve",
    "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve",
    "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve", "treinta"
]

decenas_en_texto = ["cero", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa", "cien"]


print(instrucciones)
numero = int(input("Ingrese un numero: "))

if numero == 0:
    print(f'Numero ingresado: {numero} {numeros_en_texto[numero]}')

elif numero >= 1 and numero <= 30:
    print(f'Numero ingresado: {numero} {numeros_en_texto[numero]}')

elif numero >= 31 and numero <= 99:
    decena = numero // 10
    unidad = numero % 10
    #print(unidad)
    #print(decena)
    print(f'Numero ingresado: {numero} {decenas_en_texto[decena]} y {numeros_en_texto[unidad]}')

elif numero >= 100:
    print(f'Numero no valido, ingreso {numero}')
