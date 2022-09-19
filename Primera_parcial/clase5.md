![Link](https://portal.ucol.mx/content/micrositios/188/image/Escudo2021/1_Linea/UdeC%20Abajo_392.png).

# <center>Facultad de Ingeniería Mecánica y Électrica</center>

## <center>Ingeniería en Computación Inteligente</center>

### <center>Fundamentos de programación</center>

### <center>Estudiante: Jesus Eduardo Ceballos Contreras</center>
### <center>Profesor: Dr. Walter Alejandro Mata López</center>
### <center>Semestre y Grupo: 3°D</center>
### <center>Fecha: 18/09/2022</center>

### Durante ésta materia se vió la programación funcional en el lenguaje orientado a objetos python, a continuación se verá los apuntes y actividades realizadas de la quinta clase. 

En ésta clase se aprendió sobre el uso de listas y sus funciones que tienen.
* ### Forma de imprimir la longitud de una lista:


```python
lista1 = [1,2,3,4]
# imprimir la longitud de una cadena
print(len(lista1))
```

    4
    

* ### Forma de imprimir un valor en especifico de una lista:


```python
lista2 = [1,3.14,"a", True, [4,5,6], (1,2,3), {8,"a",5.4}]
# imprimir directamente un solo caracter
print(lista2[6])
```

    {8, 5.4, 'a'}
    

* ### Forma de agregar datos a una lista usando ___"append()"___:


```python
# Crear e imprimir una lista
lista_cal = []
# metodo append agrega un valor al final de la lista
lista_cal.append(5)
print(lista_cal)
lista_cal.append(8)
print(lista_cal)
```

    [5]
    [5, 8]
    

* ### Forma de agregar un dato usando ___"insert()"___:


```python
# insert parametros 1, es la pocision y despues valor
lista_cal.insert(0,6)
print(lista_cal)
```

    [6, 5, 8]
    

* ### Forma de rellanar una lista con valores del 1 al 10: 


```python
datos = []
for i in range(1,11):
    datos.append(i)

print(datos)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    

* ### Ejemplo para llegar al último valor de una lista:


```python
#llegar al ultimo valor de la lista con indices negativos -1
lista3 = [1,2,3,4,5,6,7,9,10]
print(lista3[-1])
```

    10
    

***
## Slices(rebanadas)

* ### Ejemplos de slices:


```python
#forma de indicar de que rango imprimir los datos
print(lista3[0:3])
#forma de imprimir la mitad de la lista al final
print(lista3[int(len(lista3)/2):])
#lo mismo de arriba pero al contrario
print(lista3[:int(len(lista3)/2)])
#imrpmir un rango
print(lista3[3:7])
#imrpmir un rango con numeros negativos
print(lista3[-6:-2])
```

    [1, 2, 3]
    [5, 6, 7, 9, 10]
    [1, 2, 3, 4]
    [4, 5, 6, 7]
    [4, 5, 6, 7]
    

* ### Actualizar los valores de una lista: 


```python
#forma de cmabiar el valor de una lista
listagg = [1,"dos",3,"cuatro"]
listagg[1]=2
print(listagg)
```

    [1, 2, 3, 'cuatro']
    


```python
#intento de querer cambiar el valor de una lista sin poder cambiar un valor(fallido)
listaggg = [1,"dos",3,"cuatro"]
listagg2 = listaggg
print(f"lista 1: {listaggg}")
print(f"lista 2: {listagg2}")
listagg2[1] = 2
print("----------")
print(f"lista 1: {listaggg}")
print(f"lista 2: {listagg2}")
```

    lista 1: [1, 'dos', 3, 'cuatro']
    lista 2: [1, 'dos', 3, 'cuatro']
    ----------
    lista 1: [1, 2, 3, 'cuatro']
    lista 2: [1, 2, 3, 'cuatro']
    


```python
#intento de querer cambiar el valor de una lista sin poder cambiar un valor(correcta)
listagg1 = [1,"dos",3,"cuatro"]
listagg2 = listagg1[:]
listagg1[1] = 2
print("----------")
print(f"lista 1: {listagg1}")
print(f"lista 2: {listagg2}")
```

    ----------
    lista 1: [1, 2, 3, 'cuatro']
    lista 2: [1, 'dos', 3, 'cuatro']
    

* ### Agregar valores con slices:


```python
#Forma de ingresar varios valores al mismo tiempo al final de la lista
lista1 = [0,1,2,3,4]
lista1[len(lista1):] = [5,6,7]
print(lista1)
```

    [0, 1, 2, 3, 4, 5, 6, 7]
    


```python
#Forma de ingresa varios valores al mismo tiempo al inicio de la lista
lista1[:0] = [5,6,7]
print(lista1)
```

    [5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7]
    

* ### Agregar una lista en otra lista:


```python
#Forma de agregar una lista a otra
lista11 = [5,6,7]
lista2 = [8,9,10]
lista11.extend(lista2)
print(lista11)
```

    [5, 6, 7, 8, 9, 10]
    

* ### Borrar elemntos de una lista:


```python
#Borrar elementos del lista1[0] o tambien del(lista1[0])
print(lista1)
#Borrar por slices
del(lista1[2:5])
print(lista1)
```

    [5, 6, 7, 0, 1, 2, 3, 4, 5, 6, 7, 5, 6, 7, 8, 9, 10]
    [5, 6, 2, 3, 4, 5, 6, 7, 5, 6, 7, 8, 9, 10]
    
