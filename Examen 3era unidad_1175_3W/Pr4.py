print(" ")
print("Alvaro Campechano 3W")
print(" ")
class Calculadora:
    def __init__(self, num1, num2):
        # Inicializa los dos números para las operaciones
        # :param num1: Primer número (int o float)
        # :param num2: Segundo número (int o float)
        self.num1 = num1
        self.num2 = num2
    
    def sumar(self):
        # Realiza la suma de los dos números
        return self.num1 + self.num2
    
    def restar(self):
        # Realiza la resta entre los dos números
        return self.num1 - self.num2
    
    def multiplicar(self):
        # Realiza la multiplicación de los dos números
        return self.num1 * self.num2
    
    def dividir(self):
        # Realiza la división entre los dos números
        # Si el divisor es 0, retorna un mensaje de error
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "No se puede dividir entre cero"

# Crear un objeto de la clase Calculadora
calc = Calculadora(10, 5)
print(f"Suma: {calc.sumar()}")
print(f"Resta: {calc.restar()}")
print(f"Multiplicación: {calc.multiplicar()}")
print(f"División: {calc.dividir()}")
