#                                <center>*UNIVERSIDAD DE COLIMA*</center>
##                     <center> FACULTA DE INGENIERIA MECANICA Y ELECTRICA</center>
###                          <center>  REPORTE DEL FUNCIONAMMIENTO DEL EXAMEN PRATICO</center>
####                           <center>ELABORADO POR: JESUS EDUARDO CEBALLOS CONTRERAS 3°D</center>



 ## *El maestro indicó una serie de instrucciones para llevar a cabo el exámen prático, son las siguientes:*
 

- ### 1) dar de alta un artículo con su ID, nombre artículo, precio unitario y existencia.
- ### 2) modificar un artículo en cualquiera de sus datos (menos el ID). 
- ### 3) eliminar un artículo de manera lógica o física de acuerdo con su ID.
- ### 4) consultar las existencias por ID 
- ### 5) Inventario total.


## *Programa que desarrollé por medio de funciones y varios temas vistos en clase.*
## *Para su desarrollo creé 5 archivos python en los cuáles; uno es el principal, otro es el de alta de los articulos(insert_alta.py), otro donde modifico los articulos(update_dto.py), uno donde elimino datos(delete_item.py), también otro para realizar consultas por ID(search_existencia.py) y por último el de inventario total lo realicé dentro del principal.* 


***
# <center>**Ahora vamos a explicar el programa de altas:** </center>


### Creamos una función llamada "input_id", la cuál llamaremos para leer el valor del id.


```python
def input_id()->int: #Aqui creamos una funcion llamada "input_id" para poder cambiar 
```

### Después se crea un ciclo while en donde condicionamos una variable para que éste se siga ciclando
### Dentro del ciclo se contiene la lectura del valor del id y su validación de que sea un digito


```python
respuesta = False #Variable que contendrá el valor booleano para tener un control sobre el ciclo
    while respuesta == False: #ciclo while condicionando la variable anterior usada como limitante
        identificador = input("Ingresa el ID: ") #Leer por teclado el valor de ID
        
        if identificador.isdigit()==False or int(identificador)<0: #Condicionamiento para saber si el dato ingresado es un digito
            print("valor no admitido, ingresalo de nuevo como numero entero") #mensaje para ingresar un valor digito
            
        else:
            respuesta=True #En caso de que si sea un digito, el ciclo se rompre haciendo verdadera la variable de control
    return identificador
```

### Función para saber si es *digito (identificador.isdigit())*
### Lo que hace isdigit() es comproba el un dato es digito, que en éste caso se usó para saber si es un número entero, ésta retorna **False** o **True** dependiendo el caso, se usa de la siguiente manera:


```python
if identificador.isdigit()==False or int(identificador)>0: #condicion donde compara si es digito positivo
            print("valor no admitido, ingresalo de nuevo como numero entero")
```

### En conclusión la función quedaría así:


```python
def input_id()->int: #Aqui creamos una funcion llamada "input_id" para poder cambiar 
    respuesta = False #Variable que contendrá el valor booleano para tener un control sobre el ciclo
    while respuesta == False: #ciclo while condicionando la variable anterior usada como limitante
        identificador = input("Ingresa el ID: ") #Leer por teclado el valor de ID
        
        if identificador.isdigit()==False or int(identificador)>0: #condicion donde compara si es digito positivo
            print("valor no admitido, ingresalo de nuevo como numero entero") #mensaje para ingresar un valor digito
            
         else:
            respuesta=True #En caso de que si sea un digito, el ciclo se rompre haciendo verdadera la variable de control
    return identificador
```

### Después se creó una función para cada lista similar a la explicada con anterioridad, por ejemplo la función "input_name" que sigue casi la misma lógica


```python
def input_name(): #Funcion para leer datos y guardar en la lista de nombre
    respuesta = False #variable similar para mantener un control del ciclo
    while respuesta == False: #ciclo para validar
        nam_art = input("Ingresa el nombre del articulo: ") #leer dato 
        
        if nam_art.isalpha()==False: #Condicion para comprobar si es valor alfanumerico
            print("Valor no admitido, ingresa un valor admitido")
            
        else:
            respuesta=True
    return nam_art
```

