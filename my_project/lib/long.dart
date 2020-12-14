import 'dart:async';

import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

class PatientmapPage extends StatefulWidget {
  String get title => null;

  @override
  PatientmapPageState createState() {
    return new PatientmapPageState();
  }
}

class PatientmapPageState extends State<PatientmapPage>  {
  // double currentOpacity = 0;
  // Animation<double> starAnimation;
Completer<GoogleMapController> _controller = Completer();
  // @override
  @override
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
         onPressed: () { },
       ),
     ],
         backgroundColor: Colors.indigo,
       ),
      body: GoogleMap(
        mapType: MapType.normal,
        initialCameraPosition: CameraPosition(
          target: LatLng(15.1989675, 104.8405362),//ของจังหวัดตัวเอง104.8405362
          zoom: 16,
        ),
        onMapCreated: (GoogleMapController controller) {
          _controller.complete(controller);
        },
      )
    ),
     );
  }
}