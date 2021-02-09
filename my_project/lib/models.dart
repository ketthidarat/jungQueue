class Farmer {
  String farmerName;
  String address;
  String phone;
  String email;
  String username;
  String password;

  Farmer(this.farmerName, this.address, this.phone, this.email, this.username,
      this.password);

  factory Farmer.fromMap(Map<String, dynamic> json) {
    return Farmer(json['farmer_name'], json['address'], json['phone'],
        json['email'], json['username'], json['password']);
  }

  String toString() {
    return '${this.farmerName} โทรศัพท์: ${this.phone} ที่อยู่ ${this.address}';
  }

  static fromJson(data) {}
}

class Owner {
  String ownerName;
  String address;
  String phone;
  String email;
  String username;
  String password;

  Owner(this.ownerName, this.address, this.phone, this.email, this.username,
      this.password);

  factory Owner.fromMap(Map<String, dynamic> json) {
    return Owner(json['owner_name'], json['address'], json['phone'],
        json['email'], json['username'], json['password']);
  }

  String toString() {
    return '${this.ownerName} โทรศัพท์: ${this.phone} ที่อยู่ ${this.address}';
  }
}

class Tractor {
  String tractorName;
  int workId;
  String tractor_status;

  Tractor(this.tractorName, this.workId, this.tractor_status);

  factory Tractor.fromMap(Map<String, dynamic> json) {
    return Tractor(json['tractor'], json['workId'], json['tractor_status']);
  }

  String toString() {
    return '${this.tractorName} ${this.workId} ${this.tractor_status}';
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
  String riceType;

  RiceType(this.riceType);

  factory RiceType.fromMap(Map<String, dynamic> json) {
    return RiceType(json['rice_type']);
  }

  String toString() {
    return '${this.riceType}';
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
  String farmerId;
  String lat;
  String lng;
  String dateStart;
  String dateEnd;
  int area;
  RiceType riceType;
  String repairTime;
  String harverstime;
  int money;
  MoneyStatus moneyStatus;
  WorkStatus workStatus;
  Tractor tractor;
  TractorStatus tractorStatus;
  Farmer farmerName;
  Work(
      this.farmerId,
      this.lat,
      this.lng,
      this.dateStart,
      this.dateEnd,
      this.area,
      this.riceType,
      this.repairTime,
      this.harverstime,
      this.money,
      this.moneyStatus,
      this.workStatus,
      this.tractor,
      this.tractorStatus);

  factory Work.fromMap(Map<String, dynamic> json) {
    return Work(
      json['farmer_name'],
      json['lat'],
      json['lng'],
      json['date_start'],
      json['date_end'],
      json['area'],
      json['rice_type'],
      json['RepairTime'],
      json['Harverstime'],
      json['money'],
      json['money_status'],
      json['work_status'],
      json['tractor'],
      json['tractor_status'],
      Farmer.fromMap(json['farmer_name']),
      RiceType.fromMap(json['rice_type']),
      Tractor.fromMap(json['tractor']),
      TractorStatus.fromMap(json['tractor_status']),
      MoneyStatus.fromMap(json['money_status']),
      WorkStatus.fromMap(json['work_status']),
    );
  }

  String toString() {
    return '${this.farmerName} ตำแหน่ง: ${this.lat}  ${this.lat}';
  }
}
