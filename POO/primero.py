class Persona:
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))


    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)



class Empleado(Persona):

    def __init__(self):

        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))

    def mostrar(self):
        super().mostrar()
        print(f"Sueldo: {self.sueldo:.0f}")

    def pagar_impuestos(self):
        if self.sueldo > 3600000:
            descuento=self.sueldo*0.035
            print(f"El descuento es igual a: {descuento:.0f}")
            total=self.sueldo-descuento
            print(f"Total a ganar: {total:.0f}")
            
        else:
            print("El empleado no tiene descuento en su sueldo.")

    
persona1=Persona()
persona1.mostrar()
empleado1=Empleado()
empleado1.mostrar()
empleado1.pagar_impuestos()