# semana_laboral = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
# print("Semana laboral =", semana_laboral)
# print("Dia 1 =", semana_laboral[0])
# print("Dia 2 =", semana_laboral[1])
# print("Dia 3 =", semana_laboral[2])
# print("Dia 4 =", semana_laboral[3])
# print("Dia 5 =", semana_laboral[4])

################################################################################################

# print("Mostrar longitud de la lista = ", len(semana_laboral))
# print("Encontrar la posicion de Miercoles = ", semana_laboral.index("Miercoles"))
# semana_laboral.append("Sabado") # Agregar un valor a la lista
# print("Nuevo dato agregado a la lista = ", semana_laboral)
# del semana_laboral[5] # Borrar un elemento de la lista
# print("Dato \" Sabado \" eliminado de la lista")

################################################################################################

with open("datos.txt", "r") as txt:
    lista = txt.readlines()

#print(lista)

# Viasualizar linea por linea

# for linea in lista:
#     print(linea+"\n")

###############################################################################################
    
# Visualizar el numero de linea

# num_lines = 1
# for line in lista:
#     print(f"Ahorita estas en la linea: {num_lines}")
#     num_lines = num_lines + 1


################################################################################################

#verificar si hay lineas vacias

# num_lines = 1
# for line in lista:

#     if line.strip() == "": 
#         continue
#     print(f"Ahorita estas en la linea: {num_lines}")
#     num_lines = num_lines + 1

# print("FIN DEL ARCHIVO")
    

#################################################################################################
    
# Cuente las lineas que contiene el archivo y lo indique
    
#print(f"El archivo tiene {len(lista)} lineas")

# Cuando encuentre una linea que NO contenga texto indique que esa linea está vacía

for line in lista:
    if line.strip() == "":
       print("Esta linea está vacía")
    else:
        print(line)

# Muestra cuantas lineas tienen texto y cuantas no
    
# num_lines = 0
# vacia = 0
# for line in lista:
#     if line.strip() == "":
#         vacia = 1
#         num_lines = num_lines - 1
#     else:
#         num_lines = num_lines + 1
# print(f": El archivo tiene {num_lines} lineas con texto y {vacia} lineas vacias")

