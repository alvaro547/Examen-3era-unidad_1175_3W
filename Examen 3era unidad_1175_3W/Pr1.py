print(" ")
print("Alvaro Campechano 3W")
print(" ")
class Alumno:
    def __init__(self, nombre, nota):
        # Inicia los atributos del alumno con su nombre y nota
        # :param nombre: Nombre del alumno (str)
        # :param nota: Nota del alumno (float)
        self.nombre = nombre
        self.nota = nota
    
    def imprimir_datos(self):
        # Imprime el nombre y la nota del alumno
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
    
    def resultado(self):
        # Muestra si el alumno ha aprobado o reprobado basado en su nota
        # Si la nota es mayor o igual a 6, se considera aprobado
        if self.nota >= 6:
            print("¡Aprobado!")
        else:
            print("Reprobado")

# Crear un objeto de la clase Alumno
alumno1 = Alumno("Alvaro Estrada", 9)
alumno1.imprimir_datos()
alumno1.resultado()
