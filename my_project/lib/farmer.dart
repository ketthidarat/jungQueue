import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'models.dart';
import 'models.dart';
import 'farmer_detail.dart';

class Farmer extends StatefulWidget {
  @override
  _FarmerPageState createState() {
    return new _FarmerPageState();
  }

  static fromJson(data) {}
}

class _FarmerPageState extends State<Farmer> {
  var url = "https://jungqueue.pythonanywhere.com/api/farmer/";

  List<Farmer> _farmer = <Farmer>[];

  @override
  void initState() {
    super.initState();

    fetchData();
  }

  fetchData() async {
    final Stream<Farmer> stream = await getFarmers();
    stream.listen((Farmer farmer) => setState(() => _farmer.add(farmer)));
  }

  Future<Stream<Farmer>> getFarmers() async {
    print('calling getFarmers()');
    final client = new http.Client();
    final streamedRest = await client.send(http.Request('get', Uri.parse(url)));

    return streamedRest.stream
        .transform(utf8.decoder)
        .transform(json.decoder)
        .expand((data) => (data as List))
        .map((data) => Farmer.fromJson(data));
  }

  Widget build(BuildContext context) {
    var _farmer;
    return MaterialApp(
        title: 'First Example',
        home: Scaffold(
            appBar: AppBar(
              title: Text('เกษตรกร'),
            ),
            body: _farmer.isEmpty
                ? Center(
                    child: CircularProgressIndicator(),
                  )
                : ListView(
                    children: _farmer.map(
                      (farmer) => Padding(
                        padding: const EdgeInsets.all(2.0),
                        child: InkWell(
                          onTap: () {
                            Navigator.push(
                                context,
                                MaterialPageRoute(
                                    builder: (context) => FarmerDetail(
                                          farmer: farmer,
                                        )));
                          },
                        ),
                      ),
                    ),
                  )));
  }
}
