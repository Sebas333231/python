class Calculadora:
    def __init__(self):
        self.numero1=int(input("Ingrese un numero: "))
        self.numero2=int(input("Ingrese un numero: "))


    
    def mostrar(self):
        print("Numero1: ", self.numero1)
        print("Numero2: ", self.numero2)

    def suma (self):
       print("Resultado de la Suma: ",self.numero1 + self.numero2)

    def resta(self):
        print("Resultado de la Resta: ",self.numero1 - self.numero2)

    def multiplicacion(self):
        print("Resultado de la Multiplicacion: ",self.numero1 * self.numero2)

    def division(self):
        print("Resultado de la Division: ",self.numero1 / self.numero2)

    

persona1=Calculadora()
persona1.mostrar()
persona1.suma()
persona1.resta()
persona1.multiplicacion()
persona1.division()