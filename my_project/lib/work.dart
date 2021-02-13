import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'models.dart';
import 'work_detail.dart';

class WorkWidget extends StatefulWidget {
  final int workId;

  WorkWidget(this.workId);

  @override
  _WorkWidgetState createState() {
    print('creating state');
    return new _WorkWidgetState();
  }

  static fromJson(data) {}
}

class _WorkWidgetState extends State<WorkWidget> {
  var url = "https://jungqueue.pythonanywhere.com/api/work/1";

  // เอารายชื่อของ farmer มาทั้งหมด
  List<Work> _works = <Work>[];

  // เอาข้อมูลชาวนามาคนเยว? one farmer
  // Farmer _farmer;

  @override
  void initState() {
    super.initState();
    print('fetching data');
    getWorkWidgets();
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

  void getWorkWidgets() async {
    print('calling getWorkWidget()');
    String url = 'https://jungqueue.pythonanywhere.com/api/work/';
    var response =
        await http.get(url, headers: {'Content-Type': 'application/json'});
    List<dynamic> result = json.decode(utf8.decode(response.bodyBytes));
    _works = result.map<Work>((data) => Work.fromMap(data)).toList();
    setState(() {});
  }

  // void getFamers() async {
  //   print('calling getWorkWidget()');
  //   String url1 = 'https://jungqueue.pythonanywhere.com/api/farmer/';
  //   var response =
  //       await http.get(url1, headers: {'Content-Type': 'application/json'});
  //   List<dynamic> result = json.decode(utf8.decode(response.bodyBytes));
  //   _farmers = result.map<Farmer>((data) => Farmer.fromMap(data)).toList();
  //   setState(() {});
  // }

  Widget build(BuildContext context) {
    print('update WorkWidget');
    //print('${_farmers}');
    return MaterialApp(
      title: 'First Example',
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.green,
          title: Text('รายละเอียดการของเกษตรกร'),
        ),
        body: _works.isEmpty
            ? Center(
                child: CircularProgressIndicator(),
              )
            : Column(
                children: _works
                    .map((work) => Card(
                        child: ListTile(
                            leading: FlutterLogo(size: 62.0),
                            title: Text("ชื่อ ${work.farmer_name} "),
                            subtitle: Text(
                                "จำนวนไร่ที่ต้องการเก็บเกี่ยว ${work.area} "),
                            trailing: Icon(Icons.more_vert),
                            isThreeLine: true,
                            onTap: () {
                              Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                      builder: (context) => WorkDetail(
                                            work: work,
                                            // farmer: farmer,
                                          )));
                            })))
                    .toList(),
              ),
      ),
    );
  }
}