### Aquí se usó un nuevo método que es "isalpha()", el cuál lo que hace es comprobar si contiene valores alfanuméricos como se explica en el siguiente fragmento:


```python
if nam_art.isalpha()==False: #Condicion para comprobar si es valor alfanumerico
            print("Valor no admitido, ingresa un valor admitido")
```

### Enseguida creé la función para la lista de precio, la cuál lee los valores por teclado como se muestra a continuación:


```python
def input_precio(): #Nombre de la función para leer datos del precio
    respuesta = False #Variable de control
    while respuesta == False: #ciclo para la validacion del dato
        precio = input("Ingresa el precio del articulo $ ") #lectura del valor ingresado 
        
        if "." in precio or precio.isdigit(): #Condicionamiento para saber si el dato contiene un punto (.) o es digito
            precio = float(precio) #Conversion a float
            respuesta=True #Ruptura del ciclo
            
        else:
            print("Ingresa un dato valido") #Mensaje de alerta

    return precio
```

### Se usó una condición nueva dónde se detecta si el valor contiene un punto (.) con tal de ser de tipo flotante o tambien de caracter entero


```python
if "." in precio or precio.isdigit(): #Condicionamiento para saber si el dato contiene un punto (.) o es digito
            precio = float(precio) #Conversion a float
            respuesta=True #Ruptura del ciclo
```

### Por último se usó la ultima función que es para contener las existencias, nada fuera de lo ya explicado, es similar a la función de ID


```python
def input_existencia(): #Nombre de la funcion
    respuesta = False #variable de control
    while respuesta == False: 
        existencia = input("Ingresa la existencia total del producto: ") #Lectura del dato
        
        if existencia.isdigit()==False or int(existencia)>1: #Comprobar que sea un digito y positivo
            print("Valor no admitido, ingresa un valor admitido") #advertencia
            
        else:
            respuesta=True #Ruptura del ciclo

    return existencia
```

# **Código final del archivo insert_alta.py**


```python
def input_id()->int:
    respuesta = False
    while respuesta == False:
        identificador = input("Ingresa el ID: ")
        
        if identificador.isdigit()==False or int(identificador)>0:
            print("valor no admitido, ingresalo de nuevo como numero entero")
            
        else:
            respuesta=True
    return identificador

def input_name():
    respuesta = False
    while respuesta == False:
        nam_art = input("Ingresa el nombre del articulo: ")
        
        if nam_art.isalpha()==False:
            print("Valor no admitido, ingresa un valor admitido")
            
        else:
            respuesta=True
    return nam_art

def input_precio():
    respuesta = False
    while respuesta == False:
        precio = input("Ingresa el precio del articulo $ ")
        
        if "." in precio or precio.isdigit():
            precio = float(precio)
            respuesta=True
            
        else:
            print("Ingresa un dato valido")

    return precio

def input_existencia():
    respuesta = False
    while respuesta == False:
        existencia = input("Ingresa la existencia total del producto: ")
        
        if existencia.isdigit()==False or int(existencia)>1:
            print("Valor no admitido, ingresa un valor admitido")
            
        else:
            respuesta=True

    return existencia
```

***
# <center>Programa de modificar un articulo </center>

### A éste archivo lo llamé ___"update_dto.py"___ y contiene el siguiente código:


