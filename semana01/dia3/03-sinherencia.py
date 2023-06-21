class Alumno:
    def __init__(self, nom, ema, nota) -> None:
        self.nombre = nom
        self.email = ema
        self.nota = nota

    def mostrar(self):
        print("Nombre: " + self.nombre)
        print("Email: " + self.email)
        print("Nota: " + str(self.nota))


class Profesor:
    def __init__(self, nom, ema, esp):
        self.nombre = nom
        self.email = ema
        self.especialidad = esp

    def mostrar(self):
        print("Nombre: " + self.nombre)
        print("Email: " + self.email)
        print("Especialidad: " + self.especialidad)


alumno1 = Alumno("Carla Perez", "cperez@gmail.com", 20)
alumno1.mostrar()

profesor1 = Profesor("Cesar Mayta", "cmayta@gmail.com", "Python")
profesor1.mostrar()
