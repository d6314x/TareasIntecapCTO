'''este codigo crea dos clases que permite guardar informacion de los proveedores 
  permie almacenar nombre,direccion, trelefono, correo,contacoz, sobre estos datos nos deja crear actualisar, mostrar y eliminar'''

#clase provee esta clase prmite guadar los datos y permite ver la informacion y cuenta con un metodo def mostrar_informacion

class Proveedor:
    _contador_id = 1  # Contador de ID único

    def __init__(self, nombre, direccion, telefono, correo, contacto): #constructor
        self.id = Proveedor._contador_id 
        Proveedor._contador_id += 1
          #parametros
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.contacto = contacto

         #funcion para mostrar la informacion
    def mostrar_informacion(self):
        print(f"\nID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")
        print(f"Persona de Contacto: {self.contacto}")

           #almacena los datos
class GestorProveedores:
    def __init__(self):
        self.lista_proveedores = []

    def agregar_proveedor(self, nombre, direccion, telefono, correo, contacto):
        nuevo = Proveedor(nombre, direccion, telefono, correo, contacto)
        self.lista_proveedores.append(nuevo)
        print(f"\nProveedor '{nombre}' agregado con ID {nuevo.id}.")
            #mustra el mensaage si no hay datos
    def mostrar_proveedores(self):
        if not self.lista_proveedores:
            print("\nNo hay proveedores registrados.")
            return
        print("\nLista de proveedores:")
        for prov in self.lista_proveedores:
            prov.mostrar_informacion()
            #esto deja que el provedor edita las cosas y a la persona agregada
    def editar_proveedor(self, id_proveedor, nuevo_nombre=None, nueva_direccion=None,
                         nuevo_telefono=None, nuevo_correo=None, nuevo_contacto=None):
        for prov in self.lista_proveedores:
            if prov.id == id_proveedor:
                if nuevo_nombre: prov.nombre = nuevo_nombre
                if nueva_direccion: prov.direccion = nueva_direccion
                if nuevo_telefono: prov.telefono = nuevo_telefono
                if nuevo_correo: prov.correo = nuevo_correo
                if nuevo_contacto: prov.contacto = nuevo_contacto
                print(f"\nProveedor ID {id_proveedor} ha sido actualizado.")
                return
        print(f"\nProveedor con ID {id_proveedor} no encontrado.")
              #sirve para elinibar un proveedor
    def eliminar_proveedor(self, id_proveedor):
        for prov in self.lista_proveedores:
            if prov.id == id_proveedor:
                self.lista_proveedores.remove(prov)
                print(f"\nProveedor ID {id_proveedor} eliminado.")
                return
        print(f"\nProveedor con ID {id_proveedor} no encontrado.")

    def obtener_diccionario(self):
        return {
            "proveedores": [vars(p) for p in self.lista_proveedores]
        }


# -------------------------------
# USO / DEMO
# -------------------------------

# Instancia del gestor
gestor = GestorProveedores()

# Agregar proveedores
gestor.agregar_proveedor("Tienda el Olam", "Calle 123", "123-456-7890", "proveedorA@example.com", "Juan Perez")
gestor.agregar_proveedor("Distribuidora Maya", "Av. Reforma", "555-123-4567", "maya@correo.com", "Ana Gómez")

# Mostrar todos los proveedores
gestor.mostrar_proveedores()

# Editar un proveedor
gestor.editar_proveedor(1, nuevo_telefono="321-000-9999", nuevo_contacto="Carlos López")

# Eliminar un proveedor
gestor.eliminar_proveedor(2)

# Mostrar todos los proveedores después de cambios
gestor.mostrar_proveedores()

# Obtener el diccionario
diccionario_final = gestor.obtener_diccionario()
print("\nDiccionario de proveedores:", diccionario_final)
