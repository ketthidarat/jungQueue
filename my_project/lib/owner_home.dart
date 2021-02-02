import 'package:flutter/material.dart';
import 'main.dart';
import 'package:google_fonts/google_fonts.dart';

class OwnerHome extends StatelessWidget {
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.greenAccent[50],
        appBar: AppBar(
          title: Text("Home"),
        ),
        body: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              const SizedBox(height: 30),
              RaisedButton(
                onPressed: () {},
                child: Text('จองคิวเก็บเกี่ยวข้าว',
                    style: TextStyle(fontSize: 20)),
              ),
              const SizedBox(height: 30),
              RaisedButton(
                onPressed: () {},
                child: const Text('จองคิวรถเกี่ยวนวดข้าว',
                    style: TextStyle(fontSize: 20)),
              ),
              const SizedBox(height: 30),
              RaisedButton(
                onPressed: () {},
                child: const Text('ตารางงานรถเกี่ยวนวดข้าว',
                    style: TextStyle(fontSize: 20)),
              ),
              const SizedBox(height: 30),
              RaisedButton(
                onPressed: () {},
                child: const Text('ข้อมูลรถเกี่ยวนวดข้าว',
                    style: TextStyle(fontSize: 20)),
              ),
            ],
          ),
        ));
  }
}
