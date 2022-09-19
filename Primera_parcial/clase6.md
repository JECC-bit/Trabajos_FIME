![Link](https://portal.ucol.mx/content/micrositios/188/image/Escudo2021/1_Linea/UdeC%20Abajo_392.png).

# <center>Facultad de Ingeniería Mecánica y Électrica</center>

## <center>Ingeniería en Computación Inteligente</center>

### <center>Fundamentos de programación</center>

### <center>Estudiante: Jesus Eduardo Ceballos Contreras</center>
### <center>Profesor: Dr. Walter Alejandro Mata López</center>
### <center>Semestre y Grupo: 3°D</center>
### <center>Fecha: 18/09/2022</center>

### Durante ésta materia se vió la programación funcional en el lenguaje orientado a objetos python, a continuación se verá los apuntes y actividades realizadas de la sexta clase. 

### En la sexta clase de la parcial se vieron las funciones y sus diferentes tipos de parámetros.

* ### Ejemplo de parámetros posicionales:


```python
#parametros posicionales
def suma(a,b):
    return a/b

print(suma(b=0, a=2)) #Retorna error porque no se puede dividir entre cero
```

* ### Ejemplo de valor por defecto:


```python
#valor por defecto
def suma(a,b, c=0):
    return a/b+c

print(suma(b=2, a=0))
```

    0.0
    

* ### Ejemplo de valores asignados: 


```python
#diferentes formas con asignados
def suma(a=0,b=0,c=0):
    return a+b+c

print(suma(2.3))
print(suma(2,3,4))
print(suma(b=5))
print(suma(6,b=5))
```

    2.3
    9
    5
    11
    
