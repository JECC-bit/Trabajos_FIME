# def funcc(espaciado: int):
#     alumnos = ["Hugo", "Paco", "Luis", "Lupita"]
#     encabezado = ["Nombre", "Est._Datos", "Prog_fuc", "Inglés"]
#     m_e_d = [9,7,9,8]
#     m_p_f = [10,9,8,10]
#     m_i = [10,8,8,9]
#     print(f"{encabezado[0]:^{espaciado}} {encabezado[1]:^{espaciado}} {encabezado[2]:^{espaciado}} {encabezado[3]:^{espaciado}}")

#     for i in range(len(alumnos)):
#         print(f"{alumnos[i]:*<{espaciado}} {m_e_d[i]:+^{espaciado}} {m_p_f[i]:^{espaciado}} {m_i[i]:^{espaciado}}")
#         #el * y el signo operativo +, muestran losespacios en blanco para demostrar los n espacios que se le ponen al programa
# if __name__ == "__main__":
#     funcc(10)






# numero_big=12321343783289
# numero_big2=123213.43783289
# numero_big3=0.43783289
# #forma de separar numeros por coma, solo funciona con el caracter especial de coma ","
# print(f"{numero_big:,d}")
# #Forma de separar numeros con numero flotante
# print(f"{numero_big:.3f}")
# #Notacion cientifica
# print(f"{numero_big2:e}")
# #quitar decimales
# print(f"{numero_big2:.2e}")
# #porcentajes
# print(f"{numero_big3:%}")
# #reducir decimales de porcentajes
# print(f"{numero_big3:.2%}")
# #Numeros binarios
# print(f"{25 - 5:b}")
# #escribir codigo ascii
# print(f"{64:c}")
# #hexadecimal
# print(f"{255:x}")
# #octal
# print(f"{255:o}")


"""
Escribe una funcion que genere una tabla de multiplicar recibiendo como argumento
la cantidad de numeros y la tabla a generar.

"""

def tabla(nm: int, tbl: int):
    return f"{(nm+1)*tbl:^5}"

def ntbl(rg: int, tbl2: int):
    for i in range(rg):
        print(f"\n")
        for i2 in range(tbl2):
            print(f"{i2+1:^5} X {i+1:^5} = {tabla(i2, i+1)}")

if __name__ == "__main__":
    ntbl(3, 5)



