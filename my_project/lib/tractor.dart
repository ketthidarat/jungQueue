import 'package:flutter/material.dart';

import 'calendarcontroller.dart';

class TractorPage extends StatefulWidget {
  @override
  _TractorPageState createState() => _TractorPageState();
}

class _TractorPageState extends State<TractorPage> {
  int _value = 1;
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'รายละเอียดการจอง',
        theme: ThemeData(
          primarySwatch: Colors.green,
          backgroundColor: Colors.greenAccent[50],
        ),
        home: Scaffold(
          appBar: new AppBar(
            title: Text('รายละเอียดการจอง'),
            // Here we take the value from the MyHomePage object that was created by
            // the App.build method, and use it to set our appbar title.
            actions: <Widget>[
              // new IconButton(icon: const Icon(Icons.save), onPressed: () {})
            ],
          ),
          body: new Column(children: <Widget>[
            // new ListTile(
            //   // leading: const Icon(Icons.person),
            //   title: new TextField(
            //     decoration: new InputDecoration(
            //       hintText: "จำนวนไร่ที่ต้องการเก็บเกี่ยว",
            //     ),
            //   ),
            // ),
            // new ListTile(
            //   // leading: const Icon(Icons.phone),
            //   title: new TextField(
            //     decoration: new InputDecoration(
            //       hintText: "พันธุ์ข้าว",
            //     ),
            //   ),
            // ),
            Container(
              padding: EdgeInsets.all(20.0),
              child: DropdownButton(
                  hint: Text("สถานะการทำงานของรถเกี่ยวนวดข้าว"),
                  value: _value,
                  items: [
                    DropdownMenuItem(
                      child: Text("กำลังทำงาน"),
                      value: 1,
                    ),
                    DropdownMenuItem(
                      child: Text("กำลังซ่อม"),
                      value: 2,
                    ),
                    // DropdownMenuItem(child: Text("ล้ม"), value: 3),
                    // DropdownMenuItem(child: Text("Fourth Item"), value: 4)
                  ],
                  onChanged: (value) {
                    setState(() {
                      _value = value;
                    });
                  }),
            ),
            const SizedBox(height: 20),
            RaisedButton(
              onPressed: () => {
                Navigator.push(context,
                    MaterialPageRoute(builder: (context) => Calendar()))
              },
              color: Colors.blueAccent[100],
              child: Text(
                'วันที่ต้องการเก็บเกี่ยว',
                style: TextStyle(color: Colors.white),
              ),
            ),
            new ListTile(
              // leading: const Icon(Icons.person),
              title: new TextField(
                decoration: new InputDecoration(
                  hintText: "เวลาที่ใช้ในการเก็บเกี่ยว",
                ),
              ),
            ),
            new ListTile(
              // leading: const Icon(Icons.phone),
              title: new TextField(
                decoration: new InputDecoration(
                  hintText: "เวลาที่ใช้ในการซ่อมรถ",
                ),
              ),
            ),
            ButtonBar(alignment: MainAxisAlignment.center, children: <Widget>[
              RaisedButton(
                onPressed: () => {},
                color: Colors.green,
                child: Text(
                  'ยืนยัน',
                  style: TextStyle(color: Colors.white),
                ),
              ),
              RaisedButton(
                onPressed: () => {
                  // Navigator.push(context,
                  //     MaterialPageRoute(builder: (context) => Calendar()))
                },
                color: Colors.red,
                child: Text(
                  'ยกเลิก',
                  style: TextStyle(color: Colors.white),
                ),
              ),
            ]),
          ]),
        ));
  }
}
