import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;

import 'package:flutter/material.dart';
import 'package:my_project/Screens/Login/login_screen.dart';
import 'package:my_project/Screens/Signup/signup_screen.dart';
import 'package:my_project/Screens/Welcome/components/background.dart';
import 'package:my_project/components/rounded_button.dart';
import 'package:my_project/constants.dart';
import 'package:flutter_svg/svg.dart';
import 'package:my_project/models.dart';

class Body51 extends StatelessWidget {
  void fetching() async {
    // https://pub.dev/packages/http

    //await http.post(url, headers={ 'Content-Type': 'application/json' })
    //await http.delete(url, headers={ 'Content-Type': 'application/json' })
    //await http.get(url, headers={ 'Content-Type': 'application/json' })
    //await http.update(url, headers={ 'Content-Type': 'application/json' })
  }
  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    // This size provide us total height and width of our screen
    var fetch = () async {
      print('fetching');
      String url = 'https://jungqueue.pythonanywhere.com/api/farmer/';
      var response =
          await http.get(url, headers: {'Content-Type': 'application/json'});
      print('Response status: ${response.statusCode}');
      print('Response body: ${response.body}');
      print('jsondecode: ${json.decode(response.body)}');
      List<dynamic> result = json.decode(utf8.decode(response.bodyBytes));
      print('utf8decode: $result');
      print('---convert to list of Farmer---');

      List<Farmer> farmers =
          result.map<Farmer>((data) => Farmer.fromMap(data)).toList();

      farmers.forEach((farmer) => print(farmer.toString()));
    };
    return Background(
      child: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              "WELCOME",
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            SizedBox(height: size.height * 0.05),
            /*SvgPicture.asset(
              "assets/icons/chat.svg",
              height: size.height * 0.45,
            ),*/
            SizedBox(height: size.height * 0.05),
            RoundedButton(
              text: "เกษตรกร",
              press: () {
                fetch();
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) {
                      return LoginScreen();
                    },
                  ),
                );
              },
            ),
            RoundedButton(
              text: "เจ้าของรถ",
              color: kPrimaryLightColor,
              textColor: Colors.black,
              press: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) {
                      return LoginScreen();
                    },
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}
