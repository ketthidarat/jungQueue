import 'package:flutter/material.dart';
import 'package:my_project/Screens/Login/components/background.dart';
import 'package:my_project/Screens/Signup/signup_screen.dart';
import 'package:my_project/components/already_have_an_account_acheck.dart';
import 'package:my_project/components/rounded_button.dart';
import 'package:my_project/components/rounded_input_field.dart';
import 'package:my_project/components/rounded_password_field.dart';
import 'package:flutter_svg/svg.dart';
import 'package:http/http.dart' as http;

class Body extends StatefulWidget {
  Body({
    Key key,
  }) : super(key: key);

  @override
  _BodyState createState() => _BodyState();
}

class _BodyState extends State<Body> {
  String email = '';
  String password = '';

  void postToServer() async {
    var url = 'http://jungqueue.pythonanywhere.com/api/farmer/';
    var response =
        await http.post(url, body: {'name': 'doodle', 'color': 'blue'});
    print('Response status: ${response.statusCode}');
    print('Response body: ${response.body}');
  }

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Background(
      child: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              "LOGIN",
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            SizedBox(height: size.height * 0.03),
            SvgPicture.asset(
              "assets/icons/login.svg",
              height: size.height * 0.35,
            ),
            SizedBox(height: size.height * 0.03),
            RoundedInputField(
              hintText: "Your Email",
              onChanged: (value) {
                this.email = value;
              },
            ),
            RoundedPasswordField(
              onChanged: (value) {
                print('เปลี่ยนค่า password: ${value}');
                this.password = value;
              },
            ),
            RoundedButton(
              text: "LOGIN",
              press: () {
                print('พยายาม login: ด้วย ${this.email} ${this.password}');
                postToServer();
              },
            ),
            SizedBox(height: size.height * 0.03),
            AlreadyHaveAnAccountCheck(
              press: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) {
                      return SignUpScreen();
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
