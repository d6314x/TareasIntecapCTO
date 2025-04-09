
#Integrantes 
#Edvin Yax
#Francisco Tax
#Daniel Camey

vuelos = {
        "vuelo1": {"CUI": 1, "Origen": "Mexico", "Destino": "Guatemala", "CantidadAsientos": 25, "AsientosDisponibles": 25},
        "vuelo2": {"CUI": 2, "Origen": "El Salvador", "Destino": "Guatemala", "CantidadAsientos": 25, "AsientosDisponibles": 25}
        }

# menu
opcion = '0'
opcionM1 = 0
while not(opcion=='9'):
    print(' 1. Creación de vuelos:')
    print(' 2. Reservar un vuelo: ')
    print(' 3. Selección de asiento: ')
    print(' 4. Ver reservas: ')
    print(' 9. Salir')

    opcion=input('Sistema de Reserva de Vuelos: ')
    
    if (opcion=='1'):
        nuevos_datos = []

        print(' **** menu Creación de vuelos ***')
        
        opcion_M1_Nombre=input('Ingrese Nombre de vuelo: ')
        nuevos_datos.append(opcion_M1_Nombre) 

        opcion_M1_CUI=input('Ingrese CUI de vuelo: ')
        nuevos_datos.append(opcion_M1_CUI)
        opcion_M1_Origen=input('Ingrese Origen de vuelo: ')
        nuevos_datos.append(opcion_M1_Origen)
        opcion_M1_Destino=input('Ingrese Destino de vuelo: ')
        nuevos_datos.append(opcion_M1_Destino)
        opcion_M1_Asientos=input('Ingrese Cantidad de Asientos de vuelo: ')
        nuevos_datos.append(opcion_M1_Asientos)
        print(nuevos_datos)
        vuelos.update(nuevos_datos)
        print(vuelos)
        break
    elif (opcion=='2'):
        print(' **** menu Reservar un vuelo ****')
        
    elif (opcion=='3'):
        print(' **** menu Selección de asiento ****')
        
    elif (opcion=='4'):
        print(' **** menu Ver reservas ****')
        
    elif (opcion=='9'):
        print(' **** Saliendo del menu  ****')
        print(' **** fin de programa ****')
    else:
        print('No existe la opcion en el menu')
