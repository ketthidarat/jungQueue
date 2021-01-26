import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'models.dart';
import 'work_detail.dart';

class WorkWidget extends StatefulWidget {
  static final route = 'Work';

  @override
  _WorkPageState createState() {
    return new _WorkPageState();
  }

  // ????
  // static fromJson(data) {}
}

class _WorkPageState extends State<WorkWidget> {
  var url = "https://jungqueue.pythonanywhere.com/api/work/";

  List<Work> _work = <Work>[];

  get work => null;

  @override
  void initState() {
    super.initState();
    print('what the');
    print(_work);
    fetchData();
  }

  fetchData() async {
    final Stream<Work> stream = (await getWorks()) as Stream<Work>;
    stream.listen((Work work) => setState(() => _work.add(work)));
  }

  Future<Stream<Farmer>> getWorks() async {
    print('calling getFarmers()');
    final client = new http.Client();
    final streamedRest = await client.send(http.Request('get', Uri.parse(url)));

    return streamedRest.stream
        .transform(utf8.decoder)
        .transform(json.decoder)
        .expand((data) => (data as List))
        .map((data) => Farmer.fromMap(data));
  }

  Widget build(BuildContext context) {
    // var _farmer;
    return MaterialApp(
        title: 'First Example',
        home: Scaffold(
            appBar: AppBar(
              title: Text('เกษตรกร'),
            ),
            body: _work.isEmpty
                ? Center(
                    child: CircularProgressIndicator(),
                  )
                : ListView(
                    children: _work
                        .map(
                          (work) => Padding(
                            padding: const EdgeInsets.all(2.0),
                            child: InkWell(
                              onTap: () {
                                Navigator.push(
                                    context,
                                    MaterialPageRoute(
                                        builder: (context) => WorkDetail(
                                              work: work,
                                            )));
                              },
                            ),
                          ),
                        )
                        .toList(),
                  )));
  }
}
