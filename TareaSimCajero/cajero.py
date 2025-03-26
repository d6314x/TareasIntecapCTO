# Instrucciones para el programa
instrucciones = '''
Programa que simula: Cajero Automático
Crea un programa que simule un cajero automático. El usuario tiene un saldo inicial de Q3000 y puede realizar retiros ingresando una cantidad. Si el saldo es insuficiente, debe mostrar un mensaje y permitir otro intento.
El programa termina si:
El usuario retira exactamente su saldo disponible.
Ingresa "0" para salir.
Intenta retirar más de tres veces un monto superior al saldo disponible.
'''

# Inicialización de variables: saldo inicial del usuario y límite de intentos
saldo = 3000
intentos = 3

# Mostrar las instrucciones al usuario
print(instrucciones)
print("\n")
print("---------------*-----------------")
print("***********Bienvenido************")
print("---------------*-----------------")
print(f'Saldo inicial: Q{saldo}')  # Informar al usuario sobre su saldo actual

# Ciclo principal del programa: se ejecuta mientras haya saldo y queden intentos
while saldo > 0 and intentos > 0:
    # Solicitar al usuario el monto a retirar
    retiro = float(input("Ingrese monto a retirar: "))
    # Si el usuario ingresa 0, termina el programa
    if retiro == 0:
        print("Has decidido salir. Adiós.")
        break
    # Validar que el monto no sea negativo
    elif retiro < 0:
        print("El monto ingresado no puede ser negativo.")
    # Si el monto es mayor al saldo, restar un intento
    elif retiro > saldo:
        intentos -= 1
        print(f'Saldo insuficiente. Intentos restantes: {intentos}')
    # Si el monto es válido, realizar el retiro
    else:
        saldo -= retiro
        print(f'Retiro exitoso. Nuevo saldo: Q{saldo}')
        # Si el saldo llega a cero, terminar el programa
        if saldo == 0:
            print("Saldo agotado. Adiós.")
            break

# Si se agotan los intentos, informar al usuario y terminar el programa
if intentos == 0:
    print("Has excedido el número de intentos. Adiós.")

