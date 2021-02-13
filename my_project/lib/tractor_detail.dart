import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:my_project/tractor_showDetail.dart';
import 'add_tractor.dart';
import 'models.dart';

class TractorDetail extends StatefulWidget {
  final int tractorId;

  TractorDetail(this.tractorId);

  @override
  _TractorDetail createState() {
    print('creating state');
    return new _TractorDetail();
  }

  static fromJson(data) {}
}

class _TractorDetail extends State<TractorDetail> {
  var url = "https://jungqueue.pythonanywhere.com/api/tractor/1";

  // เอารายชื่อของ farmer มาทั้งหมด
  List<Tractor> _tractors = <Tractor>[];
  // เอาข้อมูลชาวนามาคนเยว? one farmer
  // Farmer _farmer;

  @override
  void initState() {
    super.initState();
    print('fetching data');
    getTractorDetails();
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

  void getTractorDetails() async {
    print('calling getWorkWidget()');
    String url = 'https://jungqueue.pythonanywhere.com/api/tractor/';
    var response =
        await http.get(url, headers: {'Content-Type': 'application/json'});
    List<dynamic> result = json.decode(utf8.decode(response.bodyBytes));
    _tractors = result.map<Tractor>((data) => Tractor.fromMap(data)).toList();
    setState(() {});
  }

  Widget build(BuildContext context) {
    print('update WorkWidget');
    //print('${_farmers}');
    return MaterialApp(
      title: 'First Example',
      theme: ThemeData(
        primarySwatch: Colors.green,
        backgroundColor: Colors.greenAccent[50],
      ),
      home: Scaffold(
        appBar: AppBar(
          title: Text('ข้อมูลรถเกี่ยวนวดข้าว'),
        ),
        body: _tractors.isEmpty
            ? Center(
                child: CircularProgressIndicator(),
              )
            : Column(
                children: _tractors
                    .map((tractor) => Card(
                        child: ListTile(
                            leading: FlutterLogo(size: 62.0),
                            title: Text(tractor.tractorName),
                            subtitle: Text("Tractor"),
                            trailing: Icon(Icons.more_vert),
                            isThreeLine: true,
                            onTap: () {
                              Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                      builder: (context) => TractorShowDetail(
                                            tractor: tractor,
                                          )));
                            })))
                    .toList(),
              ),
        floatingActionButton: FloatingActionButton(
          child: Icon(Icons.add),
          onPressed: () {
            Navigator.push(
                context, MaterialPageRoute(builder: (context) => AddTractor()));
          },
        ),
      ),
    );
  }
}
