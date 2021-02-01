import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import 'package:flutter/material.dart';
import 'package:my_project/bar.dart';
import 'package:my_project/Screens/Welcome/welcome_screen.dart';
import 'package:my_project/constants.dart';
import 'bar.dart';
import 'work.dart';
import 'bar.dart';
import 'owner.dart';

void main() {
  LicenseRegistry.addLicense(() async* {
    final license = await rootBundle.loadString('assets/fonts/OFL.txt');
    yield LicenseEntryWithLineBreaks(['assets/fonts'], license);
  });
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.green,
        fontFamily: 'Sarabun',
        backgroundColor: Colors.greenAccent[50],
      ),
      home: BarNavy(),
    );
  }
}
