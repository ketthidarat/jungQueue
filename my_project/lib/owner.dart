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
