# modelo.py
class Nino:
    _contador_id = 1  # variable de clase (compartida entre todas las instancias)

    def __init__(self, edad, peso, talla, craneo, departamento):
        self.id = Nino._contador_id  # asigna el ID actual
        Nino._contador_id += 1       # incrementa para el siguiente niño

        self.edad = edad
        self.peso = peso
        self.talla = talla
        self.craneo = craneo
        self.departamento = departamento

