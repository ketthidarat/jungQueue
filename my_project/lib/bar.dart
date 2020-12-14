//import 'package:bottom_navy_bar/bottom_navy_bar.dart';
import 'package:flutter/material.dart';
import 'home.dart';
import 'queue.dart';
import 'detail01.dart';
import 'kubota.dart';



class BarNavy extends StatefulWidget {
  @override
  _BarNavyState createState() => _BarNavyState();
}
class _BarNavyState extends State<BarNavy> {

  int _selectedIndex = 0;
  final List<Widget> _children = 
  [
    HomePage(),
    Queue(),
    DetailPage(),
    KubotaPage()


  ];
  PageController _pageController;
  void onTappedBar(int index){
    setState(() {
      _selectedIndex = index;
    });
  }
  @override
  void initState() {
    super.initState();
    _pageController = PageController();
  }

  @override
  void dispose() {
    _pageController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _children[_selectedIndex],
      bottomNavigationBar: BottomNavigationBar(
        backgroundColor: Colors.greenAccent[50],
        type: BottomNavigationBarType.fixed,
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.lightGreenAccent[50],
        unselectedItemColor: Colors.blueGrey,
        onTap: onTappedBar,
        items: const <BottomNavigationBarItem>[
         BottomNavigationBarItem(
            // ignore: deprecated_member_use
            title: Text('Home'),
            icon: Icon(Icons.home)
          ),
          BottomNavigationBarItem(
            // ignore: deprecated_member_use
            title: Text('Coach'),
            icon: Icon(Icons.star)
          ),
          BottomNavigationBarItem(
            // ignore: deprecated_member_use
            title: Text('Store'),
            icon: Icon(Icons.pets),
          ),
          BottomNavigationBarItem(
            // ignore: deprecated_member_use
            title: Text('Me'),
            icon: Icon(Icons.face),
          ),
        ],
      ),
    );
  }
}