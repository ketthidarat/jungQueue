import 'package:flutter/material.dart';
import 'package:my_project/tractor_detail.dart';
import 'package:my_project/work.dart';
import 'calendarcontroller.dart';

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
              const SizedBox(height: 2),
              Image.asset(
                'assets/images/queue.png',
                width: 200,
                height: 100,
              ),
              RaisedButton(
                onPressed: () {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => WorkWidget(1)));
                },
                child: Text('จองคิวเก็บเกี่ยวข้าว',
                    style: TextStyle(fontSize: 20)),
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
                      MaterialPageRoute(builder: (context) => Calendar()));
                },
                child: const Text('ตารางงานรถเกี่ยวนวดข้าว',
                    style: TextStyle(fontSize: 20)),
              ),
              // const SizedBox(height: 20),
              // RaisedButton(
              //   onPressed: () {},
              //   child: const Text('ตารางงานรถเกี่ยวนวดข้าว',
              //       style: TextStyle(fontSize: 20)),
              // ),
              const SizedBox(height: 2),
              Image.asset(
                'assets/images/schedule.png',
                width: 200,
                height: 100,
              ),
              RaisedButton(
                onPressed: () {
                  Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => TractorDetail(1)));
                },
                child: const Text('ข้อมูลรถเกี่ยวนวดข้าว',
                    style: TextStyle(fontSize: 20)),
              ),
            ],
          ),
        ));
  }
}
