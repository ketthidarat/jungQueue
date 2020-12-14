import 'package:flutter/material.dart';
import 'package:table_calendar/table_calendar.dart';
import 'bar.dart';

class Queue extends StatefulWidget {
  @override
  _QueueState createState() => _QueueState();
  Widget build(BuildContext context) {
    return Scaffold(
       backgroundColor: Colors.greenAccent[50],
      appBar: AppBar(
        title: Text("Home"),
      ),
     body: Queue(),
    );
  }
}



class _QueueState extends State<Queue>
    with SingleTickerProviderStateMixin {
final _formKey = GlobalKey<FormState>();
 bool _termsChecked1 = true;
  bool _termsChecked2 = true;
  bool _termsChecked3 = true;
  bool _termsChecked4 = true;
  bool _termsChecked5 = true;
  bool _termsChecked6 = true;
  bool _termsChecked7 = true;
  bool _termsChecked8 = true;
  bool _termsChecked9 = true;
  


  int _selectedGender = 0;
  
  List<DropdownMenuItem<int>> 
  typeList = [] ,
  jaList = [],
  genderList1 = [],
  genderList2 = [],
  typecarList = [],
  priceList = []; 
  String _name1;
  String _lastname1;
  String _keyja;
  String _idme;
  String _name2;
  String _lastname2;
  String _address;
  String _amphoe;
  String _province;
  String _numbercar;

  get body => BarNavy();
  
  
  void onPressedSubmit() {
      if (_formKey.currentState.validate() ) {
        _formKey.currentState.save();

       
      
      
        Scaffold.of(context)
            .showSnackBar(SnackBar(content: Text('Form Submitted')));
      }
    }

  void loadtype() {
    
    typeList = [];
    new Text('สถานะของรถ');
    typeList.add(new DropdownMenuItem(
      
      child: new Text('สถานะของรถ'),
      value: 0,
    ));
    typeList.add(new DropdownMenuItem(
      child: new Text('กำลังทำงาน'),
      value: 1,
    ));
    typeList.add(new DropdownMenuItem(
      child: new Text('อยู่ระหว่างการซ่อม'),
      value: 2,
    ));
    typeList.add(new DropdownMenuItem(
      child: new Text('ไม่ทำงาน'),
      value: 3,
    ));
  }
   void loadja() {
    jaList = [];
    jaList.add(new DropdownMenuItem(
      child: new Text('เดือน'),
      value: 0,
    ));
    jaList.add(new DropdownMenuItem(
      child: new Text('ผิวขาวซีด'),
      value: 1,
    ));
    jaList.add(new DropdownMenuItem(
      child: new Text('จ่าสิบตำรวจ'),
      value: 2,
    ));
      jaList.add(new DropdownMenuItem(
      child: new Text('สิบตำรวจตรี'),
      value: 4,
    ));
      jaList.add(new DropdownMenuItem(
      child: new Text('สิบตำรวจเอก'),
      value: 5,
    ));
      jaList.add(new DropdownMenuItem(
      child: new Text('สิบตำรวจโท'),
      value: 6,
    ));
  }
   void loadgender1() {
    genderList1 = [];
    genderList1.add(new DropdownMenuItem(
      child: new Text('ปี'),
      value: 0,
    ));
    genderList1.add(new DropdownMenuItem(
      child: new Text('ชาย'),
      value: 1,
    ));
    genderList1.add(new DropdownMenuItem(
      child: new Text('หญิง'),
      value: 2,
    ));
    genderList1.add(new DropdownMenuItem(
      child: new Text('อิ่นๆ'),
      value: 3,
    ));
  }
   void loadgender2() {
    genderList2 = [];
    genderList2.add(new DropdownMenuItem(
      child: new Text('เพศ'),
      value: 0,
    ));
    genderList2.add(new DropdownMenuItem(
      child: new Text('ชาย'),
      value: 1,
    ));
    genderList2.add(new DropdownMenuItem(
      child: new Text('หญิง'),
      value: 2,
    ));
    genderList2.add(new DropdownMenuItem(
      child: new Text('อิ่นๆ'),
      value: 3,
    ));
  }
   void loadtypecar() {
    typecarList = [];
    typecarList.add(new DropdownMenuItem(
      child: new Text('ประเภทรถ'),
      value: 0,
    ));
    typecarList.add(new DropdownMenuItem(
      child: new Text('รถจักรยานยนต์'),
      value: 1,
    ));
    typecarList.add(new DropdownMenuItem(
      child: new Text('รถยนต์'),
      value: 2,
    ));
    typecarList.add(new DropdownMenuItem(
      child: new Text('รถบรรทุก'),
      value: 3,
    ));
  }
    void loadprice() {
    priceList = [];
    priceList.add(new DropdownMenuItem(
      child: new Text('ยังไม่ชำระเงิน'),
      value: 0,
    ));
    priceList.add(new DropdownMenuItem(
      child: new Text('ชำระเงินเรียบร้อย'),
      value: 1,
    ));
    // priceList.add(new DropdownMenuItem(
    //   child: new Text('ชำระค่าปรบเรียบร้อย'),
    //   value: 2,
    // ));
  }
  
  
   @override
  Widget build(BuildContext context) {
      // final halfMediaWidth = MediaQuery.of(context).size.width / 2.0;
    loadtype();
    loadja();
    loadgender1();
    loadgender2();
    loadtypecar();
    loadprice();
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Form(
          key: _formKey,
          child: new ListView(
            children: getFormWidget(),
          )),
    );
  }
  
  
  List<Widget> getFormWidget() {
    List<Widget> formWidget = new List();



  
     /*formWidget.add(new DropdownButton(
      hint: new Text('Select Gender'),
      items: jaList,
      value: _selectedGender,
      onChanged: (value) {
        setState(() {
          _selectedGender = value;
        });
      },
      isExpanded: true,
    ));


  formWidget.add(new DropdownButton(
      hint: new Text('Select Gender'),
      items: genderList1,
      value: _selectedGender,
      onChanged: (value) {
        setState(() {
          _selectedGender = value;
        });
      },
      isExpanded: true,
    ));*/

    formWidget.add(new DropdownButton(
      hint: new Text('Select Gender'),
      items: typeList,
      value: _selectedGender,
      onChanged: (value) {
        setState(() {
          _selectedGender = value;
        });
      },
      isExpanded: true,
    ));
  formWidget.add(new TextFormField(
      decoration: InputDecoration(hintText: 'เวลาที่ใช้ในการเก็บเกี่ยว', labelText: 'เวลาที่ใช้ในการเก็บเกี่ยว'),
      keyboardType: TextInputType.text,
      validator: (value) {
        if (value.isEmpty) return 'เวลาที่ใช้ในการเก็บเกี่ยว';
      },
      onSaved: (value) {
        setState(() {
          _name1 = value;
        });
      },
    ));
    
  formWidget.add(new TextFormField(
      decoration: InputDecoration(hintText: 'เวลาที่ใช้ในการซ่อมรถ', labelText: 'เวลาที่ใช้ในการซ่อมรถ'),
      keyboardType: TextInputType.text,
      validator: (value) {
        if (value.isEmpty) return 'เวลาที่ใช้ในการซ่อมรถ';
      },
      onSaved: (value) {
        setState(() {
          _lastname1 = value;
        });
      },
    ));
    
    /*formWidget.add(new TextFormField(
      decoration: InputDecoration(hintText: 'Email', labelText: 'Email'),
      keyboardType: TextInputType.text,
      validator: (value) {
        if (value.isEmpty) return 'Email';
      },
      onSaved: (value) {
        setState(() {
          _keyja = value;
        });
      },
    ));*/
     /*  formWidget.add(new TextFormField(
      decoration: InputDecoration(hintText: 'ที่อยู่', labelText: 'ที่อยู่'),
      keyboardType: TextInputType.text,
      validator: (value) {
        if (value.isEmpty) return 'ที่อยู่';
      },
      onSaved: (value) {
        setState(() {
          _idme = value;
        });
      },
    ));
    formWidget.add(new TextFormField(
      decoration: InputDecoration(hintText: 'รหัสไปรษณีย์', labelText: 'รหัสไปรษณีย์'),
      keyboardType: TextInputType.text,
      validator: (value) {
        if (value.isEmpty) return 'รหัสไปรษณีย์';
      },
      onSaved: (value) {
        setState(() {
          _idme = value;
        });
      },
    ));*/

 /* formWidget.add(new DropdownButton(
      hint: new Text('Select Gender'),
      items: genderList2,
      value: _selectedGender,
      onChanged: (value) {
        setState(() {
          _selectedGender = value;
        });
      },
      isExpanded: true,
    ));
  
    
    formWidget.add(CheckboxListTile(
      value: _termsChecked1,
      onChanged: (value) {
        setState(() {
          _termsChecked1 = value;
        });
      },
      // subtitle: !_termsChecked
      //     ? Text(
      //         'Required',
      //         style: TextStyle(color: Colors.red, fontSize: 12.0),
      //       )
      //     : null,
      
    ));*/
     /*formWidget.add(CheckboxListTile(
      value: _termsChecked2,
      onChanged: (value) {
        setState(() {
          
          _termsChecked2 = value;
        });
      },
      title: new Text(
        'ชาย',
      ),
      controlAffinity: ListTileControlAffinity.leading,
    ));
     formWidget.add(CheckboxListTile(
      value: _termsChecked3,
      onChanged: (value) {
        setState(() {
          _termsChecked3 = value;
        });
      },
      title: new Text(
        'หญิง',
      ),
      controlAffinity: ListTileControlAffinity.leading,
    ));*/
   
    /*formWidget.add(new TextFormField(
      decoration: InputDecoration(hintText: 'วัน/เดือน/ปีเกิด', labelText: 'วัน/เดือน/ปีเกิด'),
      keyboardType: TextInputType.text,
      validator: (value) {
        if (value.isEmpty) return 'วัน/เดือน/ปีเกิด';
      },
      onSaved: (value) {
        setState(() {
          _name1 = value;
        });
      },
    ));
    formWidget.add(new DropdownButton(
      hint: new Text('Select Gender'),
      items: typeList,
      value: _selectedGender,
      onChanged: (value) {
        setState(() {
          _selectedGender = value;
        });
      },
      isExpanded: true,
    ));*/


   /* formWidget.add(new DropdownButton(
      hint: new Text('Select Gender'),
      items: jaList,
      value: _selectedGender,
      onChanged: (value) {
        setState(() {
          _selectedGender = value;
        });
      },
      isExpanded: true,
    ));
     formWidget.add(new DropdownButton(
      hint: new Text('Select Gender'),
      items: genderList1,
      value: _selectedGender,
      onChanged: (value) {
        setState(() {
          _selectedGender = value;
        });
      },
      isExpanded: true,
    ));*/
   /* formWidget.add(new TextFormField(
      decoration: InputDecoration(hintText: 'CVV', labelText: 'CVV'),
      keyboardType: TextInputType.text,
      validator: (value) {
        if (value.isEmpty) return 'CVV';
      },
      onSaved: (value) {
        setState(() {
          _name1 = value;
        });
      },
    ));*/
    //https://lookinggreat.pythonanywhere.com/media/${member.cover.name}

    formWidget.add(new RaisedButton(
        color: Colors.blue,
        textColor: Colors.white,
        child: new Text('Submit'),
        onPressed: onPressedSubmit));
    return formWidget;
  }
  
}
