# Número de días a registrar
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# Datos simulados de 1 semana de paciente
niveles_azucar = [130, 160, 95, 175, 160, 135, 168] # mg/dL
niveles_sal = [2000, 2400, 1800, 2400, 2700, 2200, 2300] # mg
presion_sistolica = [115, 130, 110, 125, 175, 135, 140] # mmHg
presion_diastolica = [78, 79, 85, 89, 92, 80, 90] # mmHg

#Creamos un for para recorrer cada lista sincornizada por el dia, tomamos de referencia el tamanio de la lista de dias 07
for i in range(len(dias)):
    #print(f'{dias[i]} {niveles_azucar[i]} {niveles_sal[i]} {presion_sistolica[i]} {presion_diastolica[i]}')
    print(dias[i])
    if niveles_azucar[i] >= 70 and niveles_azucar[i] <= 140 :
        print(f'{niveles_azucar[i]} Nivel de Azucar saludable')
    else:
        print(f'{niveles_azucar[i]} Nivel de Azucar no saludable')

    if niveles_sal[i] >= 2300:
        print(f'{niveles_sal[i]} Nivel de Sal no saludable')
    else:
        print(f'{niveles_sal[i]} Nivel de Sal saludable')    
    # Normal: Sistólica < 120 mmHg y Diastólica < 80 mmHg.
    if presion_sistolica[i] < 120 and presion_diastolica[i] < 80:
        print(f'Normal')

    # Elevada: Sistólica entre 120-129 mmHg y Diastólica < 80 mmHg.
    if (presion_sistolica[i] >= 120 and presion_sistolica[i] <= 129) and presion_diastolica[i] < 80:
        print(f'Elevada')

    # Hipertensión Etapa 1: Sistólica entre 130-139 mmHg o Diastólica entre 80-89 mmHg.
    if (presion_sistolica[i] >= 130 and presion_sistolica[i] <= 139) or (presion_diastolica[i] >= 80 and presion_diastolica[i] <= 89):
        print("Hipertensión Etapa 1")

    # Hipertensión Etapa 2: Sistólica ≥ 140 mmHg o Diastólica ≥ 90 mmHg.
    if presion_sistolica[i] >= 140 or presion_diastolica[i] >= 90:
        print("Hipertensión Etapa 2")

    print("-----------------------")

print("Promedio Semanal")
prmdoAzucar = (sum(niveles_azucar)/len(niveles_azucar))
print(f'Promedio de azucar semanal: {prmdoAzucar}')

prmdoSal = (sum(niveles_sal)/len(niveles_sal))
print(f'Promedio de sal semanal: {prmdoSal}')

prmdoPresionSistolica = (sum(presion_sistolica)/len(presion_sistolica))
print(f'Promedio de presion sistolica: {prmdoPresionSistolica}')

prmdoPresionDiastolica = (sum(presion_diastolica)/len(presion_diastolica))
print(f'Promedio de presion distolica: {prmdoPresionDiastolica}')
