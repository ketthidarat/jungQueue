import 'package:flutter/material.dart';
import 'package:my_project/bar.dart';
import 'package:my_project/Screens/Welcome/welcome_screen.dart';
import 'package:my_project/constants.dart';
import 'bar.dart';
import 'work.dart';
import 'bar.dart';
import 'owner.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.green,
        backgroundColor: Colors.greenAccent[50],
      ),
      home: BarNavy(),
    );
  }
}
