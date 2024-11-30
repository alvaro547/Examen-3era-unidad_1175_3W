print(" ")
print("Alvaro Campechano 3W")
print(" ")
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        # Inicializa los tres lados del triángulo
        # :param lado1: Longitud del primer lado (int o float)
        # :param lado2: Longitud del segundo lado (int o float)
        # :param lado3: Longitud del tercer lado (int o float)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def imprimir_lado_mayor(self):
        # Imprime el valor del lado más largo
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor es: {mayor}")
    
    def tipo_triangulo(self):
        # Determina el tipo de triángulo: equilátero, isósceles o escaleno
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")

# Crear un objeto de la clase Triangulo
triangulo1 = Triangulo(3, 4, 5)
triangulo1.imprimir_lado_mayor()
triangulo1.tipo_triangulo()
