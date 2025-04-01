instrucciones = '''Solicita al usuario un número hexadecimal y lo convierte a decimal, octal y binario'''
print(instrucciones)
print("\n")
print("---------------*-----------------")
print("***********Bienvenido************")
print("---------------*-----------------")
hex_value = input("Ingrese un valor hex: ")
print(hex_value)  # Muestra el valor ingresado

# Variables de control e inicialización
l = count = i = 0  # 'l' indica error en la entrada, 'count' almacenará el resultado, 'i' es el exponente
s = len(hex_value) - 1  # 's' representa la posición del último carácter

# Bucle para recorrer cada carácter del número hexadecimal en orden inverso
while s >= 0:  
    if '0' <= hex_value[s] <= '9':  # Si el carácter es un número entre 0 y 9
        r = int(hex_value[s])  # Se convierte directamente a entero
    elif 'A' <= hex_value[s] <= 'F':  # Si el carácter es una letra válida en hexadecimal (A-F)
        r = ord(hex_value[s]) - 55  # Se convierte a su valor decimal correspondiente
    else:  
        l = 1  # Si encuentra un carácter no válido, marca error
        break  # Termina el bucle

    # Calcula la conversión sumando el valor correspondiente según la base 16
    count = count + (r * 16**i)
    s = s - 1  # Reduce la posición para procesar el siguiente carácter
    i = i + 1  # Incrementa el exponente de la potencia de 16

# Verifica si la conversión fue exitosa o hubo un error
if l == 0:
    print('Valor convertido:', count)  # Muestra el resultado en decimal
else:
    print('Entrada incorrecta')  # Indica que la entrada no fue válida

