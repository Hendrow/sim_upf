from datetime import datetime
from aplikasi import db


class Alat(db.Model):
    __tablename__ = 'alat'

    id = db.Column(db.Integer, primary_key=True)
    nm_alat = db.Column(db.String(100), nullable=False)
    merk = db.Column(db.String(30), nullable=False)
    tipe = db.Column(db.String(30), nullable=False)
    no_seri = db.Column(db.String(25), nullable=False, unique=True)
    aksesoris = db.Column(db.String(100))
    th_pengadaan = db.Column(db.Integer)
    ket = db.Column(db.String(15))
    kalibrasi = db.relationship('Logkalibrasi', backref='kalibrasi', lazy=True)
    log_alat = db.relationship('Logalat', backref='logalat', lazy=True)

    def __init__(self, nm_alat, merk, tipe, no_seri, aksesoris, th_pengadaan, ket):
        self.nm_alat = nm_alat
        self.merk = merk
        self.tipe = tipe
        self.no_seri = no_seri
        self.aksesoris = aksesoris
        self.th_pengadaan = th_pengadaan
        self.ket = ket

    def __repr__(self):
        return "Nama alat : {}".format(self.nmAlat)


class Logkalibrasi(db.Model):
    __tablename__ = 'logkalibrasi'

    id = db.Column(db.Integer, primary_key=True)
    tempat_kalibrasi = db.Column(db.String(55), nullable = False)
    tgl_kalibrasi = db.Column(db.DateTime)
    hasil = db.Column(db.String(25))
    alat_id = db.Column(db.Integer, db.ForeignKey('alat.id'))

    def __init__(self, tempat_kalibrasi, tgl_kalibrasi, hasil):
        self.tempat_kalibrasi = tempat_kalibrasi
        self.tgl_kalibrasi = tgl_kalibrasi
        self.hasil = hasil

    def __repr__(self):
        return "Tempat : {}, Tanggal : {}".format(self.tempatKalibrasi, self.tglKalibrasi)


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable= False)
    email = db.Column(db.String(50), unique=True)
    nm_lengkap = db.Column(db.String(100), nullable=False)
    gambar = db.Column(db.String(100))

    def __init__(self, username, password, email, nm_lengkap, gambar):
        self.username = username
        self.password = password
        self.email = email
        self.nm_lengkap = nm_lengkap
        self.gambar = gambar

    def __repr__(self):
        return f"Add Username : {self.username}"

class Loguser(db.Model):
    __tablename__ = 'loguser'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    aksi = db.Column(db.String(25), nullable=False)
    tanggal = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, username, aksi):
        self.username = username
        self.aksi = aksi

    def __repr__(self):
        return f"aksi : {self.aksi}"

class Fasyankes(db.Model):
    __tablename__ = 'fasyankes'

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    alamat = db.Column(db.String(125), nullable=False)
    kota = db.Column(db.String(25), nullable=False)
    provinsi = db.Column(db.String(25))
    email = db.Column(db.String(30))
    telepon = db.Column(db.String(45))
    fax = db.Column(db.String(30))

    def __init__(self, nama, status, alamat, kota, provinsi, email, telepon, fax):
        self.nama = nama
        self.status = status
        self.alamat = alamat
        self.kota = kota
        self.provinsi = provinsi
        self.email = email
        self.telepon = telepon
        self.fax = fax

    def __repr__(self):
        return f"{self.nama}"


class Pinjam(db.Model):
    __tablename__ = 'pinjam'
    id = db.Column(db.Integer, primary_key=True)
    peminjam_alat = db.Column(db.String(25), nullable=False)
    petugas_catat = db.Column(db.String(25), nullable=False)
    tanggal = db.Column(db.DateTime, nullable=False)
    kordinator_tim = db.Column(db.String(25))
    status = db.Column(db.String(25), nullable=False)
    fasyankes = db.Column(db.String(100), nullable=False)
    alat_pinjam = db.relationship('Daftarpinjam', backref='pinjam', lazy=True)

    def __init__(self, peminjam_alat, petugas_catat, tanggal, kordinator_tim, status, fasyankes):
        self.peminjam_alat = peminjam_alat
        self.petugas_catat = petugas_catat
        self.tanggal = tanggal
        self.kordinator_tim = kordinator_tim
        self.status = status
        self. fasyankes = fasyankes

    def __repr__(self):
        return f"id Pinjam : {self.id}"


class Daftarpinjam(db.Model):
    __tablename__ = 'daftarpinjam'

    id = db.Column(db.Integer, primary_key=True)
    aksesoris = db.Column(db.String(50), nullable=False)
    ket = db.Column(db.String(15), nullable=False)
    id_pinjam = db.Column(db.Integer, db.ForeignKey('pinjam.id'), nullable=False)
    id_alat = db.Column(db.Integer, db.ForeignKey('alat.id'), nullable=False)

    def __init__(self, aksesoris, ket):
        self.aksesoris = aksesoris
        self.ket = ket

    def __repr__(self):
        return f"id Daftar : {self.id}"


class Logalat(db.Model):
    __tablename__ = 'logalat'

    id = db.Column(db.Integer, primary_key=True)
    aktivitas = db.Column(db.String(25), nullable=False)
    tujuan = db.Column(db.String(100))
    tanggal = db.Column(db.DateTime, default=datetime.now())
    id_alat = db.Column(db.Integer, db.ForeignKey('alat.id'), nullable=False)

    def __init__(self, aktivitas, tujuan):
        self.aktivitas = aktivitas
        self.tujuan = tujuan

    def __repr__(self):
        return f"id Logalat : {self.id}"


