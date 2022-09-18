![Link](https://portal.ucol.mx/content/micrositios/188/image/Escudo2021/1_Linea/UdeC%20Abajo_392.png).

# <center>Facultad de Ingeniería Mecánica y Électrica</center>

## <center>Ingeniería en Computación Inteligente</center>

### <center>Fundamentos de programación</center>

### <center>Estudiante: Jesus Eduardo Ceballos Contreras</center>
### <center>Profesor: Dr. Walter Alejandro Mata López</center>
### <center>Semestre y Grupo: 3°D</center>
### <center>Fecha: 18/09/2022</center>

### Durante ésta materia se vió la programación funcional en el lenguaje orientado a objetos python, a continuación se verá los apuntes y actividades realizadas de la segunda clase. 

En la segunda clase se vió el como importar codigo desde otro archivo de python al igual el cómo importar codigo desde un directorio diferente usando ___"import"___ y ___"from"___.

Para el primer ejemplo que es el uso de  ___"import"___, se necesitó de archivos python externos creados que contienen el siguiente código:




* ### Archivo ___"sumar.py"___ contiene una función para sumar 2 valores:



```python
def sumar(a: int|float, b: int|float): #funcion que recibe 2 valores enteros
    return a+b #retorno de la sumatoria de los valores
```

* ### Archivo ___"restar.py"___ contiene una función para restar 2 valores:


```python
def restar(a: int|float, b: int|float): #funcion que recibe 2 valores enteros o flotantes
    return a-b #retorno de la resta de ambos valores
```

* ### Archivo ___"multiplicar.py"___ contiene una función para multiplicar 2 valores:


```python
def multiplicar(a: int|float, b: int|float): #funcion que recibe 2 valores enteros o flotantes
    return a*b #retorna el producto de 2 números

```

* ### Archivo ___"dividir.py"___ contiene una función para dividir 2 valores:


```python
def dividr(a: int|float, b: int|float): #funcion que recibe 2 valores enteros o flotantes
    return a/b #retorno de la división de 2 valores
```

* ### Archivo ___"cuadrado.py"___ contiene una función para el cuadrado de un numero:


```python
def cuadrado(a: int|float): #funcion que recibe un valor entero o flotante
    return a*a #retorno del numero cuadrado

```

### Desde el archivo principal con nombre ___"clase2.py"___, se importan los archivos y se asignan a una variable por medio de un alias para poder llamarlos, ejemplo:


```python
import sumar as s #imporata el archivo sumar.py y le asigna el alias de "s"
import restar as r #imporata el archivo restar.py y le asigna el alias de "r"
import multiplicar as m #imporata el archivo multiplicar.py y le asigna el alias de "m"
import dividir as d #imporata el archivo dividir.py y le asigna el alias de "d"
import cuadrado as c #imporata el archivo cuadrado.py y le asigna el alias de "c"
```

### Después se declara la funcion main, con la impresion del llamado de cada una de las funciones creadas en los archivos externos:


```python
if __name__ == "__main__": #funcion principal
    print(s.sumar(5,6)) #llama la funcion sumar desde el archivo con alias de "s"
    print(r.restar(6,10)) #llama la funcion restar desde el archivo con alias de "r"
    print(m.multiplicar(5, 10)) #llama la funcion multiplicar desde el archivo con alias de "m"
    print(d.dividr(4, 2)) #llama la funcion dividir desde el archivo con alias de "d"
    print(c.cuadrado(5)) #llama la funcion cuadrado desde el archivo con alias de "c"
    
    #los numeros dentro de los parentesis son los argumentos que se mandan a las funciones
```

***
## También se vió algunas formas de importar código como las siguientes:

se creó un archivo llamado ___"operaciones.py"___ donde se contienen las funciones de los archivos anteriores pero ahora en un solo programa:


```python
def multiplicar(a: int|float, b: int|float):
    return a*b

def sumar(a: int|float, b: int|float):
    return a+b

def restar(a: int|float, b: int|float):
    return a-b

def cuadrado(a: int|float):
    return a*a

def dividr(a: int|float, b: int|float):
    return a/b

```

Se demuestra el funcioinamiento de tales funciones usando la forma de importar usando "\*" que significa "all", o sea extraer todas las funciones del arhivo.


```python
from operaciones import * #importa todo el código del archivo operaciones al programa principal

if __name__ == "__main__":
    #llamado de funciones
    print(sumar(5,6))
    print(restar(6,10))
    print(multiplicar(5, 10))
    print(dividr(4, 2))
    print(cuadrado(5))
```

Otra forma fué creando una carpeta con el nombre de ___"ops"___ dónde contiene el archivo de ___"operaciones.py"___


```python
import ops.operaciones as op #Importa desde la carpeta ops el archivo operaciones y le asigna el alias de "op" para poderlo llamar en el main
import ops.sumar as s #importa el archivo sumar desde la carpeta ops y le asigna el alias de "s"
from ops.operaciones import multiplicar #importa el archivo operaciones desde la carpeta import pero selecciona la funcion multiplicar del archivo de oparciones

if __name__ == "__main__":
    print(op.cuadrado(5)) #llamado del primer import
    print(s.sumar(5,5)) #llamado del segundo import
    print(multiplicar(5,5)) # Uso del llamado de la funcion importada especificamente
```
