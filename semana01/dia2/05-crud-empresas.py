import os
import time

"""
CRUD
C = CREATE
R = READ
U = UPDATE
D = DELETE
"""
empresa = {"ruc": "12345678985", "razon_social": "1 once sac", "ciudad": "Lima"}
lista_empresas = []
opcion = 0
ancho = 50


##################FUNCIONES####################
def buscar_empresa(ruc):
    posicion_busqueda = -1
    for posicion in range(len(lista_empresas)):
        dic_empresa = lista_empresas[posicion]
        for clave, valor in dic_empresa.items():
            if clave == "ruc" and valor == valor_busqueda:
                posicion_busqueda = posicion
                break
    return posicion_busqueda


def grabar_datos():
    str_datos = ""
    for dic_empresa in lista_empresas:
        str_datos += dic_empresa.get("ruc") + ", "
        str_datos += dic_empresa.get("razon_social") + ", "
        str_datos += dic_empresa.get("ciudad") + "\n"
    return str_datos


def cargar_datos(str_datos):
    lista_datos = []
    listado_general = str_datos.splitlines()
    for str_registro in listado_general:
        lista_registro = str_registro.split(",")
        dic_registro = {
            "ruc": lista_registro[0],
            "razon_social": lista_registro[1],
            "ciudad": lista_registro[2],
        }
        lista_datos.append(dic_registro)
    return lista_datos


##########################################################

f = open("empresas.csv", "r")
str_datos = f.read()
f.close()

lista_empresas = cargar_datos(str_datos)

while opcion != 5:
    print("=" * ancho)
    print(" " * int(ancho / 5) + "REGISTRO DE EMPRESAS PERUANAS")
    print("=" * ancho)
    print(
        """
          [1] REGISTRAR EMPRESAS
          [2] LISTADO DE EMPRESAS
          [3] ACTUALIZAR EMPRESA
          [4] ELIMINAR EMPRESA
          [5] SALIR DEL PROGRAMA
          """
    )
    print("=" * ancho)
    opcion = int(input("INGRESE UNA OPCION DEL MENÚ: "))
    os.system("clear")
    if opcion == 1:
        print("[1] REGISTRO DE NUEVA EMPRESA")
        ruc = input("RUC: ")
        razon_social = input("RAZON SOCIAL: ")
        ciudad = input("CIUDAD: ")
        dic_nueva_empresa = {"ruc": ruc, "razon_social": razon_social, "ciudad": ciudad}
        lista_empresas.append(dic_nueva_empresa)
    elif opcion == 2:
        print("[2] RELACION DE EMPRESAS")
        for dic_empresa in lista_empresas:
            print("*" * ancho)
            for clave, valor in dic_empresa.items():
                print(clave + ": " + valor)
            print("*" * ancho)
        input("presione enter para continuar...")
    elif opcion == 3:
        valor_busqueda = input("INGRESE RUC: ")
        posicion_busqueda = -1
        posicion_busqueda = buscar_empresa(valor_busqueda)
        if posicion_busqueda == -1:
            print("NO SE ENCONTRÓ EMPRESA")
        else:
            dic_empresa_busqueda = lista_empresas[posicion_busqueda]
            print("EMPRESA ENCONTRADA: " + dic_empresa_busqueda.get("razon_social"))
            razon_social = input("RAZON SOCIAL: ")
            ciudad = input("CIUDAD: ")
            dic_empresa_actualizar = {
                "ruc": dic_empresa_busqueda.get("ruc"),
                "razon_social": razon_social,
                "ciudad": ciudad,
            }
            lista_empresas[posicion_busqueda] = dic_empresa_actualizar
            print("Empresa Actualizada")
    elif opcion == 4:
        valor_busqueda = input("INGRESE RUC: ")
        posicion_busqueda = buscar_empresa(valor_busqueda)
        if posicion_busqueda == -1:
            print("NO SE ENCONTRÓ EMPRESA")
        else:
            lista_empresas.pop(posicion_busqueda)
            print("Empresa Eliminada !!!")
    elif opcion == 5:
        fsalida = open("empresas.csv", "w")
        fsalida.write(grabar_datos())
        fsalida.close()
        print("[5] ESTÁ SALIENDO DEL PROGRAMA")
    else:
        print("OPCIÓN NO VALIDA!!!")

    time.sleep(1)
    os.system("clear")
    time.sleep(1)
