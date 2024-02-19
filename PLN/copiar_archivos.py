doc1 = "datos"
doc2 = "respaldo"
arch1 = open(doc1+".txt", "r")
arch2 = open(doc2+".txt", "w")

aux = arch1.read()
new_arch = arch2.write(aux)
arch1.close()
arch2.close()
with open(doc2+".txt", 'r') as archivo:
    print(archivo.read())