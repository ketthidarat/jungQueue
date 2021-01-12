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
}
