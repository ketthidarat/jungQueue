import 'package:flutter/material.dart';
import 'package:my_project/queue.dart';
import 'package:my_project/tractor.dart';
import 'package:my_project/tractor_detail.dart';
import 'package:my_project/tractor_status.dart';
import 'calendarcontroller.dart';
import 'check_schedule.dart';
import 'farmer.dart';
import 'main.dart';
import 'package:google_fonts/google_fonts.dart';

import 'models.dart';

class HomePage extends StatelessWidget {
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
              // const SizedBox(height: 2),
              // Image.asset(
              //   'assets/images/tractor.png',
              //   width: 200,
              //   height: 100,
              // ),
              // RaisedButton(
              //   onPressed: () {
              //     Navigator.push(
              //         context,
              //         MaterialPageRoute(
              //             builder: (context) => TractorWidget(1)));
              //   },

              //   child: Text('ข้อมูลรถเกี่ยวนวดข้าว',
              //       style: TextStyle(fontSize: 20)),
              //   //child: Text('Tractor Infor', style: TextStyle(fontSize: 20)),
              // ),
              const SizedBox(height: 2),
              Image.asset(
                'assets/images/tractor.png',
                width: 200,
                height: 100,
              ),
              RaisedButton(
                onPressed: () {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => Calendar()));
                },
                //child: const Text('ตารางงานรถเกี่ยวนวดข้าว',
                child: const Text('Tractor Schedule',
                    style: TextStyle(fontSize: 20)),
              ),
              const SizedBox(height: 2),
              Image.asset(
                'assets/images/queue.png',
                width: 200,
                height: 100,
              ),
              RaisedButton(
                onPressed: () {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => Queue()));
                },
                //child: const Text('จองคิวรถเกี่ยวนวดข้าว',
                child:
                    const Text('Reservation', style: TextStyle(fontSize: 20)),
              ),
              const SizedBox(height: 20),
              Image.asset(
                'assets/images/schedule.png',
                width: 200,
                height: 100,
              ),
              RaisedButton(
                onPressed: () {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => CheckScedule()));
                },
                child:
                    //const Text('ตรวจสอบการจอง', style: TextStyle(fontSize: 20)),
                    const Text('Check schedule',
                        style: TextStyle(fontSize: 20)),
              ),
            ],
          ),
        ));
  }
}
