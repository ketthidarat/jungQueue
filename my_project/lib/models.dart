class Farmer {
  String farmer_name;
  String address;
  String phone;
  String email;
  String username;
  String password;
  String img;

  Farmer(this.farmer_name, this.address, this.phone, this.email, this.username,
      this.password, this.img);

  factory Farmer.fromMap(Map<String, dynamic> json) {
    return Farmer(json['farmer_name'], json['address'], json['phone'],
        json['email'], json['username'], json['password'], json['img']);
  }

  String toString() {
    return '${this.farmer_name} โทรศัพท์: ${this.phone} ที่อยู่ ${this.address}';
  }

  static fromJson(data) {}
}

class Owner {
  String owner_name;
  String address;
  String phone;
  String email;
  String username;
  String password;
  String img;

  Owner(this.owner_name, this.address, this.phone, this.email, this.username,
      this.password, this.img);

  factory Owner.fromMap(Map<String, dynamic> json) {
    return Owner(json['owner_name'], json['address'], json['phone'],
        json['email'], json['username'], json['password'], json['img']);
  }

  String toString() {
    return '${this.owner_name} โทรศัพท์: ${this.phone} ที่อยู่ ${this.address}';
  }
}

class Tractor {
  String tractorName;
  TractorStatus tractor_status;

  Tractor(this.tractorName, this.tractor_status);

  factory Tractor.fromMap(Map<String, dynamic> json) {
    return Tractor(
      json['tractor'],
      // json['workId'],
      TractorStatus.fromMap(json['tractor_status']),
    );
  }

  String toString() {
    return '${this.tractorName} ${this.tractor_status}';
  }
}

class TractorStatus {
  String tractorStatus;

  TractorStatus(this.tractorStatus);

  factory TractorStatus.fromMap(Map<String, dynamic> json) {
    return TractorStatus(json['tractor_status']);
  }

  String toString() {
    return '${this.tractorStatus}';
  }
}

class RiceType {
  String rice_type;

  RiceType(this.rice_type);

  factory RiceType.fromMap(Map<String, dynamic> json) {
    return RiceType(json['rice_type']);
  }

  String toString() {
    return '${this.rice_type}';
  }
}

class WorkStatus {
  String workStatus;

  WorkStatus(this.workStatus);

  factory WorkStatus.fromMap(Map<String, dynamic> json) {
    return WorkStatus(json['work_status']);
  }

  String toString() {
    return '${this.workStatus}';
  }
}

class MoneyStatus {
  String moneyStatus;

  MoneyStatus(this.moneyStatus);

  factory MoneyStatus.fromMap(Map<String, dynamic> json) {
    return MoneyStatus(json['money_status']);
  }

  String toString() {
    return '${this.moneyStatus}';
  }
}

class Work {
  Farmer farmer_name;
  String lat;
  String lng;
  String dateStart;
  String dateEnd;
  int area;
  RiceType rice_type;
  String repairTime;
  String harverstime;
  int money;
  MoneyStatus moneyStatus;
  WorkStatus workStatus;
  Tractor tractor;
  TractorStatus tractorStatus;

  Work(
      this.farmer_name,
      this.lat,
      this.lng,
      this.dateStart,
      this.dateEnd,
      this.area,
      this.rice_type,
      this.repairTime,
      this.harverstime,
      this.money,
      this.moneyStatus,
      this.workStatus,
      this.tractor,
      this.tractorStatus);

  factory Work.fromMap(Map<String, dynamic> json) {
    return Work(
      Farmer.fromMap(json['farmer_name']),
      json['lat'],
      json['lng'],
      json['date_start'],
      json['date_end'],
      json['area'],
      // json['rice_type'],
      RiceType.fromMap(json['rice_type']),
      json['RepairTime'],
      json['Harverstime'],
      json['money'],
      MoneyStatus.fromMap(json['money_status']),
      WorkStatus.fromMap(json['work_status']),
      Tractor.fromMap(json['tractor']),
      TractorStatus.fromMap(json['tractor_status']),
      // json['money_status'],
      // json['work_status'],
      // json['tractor'],
      // json['tractor_status'],
    );
  }

  String toString() {
    return '${this.farmer_name} ตำแหน่ง: ${this.lat}  ${this.lat}';
  }
}