```python
def update_data(id1:int, modif:str, id_producto, nombre_art, precio, existencia):

    indice = id_producto.index(id1)
    match modif:

        case 'Nombre' | 'nombre':

            respuesta = False
            while respuesta == False:
                new_name = input("Ingresa el nuevo nombre del articulo: ")
                
                if new_name.isalpha()==False:
                    print("Valor no admitido, ingresa un valor admitido")
                    
                else:
                    respuesta=True

            nombre_art[indice]=new_name
            print("dato actualizado con exito")
            return nombre_art


        case 'Precio' | 'precio':

            respuesta = False
            while respuesta == False:
                new_precio = input("Ingresa el precio del articulo $ ")
                
                if "." in new_precio or new_precio.isdigit():
                    new_precio = float(new_precio)
                    respuesta=True
                    
                else:
                    print("Ingresa un dato valido")

            precio[indice]=new_precio
            print("dato actualizado con exito")
            return precio


        case 'Existencia' | 'existencia':

            respuesta = False
            while respuesta == False:
                new_existencia = input("Ingresa la existencia total del producto: ")
                
                if new_existencia.isdigit()==False or int(new_existencia)>1:
                    print("Valor no admitido, ingresa un valor admitido")
                    
                else:
                    respuesta=True
            existencia[indice]=int(new_existencia)
            print("dato actualizado con exito")
            return existencia


        case other:
            print("ingresa un valor admitido")
```

### iniciamos con el nombre de la función que es ___"update_data()"___


```python
def update_data(id1:int, modif:str, id_producto, nombre_art, precio, existencia):
#funcion que contiene parámteros en los cuáles son:
#id1 es el id registrado por teclado y enviado desde el programa principal
#modif es el nombre de la lista a modificar registrado por teclado y enviado desde el programa principal
#id_producto es la lista que contiene todos los id registrados
#nombre_art es la lista que contiene todos los nombres registrados
#precio es la lista que contiene todos los precios registrados
#existencia es la lista que contiene todos los datos de existencias registrados
```

### Aquí usamos una nueva función que es ___".index()"___
### index() lo que hace es buscar un dato indicado y te regresa como valor la posicion en la que se encuentra el valor dentro de la lista, en caso de no encontreralos regresa un error.


```python
indice = id_producto.index(id1) #se busca el indice en el que se encuentra la id leida y que contiene la variable id1.
```

### Enseguida se encuentra el comando "match", match lo que hace es imitar el funcionamiento de un switch que se usa en otros lenguajes, contiene case (casos), los cuales pueden ser números, flotantes, strings, pueden tener condiciones, etc.

### Código match:


```python
match modif: #se coloca la variable modif que es la que contiene el nombre de la lista a modificar

        case 'Nombre' | 'nombre': #caso de que sea Nombre o nombre, aqui uso el operador "or" con el simbolo de pipe para validar si se escribe con mayusculas o minusculas

            respuesta = False #variable de control para el ciclo
            while respuesta == False: #ciclo para leer nuevo valor y validarlo
                new_name = input("Ingresa el nuevo nombre del articulo: ") #lectura del nuevo valor
                
                #Validacion de si es alfanumerico
                if new_name.isalpha()==False: 
                    print("Valor no admitido, ingresa un valor admitido")
                    
                else:
                    respuesta=True #Ruptura del ciclo

            nombre_art[indice]=new_name #aqui se reemplaza el dato nuevo en la lista con el indice obtenido por la funcion de index()
            print("dato actualizado con exito")
            return nombre_art #retorno de la lista actualizaada


        case 'Precio' | 'precio': #caso de que sea Precio o precio, aqui uso el operador "or" con el simbolo de pipe para validar si se escribe con mayusculas o minusculas

            respuesta = False #variable de control para el ciclo
            while respuesta == False: #ciclo para leer nuevo valor y validarlo
                new_precio = input("Ingresa el precio del articulo $ ") #lectura del nuevo valor
                
                #Validacion de si es digito o contiene punto flotante
                if "." in new_precio or new_precio.isdigit():
                    new_precio = float(new_precio)
                    respuesta=True #Ruptura del ciclo
                    
                else:
                    print("Ingresa un dato valido")

            precio[indice]=new_precio #aqui se reemplaza el dato nuevo en la lista con el indice obtenido por la funcion de index()
            print("dato actualizado con exito")
            return precio #retorno de la lista actualizaada


        case 'Existencia' | 'existencia': #caso de que sea Existencia o existencia, aqui uso el operador "or" con el simbolo de pipe para validar si se escribe con mayusculas o minusculas

            respuesta = False #variable de control para el ciclo
            while respuesta == False: #ciclo para leer nuevo valor y validarlo
                new_existencia = input("Ingresa la existencia total del producto: ") #lectura del nuevo valor
                
                #Validacion de si es digito positivo
                if new_existencia.isdigit()==False or int(new_existencia)>1:
                    print("Valor no admitido, ingresa un valor admitido")
                    
                else:
                    respuesta=True #Ruptura del ciclo
            existencia[indice]=int(new_existencia) #aqui se reemplaza el dato nuevo en la lista con el indice obtenido por la funcion de index()
            print("dato actualizado con exito")
            return existencia #retorno de la lista actualizaada


        case other: #caso other se usa como mensaje default en caso de que no se ingrese un caracter de los case anteriores
            print("ingresa un valor admitido")
```

