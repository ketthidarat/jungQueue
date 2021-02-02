import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:my_project/tractor_showDetail.dart';
import 'models.dart';
import 'work_detail.dart';

class TractorWidget extends StatefulWidget {
  final int tractorId;

  TractorWidget(this.tractorId);

  @override
  _TractorWidgetState createState() {
    print('creating state');
    return new _TractorWidgetState();
  }

  static fromJson(data) {}
}

class _TractorWidgetState extends State<TractorWidget> {
  var url = "https://jungqueue.pythonanywhere.com/api/tractor/1";

  // เอารายชื่อของ farmer มาทั้งหมด
  List<Tractor> _tractors = <Tractor>[];
  // เอาข้อมูลชาวนามาคนเยว? one farmer
  // Farmer _farmer;

  @override
  void initState() {
    super.initState();
    print('fetching data');
    getTractorWidgets();
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

  void getTractorWidgets() async {
    print('calling getOwners()');
    String url = 'https://jungqueue.pythonanywhere.com/api/tractor/';
    var response =
        await http.get(url, headers: {'Content-Type': 'application/json'});
    List<dynamic> result = json.decode(utf8.decode(response.bodyBytes));
    _tractors = result.map<Tractor>((data) => Tractor.fromMap(data)).toList();
    setState(() {});
  }

  Widget build(BuildContext context) {
    print('update TractorPage');
    //print('${_farmers}');
    return MaterialApp(
      title: 'First Example',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Tractor'),
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
                            title: Text(tractor.tractor),
                            subtitle: Text(tractor.tractor_status),
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
      ),
    );
  }
}
