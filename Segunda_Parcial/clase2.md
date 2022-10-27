![Link](https://portal.ucol.mx/content/micrositios/188/image/Escudo2021/1_Linea/UdeC%20Abajo_392.png).
# <center>Facultad de Ingeniería Mecánica y Électrica</center>
## <center>Ingeniería en Computación Inteligente</center>
### <center>Fundamentos de programación</center>
### <center>Estudiante: Jesus Eduardo Ceballos Contreras</center>
### <center>Profesor: Dr. Walter Alejandro Mata López</center>
### <center>Semestre y Grupo: 3°D</center>
### <center>Fecha: 26/10/2022</center>

### Durante ésta materia se vió la programación funcional en el lenguaje orientado a objetos Dart, a continuación se verá los apuntes y actividades realizadas de la segunda clase.

En la segunda clase se vió el uso de opercaiones matematicas, conversiones, listas y entre otras cosas.

Comencemos con un ejemplo de opercaiones simples de aritmetica y algebra.


```python
import 'dart:math'
void main(List<String> args) {
  var n1 = 15;
  var n2 = 7;
  print("Suma: $n1 + $n2 = ${n1+n2}");
  print("Resta: $n1 - $n2 = ${n1-n2}");
  print("Multiplicacion: $n1 * $n2 = ${n1*n2}");
  print("Division: $n1 / $n2 = ${n1/n2}");
  //~=alt gr + +
  print("Division entera: $n1 ~/ $n2 = ${n1~/n2}");
  
  //potencias en import 'dart:math'
  print(pow(5,3));
  //funcion para obtener el maximo y minimo de numeros
  print("Maximo: ${max(5,3)}");
  print("Minimo: ${min(5,3)}");
  
  
  //operaciones matematicas
  print("Seno ${sin(45)}");
  print("Coseno ${cos(45)}");
  print("RAiz cuadrada ${sqrt(5)}");
    
  //Enteros como objetos, propiedades de enteros
  print(10.isOdd);
  print(10.isEven);
}
```

### Después se vió algunas formas de hacer incrementos y decrementos de valores de variables y formas de acortar algunas operaciones aritmeticas:


```python
void main(){
    //Incrementos
  var contador = 0;
  contador = contador + 1;
  print(contador);
  contador++;
  print(contador);
  ++contador;
  print(contador);
  contador+=2;
  print(contador);
  
  //Decrementos
  var contador2 = 0;
  contador2 = contador2 - 1;
  print(contador2);
  contador2--;
  print(contador2);
  --contador2;
  print(contador2);
  contador2-=2;
  print(contador2);
  
  
  //Producto
  var contador3 = 3;
  contador3 *= 2;//contador3 = contador3 * 2;
  
  //Divisor
  var contador4 = 3.0;
  contador4 /= 2;//contador4 = contador4 / 2;
  //modulo
  contador4 %= 2;
}
```

### Lo siguiente que se vió fué la diferencia y el uso de los tipos de datos constantes ___"const"___ y ___"final"___ :


```python
void main(){
      // Diferencias entre final y const
  // const
  const miEntero = 10; //Se ejecuta en tiempo de compilacion
  //miEntero=15; no se puede cambiar su valor una vez declarado
  print(miEntero);
  
  //final
  final finalEntero=5;// se ejecuta en tiempo de ejecucion
  print(finalEntero);
  //tambien se puede asignar el valor despues
  final valorDespues;
  valorDespues=6;
  print(valorDespues);
    
  //Ejemplo2 final
  
  final finalentero;
  print("Ingresa un texto");
  var numero = stdin.readLinesync();
  finalentero = numero;
  print("El mensaje es: $finalentero");
}
```

### Durante la clase también explicó el profesor los tipos de interpolaciones y sistemas numericos: 


```python
void main(){
  //Interpolacion de cadenas y diferencias
  var cadena1 = "Hola";
  var cadena2 = "Mundo";
  print(cadena1 + cadena2);
  print("$cadena1 $cadena2");
  
  //diferencia 
  var nombre = "Jesus";
  var edad = 50;
  print(nombre + edad.toString());
  print("$nombre $edad");
    
  //sistemas numericos
  
  //binario
  print(125.toRadixString(2));
  //octal
   print(125.toRadixString(8));
  //hexadecimal
   print(125.toRadixString(16));
  
  var numero = 0xFFFF;
  print(numero.runtimeType);
    
}
```

### Forma de crear listas en Dart, las listas pueden contener cualquier tipo de dato y hay diferentes formas de declararlas y asignarles valores como los ejemplos que se verán enseguida:


```python
void main(){
  //Listas
  var milista = [1, "hola", 9.8, true];
  print(milista);
  //agregar valores a la lista
  milista.add(3.1416);
  print(milista);
  
  //Con las listas hechas final, se les puede agregar elementos, con const ya no deja agregar elementos
  final milista = [1, "hola", 9.8, true];
  print(milista);
  //agregar valores a la lista
  milista.add(3.1416);
  print(milista);
  
  
  const milista = [1, "hola", 9.8, true];
  print(milista);
  //agregar valores a la lista
  milista.add(3.1416);
  print(milista);
  
  
  
  //Lista definida con tipo de dato
  /* puede llevar tipo de dato final, const, int, etc */List<int> milista = [1, 2, 9, 4];
  print(milista);
  //agregar valores a la lista
  milista.add(3);
  print(milista);
  
  
  //Lista final de valores constantes
  final milista = const [1, 2, 4, 5];
  print(milista);
  //agregar valores a la lista
  milista.add(7);//Aqui causa error en tiempo de compilacion porque no se pueden agregar valores por los datos constantes
  print(milista);
  
  
  //Recorrer valores de una lista
  final listas = [2,3,5,4,1];
  for(var i = 0; i< listas.length; i++){
    stdout.write("${listas[i]}-");
    //Diferencia entre stdout.write y print es que el print mete un enter cada que vez que se ejecuta y el stdout.write escribe todo en la misma linea
  }
}
```
