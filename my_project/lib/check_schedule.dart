import 'package:flutter/material.dart';
import 'main.dart';
import 'package:google_fonts/google_fonts.dart';

class CheckScedule extends StatelessWidget {
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.greenAccent[50],
        appBar: AppBar(
          title: Text("Check Scedule"),
        ),
        body: Center(
            child: Column(mainAxisSize: MainAxisSize.min, children: <Widget>[
          const SizedBox(height: 30),
          RaisedButton(
            onPressed: () {},
            child: Text('จองคิวเก็บเกี่ยวข้าว', style: TextStyle(fontSize: 20)),
          ),
        ])));
  }
}
