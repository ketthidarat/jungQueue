import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'models.dart';
import 'owner_detail.dart';

class OwnerPage extends StatefulWidget {
  final int ownerId;

  OwnerPage(this.ownerId);

  @override
  _OwnerPageState createState() {
    print('creating state');
    return new _OwnerPageState();
  }

  static fromJson(data) {}
}

class _OwnerPageState extends State<OwnerPage> {
  var url = "https://jungqueue.pythonanywhere.com/api/owner/1";

  // เอารายชื่อของ farmer มาทั้งหมด
  List<Owner> _owners = <Owner>[];
  // เอาข้อมูลชาวนามาคนเยว? one farmer
  // Farmer _farmer;

  @override
  void initState() {
    super.initState();
    print('fetching data');
    getOwners();
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

  void getOwners() async {
    print('calling getFarmers()');
    String url = 'https://jungqueue.pythonanywhere.com/api/owner/';
    var response =
        await http.get(url, headers: {'Content-Type': 'application/json'});
    List<dynamic> result = json.decode(utf8.decode(response.bodyBytes));
    _owners = result.map<Owner>((data) => Owner.fromMap(data)).toList();
    setState(() {});
  }

  Widget build(BuildContext context) {
    print('update FarmerPage');
    //print('${_farmers}');
    return MaterialApp(
      title: 'First Example',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Owner'),
        ),
        body: _owners.isEmpty
            ? Center(
                child: CircularProgressIndicator(),
              )
            : Column(
                children: _owners
                    .map((owner) => Card(
                        child: ListTile(
                            leading: FlutterLogo(size: 62.0),
                            title: Text(owner.username),
                            subtitle: Text(owner.address),
                            trailing: Icon(Icons.more_vert),
                            isThreeLine: true,
                            onTap: () {
                              Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                      builder: (context) => OwnerDetail(
                                            owner: owner,
                                          )));
                            })))
                    .toList(),
              ),
      ),
    );
  }
}