***
# <center>Programa de eliminar un articulo</center>

### Archivo llamado ___"delete_item.py"___ y contiene el siguiente breve código:


```python
def delete_item(id1:int, id_producto, nombre_art, precio, existencia):
    indice = id_producto.index(id1)
    nombre_art.pop(indice)
    precio.pop(indice)
    existencia.pop(indice)
    id_producto.pop(indice)
    print("Datos borrados con exito")
    return nombre_art, precio, existencia, id_producto
```

### Aqui la función contiene solo 5 argumentos ya conocidos antes:


```python
def delete_item(id1:int, id_producto, nombre_art, precio, existencia):
#funcion que contiene parámteros en los cuáles son:
#id1 es el id registrado por teclado y enviado desde el programa principal
#id_producto es la lista que contiene todos los id registrados
#nombre_art es la lista que contiene todos los nombres registrados
#precio es la lista que contiene todos los precios registrados
#existencia es la lista que contiene todos los datos de existencias registrados
```

### Después se usa la función ___"index()"___ ya mencionada para obtener la pocisión del id leído
### También se usó la función ___"pop()"___ para poder eliminar un dato en la posición indicada por medio del valor obtenido de index()


```python
indice = id_producto.index(id1) #obtención de la posición del id ingresado y almacenado en la variable id1
#Eliminación del dato en el indice obtenido por index()
nombre_art.pop(indice) 
precio.pop(indice)
existencia.pop(indice)
id_producto.pop(indice)
print("Datos borrados con exito")
return nombre_art, precio, existencia, id_producto #retorno de las listas modificadas
```

***
# <center>Programa de Consultar existencias</center>

### El programa lleva por nombre ___"search_existencia.py"___ y contiene el siguiente código:


```python
def search_id(id1: int, id_producto, nombre_art, precio, existencia):
    indice = id_producto.index(id1)
    encabezado=["ID", "Nombre", "Precio", "Existencia"]
    print(f"{encabezado[0]:^10} {encabezado[1]:^10} {encabezado[2]:^10} {encabezado[3]:^10}")
    print(f"{id_producto[indice]:^10} {nombre_art[indice]:^10} {precio[indice]:^10} {existencia[indice]:^10} ")
```

### Dónde sus argumentos son exactamente iguales que los anteriores


```python
def search_id(id1: int, id_producto, nombre_art, precio, existencia):
    
#funcion que contiene parámteros en los cuáles son:
#id1 es el id registrado por teclado y enviado desde el programa principal
#id_producto es la lista que contiene todos los id registrados
#nombre_art es la lista que contiene todos los nombres registrados
#precio es la lista que contiene todos los precios registrados
#existencia es la lista que contiene todos los datos de existencias registrados
```

### Se crea una mini tabla donde se muestra al usuario los datos relacionados del id seleccionadopor ejemplo:


