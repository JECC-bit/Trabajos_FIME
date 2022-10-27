![Link](https://portal.ucol.mx/content/micrositios/188/image/Escudo2021/1_Linea/UdeC%20Abajo_392.png).
# <center>Facultad de Ingeniería Mecánica y Électrica</center>
## <center>Ingeniería en Computación Inteligente</center>
### <center>Fundamentos de programación</center>
### <center>Estudiante: Jesus Eduardo Ceballos Contreras</center>
### <center>Profesor: Dr. Walter Alejandro Mata López</center>
### <center>Semestre y Grupo: 3°D</center>
### <center>Fecha: 26/10/2022</center>

### Durante ésta materia se vió la programación funcional en el lenguaje orientado a objetos Dart, a continuación se verá los apuntes y actividades realizadas de la tercera clase. 

La clase abarcó la seccion de Clases y en ella se vieron lo que son las clases, sus propiedades y métodos, también vimos las propiedades privadas y diferentes formas de declara una clase. Dentro de las clases también vimos lo que son métodos de insersión de datos y obtención de los mismos por medio de ___"Setters"___ y ___"Getters"___ 

### En seguida un ejemplo visto en clase de como hacer una clase User la cuál contiene propiedades privadas(Forma no correcta de agregar datos a propiedades privadas):


```python
void main(){
    var usuario1 = User();//instancia de la clase User
    //User usuario 2 = User(); otra forma de declarar
    usuario1._nombre = "Jesus";
    usuario1._edad = 20;
    usuario1.reporte();
 }

 // Todas las clases empiezan con mayusculas para poder diferenciar con una variable
 // con ? se puede indicar que es de valor nulo

 //encapsulamiento, consiste en ocultar los atributos de la clase, el simbolo "_" hace todo privado
 class User{
     //propiedades
     String? _nombre;
     int? _edad;
     //metodos
     void reporte(){
         print(_nombre);
         print(_edad);
     }

}

 //todos los orientados a objetos tienen seters
```

### En seguida otro ejemplo visto en clase de como hacer una clase User la cuál contiene propiedades privadas(Forma correcta de agregar datos a propiedades privadas con Setters y Getters):


```python
void main(){
    User usuario1 = User();
    usuario1.nombre = "Jesus";
    usuario1.edad = 20;
    usuario1.reporte();
    print(usuario1.nombre);
    print(usuario1.edad);
}

class User{
    //encapsulamiento de propiedades
    String? _nombre;
    int? _edad;

    //seters
    void set nombre(String nombre){
        _nombre = nombre;

    }

    void set edad(int edad){
        _edad = edad;
    }


    //getters
    String get nombre{
        //para indicar que si se puede imprimir un nulo con "!"
        return _nombre!;
    }

    int get edad{
        return _edad!;
    }

    void reporte(){
        print(_nombre);
        print(_edad);
    }

}
```

### En la misma clase también se vió lo que es el Scope de variables o ambitos, al igual que funciones fat arrow, como por ejemplo:


```python
int x = 25;
//Scope de variables o ambitos
void main(){

    var x = 5;

    void showNumber(){
        var y = 10;
        print(y);
        print(x);
    }

    showNumber();
    showX1();
    showX2();
}

//funciones fat arrow, arrow
void showX1(){
    print(x);
}

void showX2() => print(x); // funcion declarativa
```

***
## <center>Actividad en clase</center>
### Crear una clase estudiante con propiedades de nombre de la carrerar, semestre y numero de cuenta


```python
void main(){
    var estudiante1 = Estudiante();
    estudiante1.nombre_carrera = "ICI";
    estudiante1.numero_de_cuenta = "20176724";
    estudiante1.semestre = 3;
    estudiante1.reporte();
}

class Estudiante{
    //propiedades
    String? nombre_carrera;
    String? numero_de_cuenta;
    int? semestre;

    void reporte(){
        print("Carrera: $nombre_carrera");
        print("Nummero de cuenta: $numero_de_cuenta");
        print("Semestre: $semestre");
    }

}
```
