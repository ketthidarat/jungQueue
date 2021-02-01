import 'package:flutter/material.dart';
import 'bar.dart';

class Owner extends StatefulWidget {
  @override
  _OwnerState createState() => _OwnerState();
}

class _OwnerState extends State<Owner> {
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'First Example',
      theme: ThemeData(
        primarySwatch: Colors.green,
        fontFamily: 'Sarabun',
        backgroundColor: Colors.greenAccent[50],
      ),
      home: Scaffold(
        appBar: AppBar(
          title: Text('เจ้าของรถ'),
        ),
        body: Center(
          child: Text('Hello World'),
        ),
      ),
    );
  }
}
