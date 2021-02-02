import 'package:flutter/material.dart';

class DetailPage extends StatefulWidget {
  @override
  _DetailPageState createState() => _DetailPageState();
}

class _DetailPageState extends State<DetailPage> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'First Example',
      home: Scaffold(
        // appBar: AppBar(
        //   title: Text('Home Page'),
        // ),
        body: Center(
          child: Text('Hello World'),
        ),
      ),
    );
  }
}
