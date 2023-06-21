class Usuario:
    email = "jesuschiroque@gmail.com"
    password = "codigo2023"

    def login(self, email, password):
        if self.email == email and self.password == password:
            print("Bienvenido " + self.email)
        else:
            print("datos incorrectos")


usuario1 = Usuario()
# usuario1.login("jesuschiroque@gmail.com", "codigo2023")
user = input("Ingrese su usuario: ")
pwd = input("Ingrese su password: ")
usuario1.login(user, pwd)
