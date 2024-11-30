print(" ")
print("Alvaro Campechano 3W")
print(" ")
class Persona:
    def __init__(self, nombre, edad):
        # Inicializa los atributos de la persona con su nombre y edad
        # :param nombre: Nombre de la persona (str)
        # :param edad: Edad de la persona (int)
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        # Imprime el nombre y la edad de la persona
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
    
    def es_mayor_de_edad(self):
        # Verifica si la persona es mayor de edad (edad >= 18)
        if self.edad >= 18:
            print("Es mayor de edad.")
        else:
            print("Es menor de edad.")

# Crear un objeto de la clase Persona
persona1 = Persona("Alvaro Campechano", 16)
persona1.mostrar_datos()
persona1.es_mayor_de_edad()