```python
def search_id(id1: int, id_producto, nombre_art, precio, existencia):
    indice = id_producto.index(id1) #obtención de la posición del id ingresado y almacenado en la variable id1
    encabezado=["ID", "Nombre", "Precio", "Existencia"] #lista que contiene el encabezado de la lista
    print(f"{encabezado[0]:^10} {encabezado[1]:^10} {encabezado[2]:^10} {encabezado[3]:^10}") #impresion de la cabecera
    print(f"{id_producto[indice]:^10} {nombre_art[indice]:^10} {precio[indice]:^10} {existencia[indice]:^10} ") #Impresion de los datos con indice especificado

#variables extra, usualmente éstas ya mandan datos desde el main, se les accinó valores para su demostracion
id1 = 12
id_producto =[12, 23, 5]
nombre_art=['coca', 'sabritas', 'agua']
precio=[12.5, 12, 10]
existencia=[5, 3, 2]
search_id(id1, id_producto, nombre_art, precio, existencia)
```

        ID       Nombre     Precio   Existencia
        12        coca       12.5        5      
    

***
# <center>Programa principal(main)</center>

### El prgrama principal está algo extenso pero explicaré parte por parte para que se entienda.
### Contiene el nombre de ___"main.py"___ y tiene el siguiente código:


```python
import insert_alta
import search_existencia
import update_dto
import delete_item

if __name__ == '__main__':

    salir = True

    id_producto=[]
    nombre_art=[]
    precio=[]
    existencia=[]
    res=True
    terminos = ['Nombre', 'nombre', 'Precio', 'precio', 'Existencia' ,'existencia']

    while salir == True:
        print("\n\t\t\tMenu de datos\n\n")
        print("\t 1.- Dar de alta un producto \n")
        print("\t 2.- Modificar un articulo \n")
        print("\t 3.- Eliminar un articulo \n")
        print("\t 4.- Consultar existencia \n")
        print("\t 5.- Ver inventario total \n")
        print("\t 6.- Salir \n\n")
        decision = int(input("\tIngresa el numero de la opcion deseada: "))

        match decision:
            case 1:
                print("\n\t Dar de alta un producto \n")
                
                unic_id=int(insert_alta.input_id())
                while res==True:
                    if unic_id in id_producto:
                        print("Id repetida")
                        unic_id=int(insert_alta.input_id())
                    else:
                        id_producto.append(unic_id)
                        res=False
                res=True
                nombre_art.append(str(insert_alta.input_name()))
                precio.append(float(insert_alta.input_precio()))
                existencia.append(int(insert_alta.input_existencia())) 
                print(f"{id_producto} {nombre_art} {precio} {existencia}")
                print("datos guardados")

            case 2:
                encabezado=["ID", "Nombre", "Precio", "Existencia"]
                print(f"{encabezado[0]:^10} {encabezado[1]:^10} {encabezado[2]:^10} {encabezado[3]:^10}")
                for i in range(len(id_producto)):
                    print(f"{id_producto[i]:^10} {nombre_art[i]:^10} {precio[i]:^10} {existencia[i]:^10}")
                while res==True:
                    id1 = int(input("Ingresa el id del producto a modificar: "))
                    if id1 not in id_producto:
                        print("Ingresa un Id valido")        
                    else:
                       res=False
                res=True
                while res==True:
                    modif = str(input("Ingresa el nombre del campo a modificar, Nombre, Precio o Existencia: "))
                    if modif not in terminos:
                        print("Ingresa un dato valido")
                    else:
                        res=False

                update_dto.update_data(id1, modif, id_producto, nombre_art, precio, existencia)
                print(f"{id_producto} {nombre_art} {precio} {existencia}")


            case 3:
                encabezado=["ID", "Nombre", "Precio", "Existencia"]
                print(f"{encabezado[0]:^10} {encabezado[1]:^10} {encabezado[2]:^10} {encabezado[3]:^10}")
                for i in range(len(id_producto)):
                    print(f"{id_producto[i]:^10} {nombre_art[i]:^10} {precio[i]:^10} {existencia[i]:^10}")

                id1=int(input("\tIngresa el id del producto a eliminar\n\n"))
                delete_item.delete_item(id1, id_producto, nombre_art, precio, existencia)

            case 4:
                print("\tConsultar existencias")
                id1=int(input("Ingresa el ID del producto: "))
                if id1 in id_producto:
                    search_existencia.search_id(id1, id_producto, nombre_art, precio, existencia)
                else:
                    print("ID no existente, intente de nuevo")

            case 5:
                print("\n\tInventario\n\n")
                encabezado=["ID", "Nombre", "Precio", "Existencia"]
                print(f"{encabezado[0]:^10} {encabezado[1]:^10} {encabezado[2]:^10} {encabezado[3]:^10}")
                for i in range(len(id_producto)):
                    print(f"{id_producto[i]:^10} {nombre_art[i]:^10} {precio[i]:^10} {existencia[i]:^10}")

            case 6:
                salir=False

            case other:
                print("selecciona una opcion correcta")
```

