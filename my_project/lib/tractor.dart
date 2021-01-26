import 'package:flutter/material.dart';

class Tractor extends StatefulWidget {
  @override
  _TractorState createState() => _TractorState();
}

class _TractorState extends State<Tractor> {
  int _value = 1;
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'First Example',
      theme: ThemeData(
        primarySwatch: Colors.green,
        backgroundColor: Colors.greenAccent[50],
      ),
      home: Scaffold(
        appBar: AppBar(
          title: Text('แจ้งข้อมูลรถเกี่ยวนวดข้าว'),
        ),
        body: Container(
          padding: EdgeInsets.all(20.0),
          child: DropdownButton(
              hint: Text("สถานะรถเกี่ยวนวดข้าว"),
              value: _value,
              items: [
                DropdownMenuItem(
                  child: Text("ตั้งตรง"),
                  value: 1,
                ),
                DropdownMenuItem(
                  child: Text("ราบกับพื้น"),
                  value: 2,
                ),
                DropdownMenuItem(child: Text("ล้ม"), value: 3),
                // DropdownMenuItem(child: Text("Fourth Item"), value: 4)
              ],
              onChanged: (value) {
                setState(() {
                  _value = value;
                });
              }),
        ),
      ),
    );
  }
}
