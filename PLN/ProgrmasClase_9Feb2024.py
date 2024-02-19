# Programa 1: Presentacion del uso basico de python

print("Universida de Colima")
print("Ingenieria en Computación Inteligente")

name = "Jesus Eduardo Ceballos Contreras"
print("Hola ", name)

edad = int(input("Ingresa tu edad: "))
print(name, "tiene la edad de: ", edad)
print("Operacion 1: ", 4*5-6)
x = 4+7
y = x-2
z = x+y

print("X: ", x)
print("Y: ", y)
print("Z: ", z)


#Programa 2: abrir en modo lecturar un archivo .txt

abrir = open("datos.txt", 'r')

texto = abrir.read()
print(texto)
abrir.close()


#Programa 3: Escritura en un archivo .txt

abrir = open("guardar.txt", "w")
abrir.write("Texto guardao en el archivo\n")
abrir.write("Texto escrito desde el programa\n")
abrir.write("Escribi esto desde python\n")
abrir.close()

leer = open("guardar.txt", "r")
leerTXT = leer.read()
leer.close()
print(leerTXT)