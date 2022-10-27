![Link](https://portal.ucol.mx/content/micrositios/188/image/Escudo2021/1_Linea/UdeC%20Abajo_392.png).
# <center>Facultad de Ingeniería Mecánica y Électrica</center>
## <center>Ingeniería en Computación Inteligente</center>
### <center>Fundamentos de programación</center>
### <center>Estudiante: Jesus Eduardo Ceballos Contreras</center>
### <center>Profesor: Dr. Walter Alejandro Mata López</center>
### <center>Semestre y Grupo: 3°D</center>
### <center>Fecha: 26/10/2022</center>

### Durante ésta materia se vió la programación funcional en el lenguaje orientado a objetos Dart, a continuación se verá los apuntes y actividades realizadas de la primer clase. 

En la primer clase se vieron cosas básicas sobre el lenguaje, comenzamos con un programa simple para entender su funcionamiento:


```python
void main() {
  print("hola mundo");
  print(2+2);
  print('Hola');
    
  // Comentario de una linea
  /* Comentario en 
   * bloque*/
}
```

### A continuación se muestran las tipo de variables que hay en el lenguaje Dart y el uso de interpolaciones de cadenas para poder mostrar valores de una variable en pantalla:


```python
void main() {
  print("hola mundo");
  print(2+2);
  print('Hola');
  // Comentario de una linea
  /* Comentario en 
   * bloque*/
  
  //Declaracion de variables de manera explicita
  String nombre = "Jesus";
  print(nombre);
  
  String apellido; 
  
  apellido = "Ceballos";
  print(apellido + nombre); // concatenacion
  
  // Tipado estatico, no puedo poner 20.5, python infiere en el tipo de dato
  //int
  int edad = 20;
  print(edad);
  
  //Float(Double)
  double gravedad = 9.81;
  print(gravedad);
  
  //tipo de dato de superclase num
  num numero =5;
  print(numero);
  numero = 9.81;
  print(numero);
  
  //Uso de dynamic
  dynamic variable = "Hola";
  print(variable);
  variable = 5;
  print(variable);
  variable = 9.81;
  print(variable);
  variable = true;
    print(variable);
  
  
  //interpolacion de cadenas
  print("Hola $nombre ${apellido} tienes $edad años");
  //la diferencia de poner o no poner llaves
  int aa= 2022;
  int an = 2001;
  print("Hola $nombre $apellido tienes ${aa - an} años");
  //Las llaves se usan para operaciones y el signo de pesos para pura variable
}
```

### Después se vió la forma de crear funciones en el lenguaje y también la forma de detectar un tipo de adto de una variable con el comando ___"runtimeType"___. También se vió la forma en la que se pueden leer valores por teclado.


```python
void main(){
    //llamado de funciones en interpolacines de cadenas
  print("Hola $nombre() $apellido() tienes ${calcularedad(2022, 2001)} años");
  
  
  
  //Leer valores por teclado
  print("dame tu edad: ");
  var edad2 = stdin.readLineSync(); //asignado en tiempo de ejecucion
  print(edad2 is int); // is, verifica el tipo de dato y regresa true o false
  print(edad2 is double);
  print(edad2 is bool);
  print(edad2 is String);
  //imprimir tipo de dato
  print(edad2.runtimeType);
  
  var status = espar(8);
  print(status.runtimeType);
  
  
  //recibir datos de tipo especifico
  var edad3 = int.parse(stdin.readLineSync()!);
  print(" $edad3 es de tipo ${edad3.runtimeType}");
}


// funciones
int calcularedad(int aa, int an){
  return aa - an;
}

String nombre(){
  return "Jesus";
}

String apellido(){
  return "Apellido";
}

bool espar(int num){
  if(num%2 == 0){
    return true;
  }
  else{
    return false;
  }
}
```

***
## <center>Actividad #1</center>
### Calculadora que lea los numeros del teclado y obtenga suma, resta, multiplicacion y division usando funciones


```python
import 'dart:io';
void main() {
  
  print("Ingresa un numero: ");
  var a = stdin.readLineSync();
  print("Ingresa otro numero: ");
  var b = stdin.readLineSync();
  
  print("La suma es = ${inpSuma(a, b)}");
  print("La resta es = ${inpResta(a, b)}");
  print("La multiplicacion es = ${inpMulti(a, b)}");
  print("La division es = ${inpDiv(a, b)}");
  
}

//funciones

int inpSuma(int a, int b){
  return a+b;
}

int inpResta(int a, int b){
  return a-b;
}

int inpMulti(int a, int b){
  return a*b;
} 

double inpDiv(double a, double b){
  return a/b;
}
```
