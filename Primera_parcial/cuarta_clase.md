![Link](https://portal.ucol.mx/content/micrositios/188/image/Escudo2021/1_Linea/UdeC%20Abajo_392.png).

# <center>Facultad de Ingeniería Mecánica y Électrica</center>

## <center>Ingeniería en Computación Inteligente</center>

### <center>Fundamentos de programación</center>

### <center>Estudiante: Jesus Eduardo Ceballos Contreras</center>
### <center>Profesor: Dr. Walter Alejandro Mata López</center>
### <center>Semestre y Grupo: 3°D</center>
### <center>Fecha: 18/09/2022</center>

### Durante ésta materia se vió la programación funcional en el lenguaje orientado a objetos python, a continuación se verá los apuntes y actividades realizadas de la cuarta clase. 

* Iniciamos con unos ejemplos de conversiones numéricas usando f strings


```python
numero_big=12321343783289
numero_big2=123213.43783289
numero_big3=0.43783289
#forma de separar numeros por coma, solo funciona con el caracter especial de coma ","
print(f"Esto es un numero decimal: {numero_big:,d}")

#Forma de separar numeros con numero flotante
print(f"Esto es un numero flotante:{numero_big:.3f}")

#Notacion cientifica
print(f"Esto es una expresion de notacion cientifica: {numero_big2:e}")

#quitar decimales
print(f"Decimales reducidos: {numero_big2:.2e}")

#porcentajes
print(f"Esto es un porcentaje: {numero_big3:%}")

#reducir decimales de porcentajes
print(f"Porcentaje reducido: {numero_big3:.2%}")

#Numeros binarios
print(f"Esto es una operacion binaria: {25 - 5:b}")

#escribir codigo ascii
print(f"Esto es un simbolo del ascii: {64:c}")

#hexadecimal
print(f"Numero hexadecimal: {255:x}")

#octal
print(f"Numero octal: {255:o}")
```

    Esto es un numero decimal: 12,321,343,783,289
    Esto es un numero flotante:12321343783289.000
    Esto es una expresion de notacion cientifica: 1.232134e+05
    Decimales reducidos: 1.23e+05
    Esto es un porcentaje: 43.783289%
    Porcentaje reducido: 43.78%
    Esto es una operacion binaria: 10100
    Esto es un simbolo del ascii: @
    Numero hexadecimal: ff
    Numero octal: 377
    

* ## Se dejó el siguiente ejercicio en clase:

    * ### Escribe una funcion que genere una tabla de multiplicar recibiendo como argumento la cantidad de numeros y la tabla a generar.


```python
def tabla(nm: int, tbl: int): #funcion que recibe los parametros enteros
    return f"{(nm+1)*tbl:^5}" #retorna el producto de 2 valores

def ntbl(rg: int, tbl2: int): #funcion para imprimir la tabla que recibe 2 valores enteros
    for i in range(rg): #ciclo para imprimir un numero determinado de tablas
        print(f"\n") #Imprime un salto de linea
        for i2 in range(tbl2): #ciclo para imprimir el total de numeros deseados
            print(f"{i2+1:^5} X {i+1:^5} = {tabla(i2, i+1)}") #Imprime la tabla con los valores solicitados

if __name__ == "__main__":
    ntbl(3, 5) #llama la funcion y manda como argumentos el numero de tablas y hasta que numero imprimir cada tabla
```

    
    
      1   X   1   =   1  
      2   X   1   =   2  
      3   X   1   =   3  
      4   X   1   =   4  
      5   X   1   =   5  
    
    
      1   X   2   =   2  
      2   X   2   =   4  
      3   X   2   =   6  
      4   X   2   =   8  
      5   X   2   =  10  
    
    
      1   X   3   =   3  
      2   X   3   =   6  
      3   X   3   =   9  
      4   X   3   =  12  
      5   X   3   =  15  
    
