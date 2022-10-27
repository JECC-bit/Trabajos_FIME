![Link](https://portal.ucol.mx/content/micrositios/188/image/Escudo2021/1_Linea/UdeC%20Abajo_392.png).
# <center>Facultad de Ingeniería Mecánica y Électrica</center>
## <center>Ingeniería en Computación Inteligente</center>
### <center>Fundamentos de programación</center>
### <center>Estudiante: Jesus Eduardo Ceballos Contreras</center>
### <center>Profesor: Dr. Walter Alejandro Mata López</center>
### <center>Semestre y Grupo: 3°D</center>
### <center>Fecha: 26/10/2022</center>

### Durante ésta materia se vió la programación funcional en el lenguaje orientado a objetos Dart, a continuación se verá los apuntes y actividades realizadas para simulacro de exámen prático de la segunda evaluación. 

Aqui en el simulacro del exámen práctico se vió lo que son unas clases ya definidas por medi ode Setters y Getters al igual en otro simulacro se vieron el uso de constructores.

El simulacro es un programa que contenga ua clase Vehiculo y que contenga propiedades y metodos.
### Ejemplo del primer simulacro:


```python
void main(){

    Vehiculo info_carro = new Vehiculo();

    info_carro.no_de_llantas = 14;
    info_carro.color = "Azul";
    info_carro.modelo = "Corvette";
    info_carro.marca = "Chevrolet";
    info_carro.ficha();
}

class Vehiculo{
    int? _no_de_llantas;
    String? _color;
    String? _modelo;
    String? _marca;

    void arrancar(){
        print("Arrancando");
    }
    void correr(){
        print("Correriendo");
    }
    void frenar(){
        print("Frenando");
    }

    //Setters
    void set no_de_llantas(int no_de_llantas){
        _no_de_llantas = no_de_llantas;
    }

    void set color(String color){
        _color = color;
    }

    void set modelo(String modelo){
        _modelo = modelo;
    }

    void set marca(String marca){
        _marca = marca;
    }

    //Getters
    int get no_de_llantas{
        return _no_de_llantas!;
    }

    String get color{
        return _color!;
    }

    String get modelo{
        return _modelo!;
    }

    String get marca{
        return _marca!;
    }

    //mostrar valores
    void ficha(){
        print("Numero de llantas: $_no_de_llantas");
        print("Color: $_color");
        print("Modelo: $_modelo");
        print("Marca: $_marca");
    }
}
```

### De la siguiente manera se demuestra el siguiente problema pero resuelto con constructores.


```python
//constructor debe de llevar el mismo nombre de la clase, obligatoriamente 
    //this se usa para especificar que esa clase sera igual que la del metodo
    //en los constructores no usan o acceden los setter y getters pero se necesitan debideo a que si en un futuro se necesitan acceder a las propiedades de la clase sera por medio de ahi

    //ejemplo de constructor:

void main(){

    Vehiculo info_carro = new Vehiculo(4, "Azul", "Corvette", "Chevrolet");


    info_carro.ficha();
}

class Vehiculo{
    int? _no_de_llantas;
    String? _color;
    String? _modelo;
    String? _marca;

    void arrancar(){
        print("Arrancando");
    }
    void correr(){
        print("Correriendo");
    }
    void frenar(){
        print("Frenando");
    }

   

    //mostrar valores
    void ficha(){
        print("Numero de llantas: $_no_de_llantas");
        print("Color: $_color");
        print("Modelo: $_modelo");
        print("Marca: $_marca");
    }

    //forma larga de recibir el constructor
    Vehiculo(int no_de_llantas, String color, String modelo, String marca){
        this._no_de_llantas = no_de_llantas;
        this._color = color;
        this._modelo = modelo;
        this._marca = marca;

    }

    //Formar corta  de recibir el constructor
    Vehiculo(this._no_de_llantas, this._color, this._modelo, this._marca);
}
```
