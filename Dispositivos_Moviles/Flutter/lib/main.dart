import 'package:flutter/material.dart';
import 'package:multipantallas/bienvenida.dart';

// Método main
void main() {
  runApp(const Primera());
}

class Primera extends StatelessWidget {
  const Primera({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Multiformularios",
      theme: ThemeData(primarySwatch: Colors.deepPurple),
      home: const Pantalla(),
    );
  }
}

class Pantalla extends StatefulWidget {
  const Pantalla({super.key});

  @override
  State<Pantalla> createState() => _PantallaState();
}

class _PantallaState extends State<Pantalla> {
  var txtLogin = TextEditingController();
  var txtPassword = TextEditingController();
  var nombre = "";
  var clave = " ";

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: const BoxDecoration(
        image: DecorationImage(
            image: AssetImage("img/fondo.jpg"), fit: BoxFit.cover),
      ),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        appBar: AppBar(
          title: const Text("Multiformularios"),
        ),
        body: ListView(
          children: [
            Container(
              padding:
                  const EdgeInsets.symmetric(vertical: 100, horizontal: 20),
              alignment: Alignment.center,
              child: Image.asset("img/logo.png"),
            ),
            Container(
              padding: const EdgeInsets.all(15),
              alignment: Alignment.center,
              child: TextField(
                textAlign: TextAlign.center,
                decoration: InputDecoration(
                  hintText: "Nombre de Usuario",
                ),
                controller: txtLogin,
              ),
            ),
            Container(
              padding: const EdgeInsets.all(15),
              alignment: Alignment.center,
              child: TextField(
                textAlign: TextAlign.center,
                decoration: InputDecoration(
                  hintText: "Clave de Usuario",
                ),
                obscureText: true,
                controller: txtPassword,
              ),
            ),
            Container(
              padding: const EdgeInsets.all(25),
              alignment: Alignment.center,
              child: ElevatedButton.icon(
                onPressed: () {
                  nombre = txtLogin.text;
                  clave = txtPassword.text;

                  if (nombre == "pelochas" && clave == "123") {
                    Navigator.of(context).push(
                      MaterialPageRoute<Null>(builder: (BuildContext context) {
                        return Bienvenida(nombre);
                      }),
                    );
                  } else {
                    showDialog(
                        context: context,
                        barrierDismissible: false,
                        builder: (BuildContext context) {
                          return AlertDialog(
                            title: const Text("Advertencia"),
                            icon: const Icon(
                              Icons.error,
                              color: Colors.red,
                              size: 40,
                            ),
                            content: const SingleChildScrollView(
                              child: ListBody(
                                children: [
                                  Text("Verifica tus Credenciales"),
                                ],
                              ),
                            ),
                            actions: [
                              TextButton(
                                  onPressed: () {
                                    Navigator.of(context).pop();
                                  },
                                  child: const Text("Aceptar")),
                            ],
                          );
                        });
                  }
                },
                label: const Text("Validar"),
                icon: const Icon(Icons.login),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
