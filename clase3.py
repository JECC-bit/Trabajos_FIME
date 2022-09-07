# n1=10
# msg = "hola"

# print(n1,msg)
# print(str(n1)+msg)

# # fstrings
# print(f"{n1} {msg}")

# hacer una funcion que reciba el nombre de una persona, el año de ancimiento y el año actual 
#retornando el mensaje Hola <nombre>, tienes <edad> años

# if __name__ == "__main__":
# #diferentes formas de solucionarlo

#     def msn(nam: str,ann: int,ann_ac: int)->str:
#         print(f"Hola {nam}, tienes {ann_ac-ann} años")

#     def msn2(nam: str,ann: int,ann_ac: int)->str:
#         edad = ann_ac - ann
#         return f"Hola {nam}, tienes {edad} años"

#     def edd(anc:int, ana:int)->int:
#         return anc - ana

#     def nmm(namm: str, anc: int, ana: int)->str:
#         return f"Hola {namm}, tienes {edd(anc, ana)} años"

#     msn("Jesus", 2001, 2022)
#     print( msn2("Jesus", 2001, 2022))
#     print(nmm("Jesus", 2022, 2001))

# #Listas
# alumnos = ["Hugo", "Paco", "Luis", "Lupita"]
# print(f"Alumnos: {alumnos}")

# # A esto se le llama indexacion
# for i in range(len(alumnos)):
#     print(f"Alumnos: {alumnos[i]}")


# #Tuplas
# alumnos = ("Hugo", "Paco", "Luis", "Lupita")
# # A esto se le llama indexacion
# for i in range(len(alumnos)):
#     print(f"Alumno {i+1}: {alumnos[i]}")


#sets
# alumnos = {"Hugo", "Paco", "Luis", "Lupita"}
# print(f"Alumnos: {alumnos}")

#diccionario
# alumnos = {"nombre": "Hugo", "materia1": 10, "materia2": 5}
# print(f"Alumnos: {alumnos}")
# print(f"Alumnos: {alumnos['nombre']}")

# numeros_list = [1,2,123,1,2,3,4,5,4,4]
# numeros_set = {1,2,123,1,2,3,4,5,4,4}
# print(numeros_list)
# print(numeros_set)

alumnos = ["Hugo", "Paco", "Luis", "Lupita"]
encabezado = ["Nombre", "Est._Datos", "Prog_fuc", "Inglés"]
m_e_d = [9,7,9,8]
m_p_f = [10,9,8,10]
m_i = [10,8,8,9]
print(f"{encabezado[0]:^10} {encabezado[1]:^10} {encabezado[2]:^10} {encabezado[3]:^10}")

for i in range(len(alumnos)):
    print(f"{alumnos[i]:<10} {m_e_d[i]:^10} {m_p_f[i]:^10} {m_i[i]:^10}")