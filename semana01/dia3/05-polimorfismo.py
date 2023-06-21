class Persona:
    def __init__(self, nom, ema):
        self.nombre = nom
        self.email = ema

    def mostrar(self):
        print("Nombre: " + self.nombre)
        print("Email: " + self.email)


class Alumno(Persona):
    def __init__(self, nom, ema, nota):
        super().__init__(nom, ema)
        self.nota = nota

    def mostrar(self):
        print("*" * 10 + "Datos del Alumno" + "*" * 10)
        super().mostrar()
        print("Nota: " + str(self.nota))


class Profesor(Persona):
    def __init__(self, nom, ema, especialidad):
        super().__init__(nom, ema)
        self.esp = especialidad

    def mostrar(self):
        print("*" * 10 + "Datos del Docente" + "*" * 10)
        super().mostrar()
        print("Especialidad: " + self.esp)


alumno1 = Alumno("carla perez", "cperez@gmail.com", 20)
alumno1.mostrar()

profesor1 = Profesor("Cesar Mayta", "cmayta@hotmail.com", "BackEnd")
profesor1.mostrar()
