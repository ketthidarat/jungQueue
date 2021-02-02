import 'package:flutter/material.dart';
import 'package:my_project/bar.dart';
import 'package:my_project/Screens/Welcome/welcome_screen.dart';
import 'package:my_project/constants.dart';
import 'Screens/Login/login_screen.dart';
import 'bar.dart';
import 'login01.dart';
import 'owner_bar.dart';
import 'work.dart';
import 'bar.dart';
import 'owner.dart';

class AddEvent extends StatelessWidget {
  // This widget is the root of your application.
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
