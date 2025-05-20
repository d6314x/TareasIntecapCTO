# modelo.py
"""
El código muestra la creacion de la clase tipo NINO, que nos permite crear objetos 
para almacenar los datos
"""
class Nino:
    _contador_id = 1  # variable de clase (compartida entre todas las instancias)

    def __init__(self, edad, peso, talla, craneo, departamento):
        self.id = Nino._contador_id  # asigna el ID actual
        Nino._contador_id += 1       # incrementa para el siguiente niño

        self.edad = edad #Indica el registro de la edad
        self.peso = peso #Registro del peso
        self.talla = talla #Registra la talla
        self.craneo = craneo #Registra el perímetro craneal
        self.departamento = departamento #Registra la cantidad por departamento 

