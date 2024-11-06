import math
class Triangulo:
    def __init__(self, C1, C2):
        self.C1=C1
        self.C2=C2
    def Area(self):
        self.area=(self.C1 * self.C2)/2
        return self.area
    def Hipotenusa(self):
        self.hipotenusa=math.sqrt(math.pow(self.C1,2)+math.pow(self.C2,2))
        return self.hipotenusa
    def Perimetro(self):
        self.perimetro=self.C1+self.C2+self.hipotenusa
        return self.perimetro
    def Angulos(self):
        self.a1=math.degrees(math.atan(self.C2/self.C1))
        self.a2=math.degrees(math.atan(self.C1/self.C2))
        return self.a1,self.a2
    def PrintAll(self):
        self.Area()
        self.Hipotenusa()
        self.Perimetro()
        self.Angulos()
        
        print(f"Área: {self.area:.2f}")
        print(f"Perímetro: {self.perimetro:.2f}")
        print(f"Hipotenusa: {self.hipotenusa:.2f}")
        print(f"Ángulo 1: {self.a1:.2f}°")
        print(f"Ángulo 2: {self.a2:.2f}°")

print("Inserte la longitud de los dos catetos de su triangulo rectangulo")
try:
    C1=float(input("Cateto 1: "))
    C2=float(input("Cateto 2: "))

    triangulo = Triangulo(C1,C2)
    triangulo.PrintAll()
except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")


