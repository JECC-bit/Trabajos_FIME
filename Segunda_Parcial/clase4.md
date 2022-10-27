![Link](https://portal.ucol.mx/content/micrositios/188/image/Escudo2021/1_Linea/UdeC%20Abajo_392.png).
# <center>Facultad de Ingeniería Mecánica y Électrica</center>
## <center>Ingeniería en Computación Inteligente</center>
### <center>Fundamentos de programación</center>
### <center>Estudiante: Jesus Eduardo Ceballos Contreras</center>
### <center>Profesor: Dr. Walter Alejandro Mata López</center>
### <center>Semestre y Grupo: 3°D</center>
### <center>Fecha: 26/10/2022</center>

### Durante ésta materia se vió la programación funcional en el lenguaje orientado a objetos Dart, a continuación se verá los apuntes y actividades realizadas de la cuarta clase. 

En la cuarta clase el profesor nos enseñó a usar clases pero ya empleando el conocimiento en una calculadora de operaciones básicas aritmeticas.

### Veamos un ejemplos visto en clase:


```python
// calculadora

void main(){

    // Se crea instancia para llamar la funcion Calculadora 
    Calculadora miSuperCalculadora = new Calculadora();
    int n1, n2;
    n1 = 5;
    n2 = 10;

    //suma
    int res = miSuperCalculadora.suma(n1, n2);
    // primer forma
    print("$n1 + $n2 = $res");
    //segunda forma
    print("$n1 + $n2 = ${miSuperCalculadora.suma(n1, n2)}");

    //resta
    print("$n1 - $n2 = ${miSuperCalculadora.resta(n1, n2)}");

    //division
    print("$n1 / $n2 = ${miSuperCalculadora.div(n1, n2)}");

    //multiplicacion
    print("$n1 * $n2 = ${miSuperCalculadora.multi(n1, n2)}");

    //invocar funcion
    print(suma(2,2));

    //asignacion 
    var res = suma(2,3);
    print(res);
}


class Calculadora{

    // int suma(int a, int b){
    //     return a+b;
    // }//Forma imperativo para crear funciones
    int a = 0;
    int b = 0;
    int suma(int a, int b) =>  a+b;
    int resta(int a, int b) =>  a-b;//expresion declarativa para crear funciones cortas
    double div(int a, int b) =>  a/b;
    int multi(int a, int b) =>  a*b;
    //String imprimir(int res)=> return print(res);

}
```

### Usando el mismo ejemplo de la calculadora, el maestro nos enseñó a cómo poder leer datos ingresados por el usuario pero desde la misma consola de comandos.

### En el siguiente ejemplo de desmuestra su empleo:


```python
// calculadora

void main(List<String> args){
    Calculadora miSuperCalculadora = new Calculadora();
    
    if(args.length <= 2){


        miSuperCalculadora.a = int.parse(args[0]);
        miSuperCalculadora.b = int.parse(args[1]);

    }else{
        print("Error de argumentos");
        print("Ejemplo: dart main.dart valor1 valor2");
    }


    //suma
    int res = miSuperCalculadora.suma(miSuperCalculadora.a, miSuperCalculadora.b);
    // primer forma
    print("${miSuperCalculadora.a} + ${miSuperCalculadora.b} = $res");
    //segunda forma
    print("${miSuperCalculadora.a} + ${miSuperCalculadora.b} = ${miSuperCalculadora.suma(miSuperCalculadora.a, miSuperCalculadora.b)}");

    //resta
    print("${miSuperCalculadora.a} - ${miSuperCalculadora.b} = ${miSuperCalculadora.resta(miSuperCalculadora.a, miSuperCalculadora.b)}");

    //division
    print("${miSuperCalculadora.a} / ${miSuperCalculadora.b} = ${miSuperCalculadora.div(miSuperCalculadora.a, miSuperCalculadora.b)}");

    //multiplicacion
    print("${miSuperCalculadora.a} * ${miSuperCalculadora.b} = ${miSuperCalculadora.multi(miSuperCalculadora.a, miSuperCalculadora.b)}");


}


class Calculadora{

    // int suma(int a, int b){
    //     return a+b;
    // }//Forma imperativo
    int a = 0;
    int b = 0;
    int suma(int a, int b) =>  a+b;
    int resta(int a, int b) =>  a-b;//expresion declarativa  
    double div(int a, int b) =>  a/b;
    int multi(int a, int b) =>  a*b;

}
```

***
## <center>Actividad de clase</center>
### Crear una calculadora usando funciones y leyendo datos desde consola


```python
// // calculadora

void main(List<String> args){

    calcular(args[0], args[1], args[2]);

}

void calcular(a, operador, b){
    Calculadora miSuperCalculadora = new Calculadora();

    miSuperCalculadora.a = int.parse(a);
    miSuperCalculadora.b = int.parse(b);

    switch(operador){

        case "+":
            //suma
            print("${miSuperCalculadora.a} + ${miSuperCalculadora.b} = ${miSuperCalculadora.suma(miSuperCalculadora.a, miSuperCalculadora.b)}");
            break;

        case "-":
            //resta
            print("${miSuperCalculadora.a} - ${miSuperCalculadora.b} = ${miSuperCalculadora.resta(miSuperCalculadora.a, miSuperCalculadora.b)}");
            break;

        case "/":
            //division
            print("${miSuperCalculadora.a} / ${miSuperCalculadora.b} = ${miSuperCalculadora.div(miSuperCalculadora.a, miSuperCalculadora.b)}");
            break;
        
        case "*":
            //multiplicacion
            print("${miSuperCalculadora.a} * ${miSuperCalculadora.b} = ${miSuperCalculadora.multi(miSuperCalculadora.a, miSuperCalculadora.b)}");
            break;

    }
    

}

class Calculadora{
    int a = 0;
    int b = 0;
    int suma(int a, int b) =>  a+b;
    int resta(int a, int b) =>  a-b;//expresion declarativa  
    double div(int a, int b) =>  a/b;
    int multi(int a, int b) =>  a*b;
}
```

***
## <center>Segunda actividad de clase </center>
### Recibir el nombre de una persona en consola en el orden de primero apellidos y despues nombres para después imprimirlos por consola en el orden de nombres y apellidos


```python
void main(List<String> args){

    Datos nombre = new Datos();

    nombre.nombre_ordenado(nombre.n1=args[0], nombre.n2=args[1], nombre.n3=args[2], nombre.n4=args[3]);

}

class Datos{
    String n1= "", n2= "", n3= "", n4 = "";

    void nombre_ordenado(String n1, String n2, String n3, String n4)=> print("$n3 $n4 $n1 $n2");
}
```
