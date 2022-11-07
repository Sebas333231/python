class Alumno:
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.nota=int(input("Ingrese la Nota: "))


    
    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.nota)

    def nota_alumno(self):
        if self.nota >= 3 :
            print("El estudiante aprobo.")
        else:
            print("El estudiante no aprobo, debe recuperar.")
persona1=Alumno()
persona1.mostrar()
persona1.nota_alumno()