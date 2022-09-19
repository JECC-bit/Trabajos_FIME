![Link](https://portal.ucol.mx/content/micrositios/188/image/Escudo2021/1_Linea/UdeC%20Abajo_392.png).

# <center>Facultad de Ingeniería Mecánica y Électrica</center>

## <center>Ingeniería en Computación Inteligente</center>

### <center>Fundamentos de programación</center>

### <center>Estudiante: Jesus Eduardo Ceballos Contreras</center>
### <center>Profesor: Dr. Walter Alejandro Mata López</center>
### <center>Semestre y Grupo: 3°D</center>
### <center>Fecha: 18/09/2022</center>

### Durante ésta materia se vió la programación funcional en el lenguaje orientado a objetos python, a continuación se verá los apuntes y actividades realizadas de la tercera clase. 

### En ésta clase se vió el uso de los f strings, veamos el siguiente ejemplo:


```python
n1=10 #variable tipo entero 
msg = "hola" #variable str, o sea de tipo cadena

print(n1,msg) #forma de impromir un valor usando print y concatenar 2 variables
print(str(n1)+msg) #forma de imprimir la concatenacion de 2 valores convirtiendo el valor entero a string

#fstrings
print(f"{n1} {msg}") #Forma de imprimir variables con f strings y su escritura es dentro de un print
```

    10 hola
    10hola
    10 hola
    

* ## Se realizó la siguiente actividad con lo aprendido, "hacer una funcion que reciba el nombre de una persona, el año de ancimiento y el año actual retornando el mensaje Hola < nombre>, tienes < edad> años"


```python
if __name__ == "__main__": #funcion principal
 #diferentes formas de solucionarlo

    def msn(nam: str,ann: int,ann_ac: int)->str: #Funcion que recibe 2 valores enteros y regresa un valor de cadena
        print(f"Hola {nam}, tienes {ann_ac-ann} años") #imprime los valores leidos en una f string

    def msn2(nam: str,ann: int,ann_ac: int)->str: #Funcion que recibe 2 valores enteros y regresa un valor de cadena
        edad = ann_ac - ann #se realiza el calculo para retornar la edad
        return f"Hola {nam}, tienes {edad} años" #imprime los valores leidos en una f string

    def edd(anc:int, ana:int)->int: #Funcion que recibe 2 valores enteros y regresa un valor entero
        return anc - ana #se realiza el calculo para retornar la edad

    def nmm(namm: str, anc: int, ana: int)->str: #Funcion que recibe 2 valores uno entero y uno de cadena y regresa un valor de cadena
        return f"Hola {namm}, tienes {edd(anc, ana)} años" #imprime los valores leidos en una f string

    msn("Jesus", 2001, 2022) #Llamado de la primer funcion  
    print( msn2("Jesus", 2001, 2022)) #llamado de la segunda funcion 
    print(nmm("Jesus", 2022, 2001)) #LLamado de la cuarta funcion dónde dentro de la mis se lleva acabo algunas operaciones de la tercer funcion
```

***
* ## Ejemplo de listas:


```python
#Listas
alumnos = ["Hugo", "Paco", "Luis", "Lupita"] #asi se crea una lista y se le asignan valores string
print(f"Alumnos: {alumnos}") #Imprime los valores de la lista alumnos 

#A esto se le llama indexacion
for i in range(len(alumnos)): #ciclo que recorrer el largo de la lista
    print(f"Alumnos: {alumnos[i]}") #Imprision de valores de la lista por medio de indexacion
```

    Alumnos: ['Hugo', 'Paco', 'Luis', 'Lupita']
    Alumnos: Hugo
    Alumnos: Paco
    Alumnos: Luis
    Alumnos: Lupita
    

***
* ## Ejemplo de tuplas:


```python
#Tuplas
alumnos = ("Hugo", "Paco", "Luis", "Lupita") #Forma de crear una tupla
#A esto se le llama indexacion
for i in range(len(alumnos)): #ciclo para recorrer la lista
    print(f"Alumno {i+1}: {alumnos[i]}") #Imprime dato por dato de la tupla por medi ode indexacion
```

    Alumno 1: Hugo
    Alumno 2: Paco
    Alumno 3: Luis
    Alumno 4: Lupita
    

***
* ## Ejemplo de sets:


```python
#sets
alumnos = {"Hugo", "Paco", "Luis", "Lupita"} #Forma de declarar los sets
print(f"Alumnos: {alumnos}") #Impresion del set
```

    Alumnos: {'Luis', 'Paco', 'Hugo', 'Lupita'}
    

***
* ## Ejemplo de diccionarios:


```python
#diccionario
alumnos = {"nombre": "Hugo", "materia1": 10, "materia2": 5} #creacion del diccionario donde se pone el "key":"valor"
print(f"Alumnos: {alumnos}") #imprime todos los vaolres del diccionario y su key
print(f"Alumnos: {alumnos['nombre']}") #Imprime el valor del key especificado
```

    Alumnos: {'nombre': 'Hugo', 'materia1': 10, 'materia2': 5}
    Alumnos: Hugo
    

***
* ## Demostración de la diferencia entre sets y listas:


```python
numeros_list = [1,2,123,1,2,3,4,5,4,4] #lista
numeros_set = {1,2,123,1,2,3,4,5,4,4} #set
print(numeros_list) #Imprime la lista
print(numeros_set) #Imprime el set
#La diferencia es que la lista imprime todos los valores y los sets no imprimen valores repetidos
```

    [1, 2, 123, 1, 2, 3, 4, 5, 4, 4]
    {1, 2, 3, 4, 5, 123}
    

## <center>Pequeño ejemplo de una mini base de datos realizada cun listas en python:</center>


```python
alumnos = ["Hugo", "Paco", "Luis", "Lupita"] #lista que contiene los nombres de los alumnos
encabezado = ["Nombre", "Est._Datos", "Prog_fuc", "Inglés"] #lista donde estará el encabezado de la tabla
m_e_d = [9,7,9,8] #lista donde va la calificacion de est._datos
m_p_f = [10,9,8,10] #lista que contiene las calificaciones de porg_fuc
m_i = [10,8,8,9] #lista que contiene las calificaciones de ingles

print(f"{encabezado[0]:^10} {encabezado[1]:^10} {encabezado[2]:^10} {encabezado[3]:^10}")#Imprime la cabecera

for i in range(len(alumnos)): #ciclo para recorrer la lista alumnos
    print(f"{alumnos[i]:<10} {m_e_d[i]:^10} {m_p_f[i]:^10} {m_i[i]:^10}") #IMprime cada dato por medio de indexacion
    #:<10 y :^10 es un termino de f strings donde especifica el separado entre cada variable y en que sentido
```

      Nombre   Est._Datos  Prog_fuc    Inglés  
    Hugo           9          10         10    
    Paco           7          9          8     
    Luis           9          8          8     
    Lupita         8          10         9     
    
