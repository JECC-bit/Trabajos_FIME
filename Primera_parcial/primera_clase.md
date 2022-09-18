![Link](https://portal.ucol.mx/content/micrositios/188/image/Escudo2021/1_Linea/UdeC%20Abajo_392.png).

# <center>Facultad de Ingeniería Mecánica y Électrica</center>

## <center>Ingeniería en Computación Inteligente</center>

### <center>Fundamentos de programación</center>

### <center>Estudiante: Jesus Eduardo Ceballos Contreras</center>
### <center>Profesor: Dr. Walter Alejandro Mata López</center>
### <center>Semestre y Grupo: 3°D</center>
### <center>Fecha: 18/09/2022</center>

### Durante ésta materia se vió la programación funcional en el lenguaje orientado a objetos python, a continuación se verá los apuntes y actividades realizadas de la primer clase. 

* Primero creamos una función sencilla que suma 2 números llamada _"suma"_


```python
def suma(a, b): #creacion de la funcion con parametros a y b
    return a + b #retorno de la suma de los paramteros recibidos
```

* En seguida se inicializa con la función principal que se declara de la siguiente manera:


```python
if __name__ == "__main__":
```

* Después llamamos la función y le pasamos parámetros


```python
print(suma(2, 2))
```

Dando cómo resultado el siguiente programa:


```python
def suma(a, b):
    return a + b


if __name__ == "__main__":
    print(suma(2, 2))
```

    4
    

***
### Lo siguiente visto fueron las direcciones de memoria de una variable.
### Con el siguiente código accedemos y mostramos la dirección de memoria de las variables usando la función ___"id()"___:


```python
x = 10 #variable con valor 10
print(x, "addr:", id(x)) #Imprime en pantalla la direccion de memoria de la variable x
x = "Hola" #variable con valor de una cadena
print(x, "addr:", id(x)) #Imprime en pantalla la direccion de memoria de la variable x

#al cambiar variableno cambia la direccion de memoria por contener el mismo valor
y=10 #variablo con valor 10, igual que x
print(y, "addr:", id(y)) 

#Valor distinto asi sea por una mayuscula
z="HOla"
print(z, "addr:", id(z)) #con valores diferentes cambia la direccion de memoria
```

    10 addr: 3153577273936
    Hola addr: 3153663941936
    10 addr: 3153577273936
    HOla addr: 3153663942384
    

* Después se vió el cómo declara una función con argumentos especificando el tipo de dato a recibir y el tipo de dato de salida, por ejemplo:


```python
def suma2(a: int, b: int) -> int: #funcion que recibe dos datos enteros y regresa como salida un entero usando "->" despues de la funcion
    return a + b #retorna la suma de ambos datos recibidos

print(suma2(3, 3)) #imprime el resultado de los datos enviados como  argumetnos
```

    6
    

## se realizó las siguientes actividades con el siguiente enunciado:
* ## Escribir una funcion que reciba un mensaje y un nombre y escriba en pantalla "< mensaje > < nombre >"


```python
def imp(msj: str, nm: str) -> str:# Funcion que recibe como argumentos 2 cadenas y retorna un valor de tipo cadena
    return msj + " " + nm #retorno de la concatenacion de los argumentos recibidos y un espacion en blanco


print(imp("Hola", "Jesus")) #llamado de la funcion mandando las siguientes cadenas como argumentos "Hola" y "Jesus"
```

    Hola Jesus
    

* ## Escribir una funcion que reciba el nombre y la edad de una persona. El mensaje de salida tiene que ser "Hola < nombre> tienes < edad> años".


```python
def msj(nam: str, edd: int): # Funcion que recibe como argumentos una cadena y un valor entero
    print("Hola", nam, "tienes", edd, "años.") #concatenacion del mensaje


msj("Jesus", 20) #llamado dela funcion con los siguientes parametros
```

    Hola Jesus tienes 20 años.
    

* ## Escribir una funcion que reciba el año actual y el año de nacimiento, usando la funcion anterior enviando esta como argumento obtenga el mensaje: "hola < nombre> tienes < edad> años".


```python
def calcular_edd(ac: int, an: int) -> int: # Funcion que recibe como argumentos 2 enteros y retorna un valor de tipo entero
    return ac - an #retorna la resta de los datos ingresados


msj("Jesus", calcular_edd(2022, 2001)) #llama la funcion msj() hecha previamente en donde manda como argumento otra funcion para asi poder usar una funcion dentro de los argumentos de otra
```

    Hola Jesus tienes 21 años.
    
