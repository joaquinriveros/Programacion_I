"""3-Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, 
imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno)."""

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def largest_side(self):
        return max(self.side1, self.side2, self.side3)

    def triangle_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Equilátero"
        elif self.side1 == self.side2 or self.side2 == self.side3 or self.side1 == self.side3:
            return "Isósceles"
        else:
            return "Escaleno"
