import 'package:flutter/material.dart';
import 'bar.dart';
import 'dart:async';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:table_calendar/table_calendar.dart';
import 'calendarcontroller.dart';

class Queue extends StatefulWidget {
  @override
  _QueueState createState() => _QueueState();
}

class PatientmapPage extends StatefulWidget {
  String get title => null;

  @override
  PatientmapPageState createState() {
    return new PatientmapPageState();
  }
}

class PatientmapPageState extends State<PatientmapPage> {
  // double currentOpacity = 0;
  // Animation<double> starAnimation;
  Completer<GoogleMapController> _controller = Completer();

  // @override
  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
      debugShowCheckedModeBanner: false,
      home: new Scaffold(
          backgroundColor: Color(0xFFB3E5FC),
          appBar: AppBar(
            title: Text("Google Map"),
            actions: [
              //action button
              IconButton(
                icon: Image.asset('assets/icons/heart.png'),
                onPressed: () {},
              ),
            ],
            backgroundColor: Colors.indigo,
          ),
          body: GoogleMap(
            mapType: MapType.normal,
            initialCameraPosition: CameraPosition(
              target:
                  LatLng(15.1989675, 104.8405362), //ของจังหวัดตัวเอง104.8405362
              zoom: 16,
            ),
            onMapCreated: (GoogleMapController controller) {
              _controller.complete(controller);
            },
          )),
    );
  }
}

class _QueueState extends State<Queue> {
  int _value = 1;
  Completer<GoogleMapController> _controller = Completer();
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
        body: new Column(
          children: <Widget>[
            const SizedBox(height: 30),
            RaisedButton(
              onPressed: () {
                Navigator.push(context,
                    MaterialPageRoute(builder: (context) => PatientmapPage()));
              },
              child: Text('แผนที่', style: TextStyle(fontSize: 20)),
            ),

            new ListTile(
              // leading: const Icon(Icons.person),
              title: new TextField(
                decoration: new InputDecoration(
                  hintText: "จำนวนไร่ที่ต้องการเก็บเกี่ยว",
                ),
              ),
            ),
            new ListTile(
              // leading: const Icon(Icons.phone),
              title: new TextField(
                decoration: new InputDecoration(
                  hintText: "พันธุ์ข้าว",
                ),
              ),
            ),
            Container(
              padding: EdgeInsets.all(20.0),
              child: DropdownButton(
                  hint: Text("สภาพต้นข้าว"),
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
              // leading: const Icon(Icons.email),
              title: new TextField(
                decoration: new InputDecoration(
                  hintText: "อื่นๆ",
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
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => Calendar()))
                },
                color: Colors.red,
                child: Text(
                  'ยกเลิก',
                  style: TextStyle(color: Colors.white),
                ),
              ),
            ])
            // const Divider(
            //   height: 1.0,
            // ),
            // new ListTile(
            //   leading: const Icon(Icons.label),
            //   title: const Text('Nick'),
            //   subtitle: const Text('None'),
            // ),
            // new ListTile(
            //   leading: const Icon(Icons.today),
            //   title: const Text('Birthday'),
            //   subtitle: const Text('February 20, 1980'),
            //   trailing: const Icon(
            //     Icons.check_circle,
            //     color: Colors.green,
            //   ),
            // ),
            // new ListTile(
            //   leading: const Icon(Icons.group),
            //   title: const Text('Contact group'),
            //   subtitle: const Text('Not specified'),
            // )
          ],
        ),
      ),
    );
  }
}
