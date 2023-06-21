class Persona:
    def __init__(self, nom, ema):
        self.nombre = nom
        self.email = ema

    def mostrar(self):
        print("Nombre: " + self.nombre)
        print("Email: " + self.email)


class Alumno(Persona):
    nota = 0

    def mostrar_alumno(self):
        print("Nombre: " + self.nombre)
        print("Email: " + self.email)
        print("Nota: " + str(self.nota))


class Profesor(Persona):
    espe = ""

    def mostrar_profesor(self):
        print("Nombre: " + self.nombre)
        print("Email: " + self.email)
        print("Especialidad: " + self.espe)


alumno1 = Alumno("Carlos Tello", "ctello@gmail.com")
alumno1.nota = 15
alumno1.mostrar_alumno()

profesor1 = Profesor("Jorge Garnica", "jgarnica@gmail.com")
profesor1.espe = "HTML"
profesor1.mostrar_profesor()