### El programa inicia importando los archivos que contienen lasfunciones antes mencionadas.


```python
import insert_alta
import search_existencia
import update_dto
import delete_item
```

### Después declaramos la función principal y las listas junto con otras variables necesarias.


```python
if __name__ == '__main__': #función principal

    salir = True #variable de control para el ciclo del menú

    id_producto=[] #lista
    nombre_art=[] #lista
    precio=[] #lista
    existencia=[] #lista
    res=True # variable de control para validaciones
    terminos = ['Nombre', 'nombre', 'Precio', 'precio', 'Existencia' ,'existencia'] #lista que contiene encabezados
```

### A continuación puse un ciclo que es el que estará repitiendo el menú hasta que el usuario decida dejar de usarlo 


```python
while salir == True:
    #Impresion del menú
        print("\n\t\t\tMenu de datos\n\n")
        print("\t 1.- Dar de alta un producto \n")
        print("\t 2.- Modificar un articulo \n")
        print("\t 3.- Eliminar un articulo \n")
        print("\t 4.- Consultar existencia \n")
        print("\t 5.- Ver inventario total \n")
        print("\t 6.- Salir \n\n")
        decision = int(input("\tIngresa el numero de la opcion deseada: ")) #Variable que contiene el número seleccionado por el usuario de la operacion a realizar

```

### Continuamos con un match para condicionar la opción leída e ingresada por el usuario


```python
 match decision:
```

### caso1:


```python
case 1:
    print("\n\t Dar de alta un producto \n") #mensaje
                
    unic_id=int(insert_alta.input_id()) #variable que lee un id por medio de la funcion importada llamda input_id()
    while res==True: #Ciclo para la validacion de que sea un Id unico
        if unic_id in id_producto: #condicion que compara el dato obtenido con los almacenados en la lista id_producto
            print("Id repetida") #mensaje
            unic_id=int(insert_alta.input_id()) #Vuelve a ejecutar la funcion para lectura de un nuevo id
        else:
            id_producto.append(unic_id) #en caso de que la id sea única se agrega a la lista con append
            res=False #ruptura del ciclo
    res=True #Regreso valor principal a variable de control
    nombre_art.append(str(insert_alta.input_name())) #variable que lee un nombre por medio de la funcion importada llamda input_name()
    precio.append(float(insert_alta.input_precio())) #variable que lee un id por medio de la funcion importada llamda input_precio()
    existencia.append(int(insert_alta.input_existencia())) #variable que lee un id por medio de la funcion importada llamda  input_existencia()
    print(f"{id_producto} {nombre_art} {precio} {existencia}") #imprime las los datos de las listas
    print("datos guardados") #mensaje

           
```

### caso2:


