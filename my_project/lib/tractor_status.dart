import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'models.dart';
import 'farmer_detail.dart';

class TractorStatusPage extends StatefulWidget {
  final int tractorId;

  TractorStatusPage(this.tractorId);

  @override
  _TractorStatusPageState createState() {
    print('creating state');
    return new _TractorStatusPageState();
  }

  static fromJson(data) {}
}

class _TractorStatusPageState extends State<TractorStatusPage> {
  var url = "https://jungqueue.pythonanywhere.com/api/tractor_status/1";

  // เอารายชื่อของ farmer มาทั้งหมด
  List<Farmer> _farmers = <Farmer>[];
  // เอาข้อมูลชาวนามาคนเยว? one farmer
  // Farmer _farmer;

  @override
  void initState() {
    super.initState();
    print('fetching data');
    getFarmers();
  }

  /*
  void getFarmerInfo() async {
    print('calling getFarmerInfo(${widget.farmerId})');
    var response =
        await http.get(url, headers: {'Content-Type': 'application/json'});
    dynamic result = json.decode(utf8.decode(response.bodyBytes));
    print('stream is done.');
    print('${result}');
    Farmer farmer1 = Farmer.fromMap(result);
    print('${farmer1}');
    _farmer = farmer1;
    setState(() {});
  }
  fetchData() async {
    final Stream<Farmer> stream = await getFarmers();
    stream.listen((Farmer farmer) => setState(() => _farmer.add(farmer)));
  }
  */

  void getFarmers() async {
    print('calling getFarmers()');
    String url = 'https://jungqueue.pythonanywhere.com/api/tractor_status/';
    var response =
        await http.get(url, headers: {'Content-Type': 'application/json'});
    List<dynamic> result = json.decode(utf8.decode(response.bodyBytes));
    _farmers = result.map<Farmer>((data) => Farmer.fromMap(data)).toList();
    setState(() {});
  }

  Widget build(BuildContext context) {
    print('update FarmerPage');
    //print('${_farmers}');
    return MaterialApp(
      title: 'First Example',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Farmer'),
        ),
        body: _farmers.isEmpty
            ? Center(
                child: CircularProgressIndicator(),
              )
            : Column(
                children: _farmers
                    .map((farmer) => Card(
                        child: ListTile(
                            leading: FlutterLogo(size: 62.0),
                            title: Text(farmer.username),
                            subtitle: Text(farmer.address),
                            trailing: Icon(Icons.more_vert),
                            isThreeLine: true,
                            onTap: () {
                              Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                      builder: (context) => FarmerDetail(
                                            farmer: farmer,
                                          )));
                            })))
                    .toList(),
              ),
      ),
    );
  }
}
