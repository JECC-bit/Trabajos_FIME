palabra = input("Ingresa la palabra a buscar: ")
with open("datos.txt", 'r') as archivo:
    txt = archivo.read()

if palabra in txt:
    print(f"Palabara {palabra} encontrada")

else:
    print("Palabra no encontrada")

