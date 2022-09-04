# def suma(a, b):
#   return a + b
#
#
# if __name__ == "__main__":
#   print(suma(2, 2))
#
# direcciones de memoria
# x = 10
# print(x, "addr:", id(x))
# x = "Hola"
# print(x, "addr:", id(x))
# y=10
# print(y, "addr:", id(y)) #al cambiar variableno cambia la direccion de memoria por contener el mismo valor
#
# z="HOla"
# print(z, "addr:", id(z)) #con valores diferentes cambia la direccion de memoria

# x=1
# print(x, " : ", id(x))
# x=x+1
# print(x, " : ", id(x))
# x=x+1
# print(x, " : ", id(x))
# x=x+1
# print(x, " : ", id(x))
# x=x+1
# print(x, " : ", id(x))
# x=x+1
# print(x, " : ", id(x))
# x=x+1
# print(x, " : ", id(x))
# x=x+1
# print(x, " : ", id(x))
# x=x+1
# print(x, " : ", id(x))
# x=x+1
# print(x, " : ", id(x))
# x=x+1
# print(x, " : ", id(x))
# x=x+1

# ":=" operador morsa

# def suma1(a, b):
#     return a + b


# funcion especificando tipos de datos, "->" indica la salida de la funcion
# def suma2(a: int, b: int) -> int:
#     return a + b
#
#
# print(suma1(2, 2))
# print(suma2(3, 3))
# instalar libreria mypy "pip install mypy"

# Escribir una funcion que reciba un mensaje y un nombre y escriba en pastalla "<mensaje> <nombre>"

def imp(msj: str, nm: str) -> str:
    return msj + " " + nm


print(imp("Hola", "Jesus"))


# Escribir una funcion que reciba el nombre y la edad de una persona. El mensaje de salida tiene que ser
# "Hola <nombre> tienes <edad> años".


def msj(nam: str, edd: int):
    print("Hola", nam, "tienes", edd, "años.")


msj("Jesus", 20)


# Escribir una funcion que reciba el año actual y el año de nacimiento, usando la funcion anterior
# enviando esta como argumento obtenga el mensaje: "hola <nombre> tienes <edad> años".

def calcular_edd(ac: int, an: int) -> int:
    return ac - an


msj("Jesus", calcular_edd(2022, 2001))