```python
            case 2:
        #Imprime las listas en orden para que el usuario las pueda ver y seleccionar la opcion deseada
                encabezado=["ID", "Nombre", "Precio", "Existencia"] #lista con datos de la cabecera
                print(f"{encabezado[0]:^10} {encabezado[1]:^10} {encabezado[2]:^10} {encabezado[3]:^10}") #impresion de la cabecera
                for i in range(len(id_producto)): #ciclo para recorrer todas las listas en todos sus indices
                    print(f"{id_producto[i]:^10} {nombre_art[i]:^10} {precio[i]:^10} {existencia[i]:^10}") #imprime las listas
                     
                while res==True: #ciclo para validar que sea un id existente
                    id1 = int(input("Ingresa el id del producto a modificar: ")) #lectura del id a seleccionar
                    if id1 not in id_producto: #condicion para saber si el id ingresado no esta en la lista de id's, esto se hace con "not in" que significa "no está en"
                        print("Ingresa un Id valido")        
                    else:
                       res=False #Fin del ciclo
                res=True #Regresamos la variable de control a su valor normal
                
                while res==True: #ciclo para validar un campo una lista existente
                    modif = str(input("Ingresa el nombre del campo a modificar, Nombre, Precio o Existencia: ")) #lectura de datos
                    if modif not in terminos: #condicion para saber si el nombre ingresado no esta en la lista de terminos que contiene el nombre de las listas a modificar, esto se hace con "not in" que significa "no está en"
                        print("Ingresa un dato valido")
                    else:
                        res=False #fin bucle
                        
                
                #Ejecucion de la funcion update.data()
                #la cuál contiene los parametros de las listas y los nuevos datos leidos
                update_dto.update_data(id1, modif, id_producto, nombre_art, precio, existencia) 
                
                #impresion de las listas
                print(f"{id_producto} {nombre_art} {precio} {existencia}")
```

### caso3:


```python
            case 3:
       #Imprime las listas en orden para que el usuario las pueda ver y seleccionar la opcion deseada
                encabezado=["ID", "Nombre", "Precio", "Existencia"] #lista con datos de la cabecera
                print(f"{encabezado[0]:^10} {encabezado[1]:^10} {encabezado[2]:^10} {encabezado[3]:^10}") #impresion de la cabecera
                for i in range(len(id_producto)): #ciclo para recorrer todas las listas en todos sus indices
                    print(f"{id_producto[i]:^10} {nombre_art[i]:^10} {precio[i]:^10} {existencia[i]:^10}") #imprime las listas

                id1=int(input("\tIngresa el id del producto a eliminar\n\n")) #Lee el id del producto a eliminar
                delete_item.delete_item(id1, id_producto, nombre_art, precio, existencia) #manda a llamar la funcion con los parametros necesarios
```

### caso4:



```python
            case 4:
                print("\tConsultar existencias") #mensaje
                id1=int(input("Ingresa el ID del producto: ")) #Lee el id del producto a mostrar en existencia
                if id1 in id_producto: #condicion para saber si el id ingresado existe dentro de la lista de id's
                    search_existencia.search_id(id1, id_producto, nombre_art, precio, existencia) #si existe, llama lafuncion search_id()
                else:
                    print("ID no existente, intente de nuevo") #Sino esxite el id, no muestra nada mas que éste mensaje de error
```

### caso5:



```python
            case 5:
                print("\n\tInventario\n\n") #mensaje
                #Imprime las listas en orden para que el usuario las pueda ver y seleccionar la opcion deseada
                encabezado=["ID", "Nombre", "Precio", "Existencia"] #lista con datos de la cabecera
                print(f"{encabezado[0]:^10} {encabezado[1]:^10} {encabezado[2]:^10} {encabezado[3]:^10}") #impresion de la cabecera
                for i in range(len(id_producto)): #ciclo para recorrer todas las listas en todos sus indices
                    print(f"{id_producto[i]:^10} {nombre_art[i]:^10} {precio[i]:^10} {existencia[i]:^10}") #imprime las listas
```

### caso6 y other:


```python
            case 6:
                salir=False #rompe el ciclo del menú para darle fin a la ejecución

            case other:
                print("selecciona una opcion correcta") #caso default, imprime un mensaje en caso de seleccionar una opción no existente
```
