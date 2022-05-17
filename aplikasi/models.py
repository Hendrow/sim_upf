from datetime import datetime
from aplikasi import db


class Alat(db.Model):
    __tablename__ = 'alat'

    id = db.Column(db.Integer, primary_key=True)
    kd_alat = db.Column(db.String(6), nullable=False)
    nm_alat = db.Column(db.String(100), nullable=False)
    merk = db.Column(db.String(30), nullable=False)
    tipe = db.Column(db.String(30), nullable=False)
    no_seri = db.Column(db.String(25), nullable=False, unique=True)
    aksesoris = db.Column(db.String(100))
    th_pengadaan = db.Column(db.Integer)
    ket = db.Column(db.String(15))
    log_pinjam = db.relationship('Log_pinjam', backref='alat', lazy=True)

    def __init__(self, kd_alat, nm_alat, merk, tipe, no_seri, aksesoris, th_pengadaan, ket):
        self.kd_alat = kd_alat
        self.nm_alat = nm_alat
        self.merk = merk
        self.tipe = tipe
        self.no_seri = no_seri
        self.aksesoris = aksesoris
        self.th_pengadaan = th_pengadaan
        self.ket = ket

    def __repr__(self):
        return f"{self.nm_alat}"

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


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable= False)
    email = db.Column(db.String(50), unique=True)
    nm_lengkap = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(8), nullable=False)
    gambar = db.Column(db.String(100))

    def __init__(self, username, password, email, nm_lengkap, level, gambar):
        self.username = username
        self.password = password
        self.email = email
        self.nm_lengkap = nm_lengkap
        self.level = level
        self.gambar = gambar

    def __repr__(self):
        return f"{self.username}"

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


class Peminjam_alat(db.Model):
    __tablename__ = 'peminjam_alat'
    id = db.Column(db.Integer, primary_key=True)
    peminjam_alat = db.Column(db.String(25), nullable=False)
    petugas_catat = db.Column(db.String(25), nullable=False)
    tanggal = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.String(25), nullable=False)
    tujuan = db.Column(db.String(100), nullable=False)
    tanggal_berangkat = db.Column(db.Date, nullable=False)
    tanggal_kembali = db.Column(db.Date, nullable=False)
    keterangan = db.Column(db.String(150))
    log_pinjam = db.relationship('Log_pinjam', backref='peminjam', lazy=True)

    def __init__(self, peminjam_alat, petugas_catat,  status, tujuan, tanggal_berangkat, tanggal_kembali, keterangan):
        self.peminjam_alat = peminjam_alat
        self.petugas_catat = petugas_catat
        self.status = status
        self.tujuan = tujuan
        self.tanggal_berangkat = tanggal_berangkat
        self.tanggal_kembali = tanggal_kembali
        self.keterangan = keterangan

    def __repr__(self):
        return f'{self.tujuan}'


class Log_pinjam(db.Model):
    __tablename__ = 'log_pinjam'
    id = db.Column(db.Integer, primary_key=True)
    id_alat = db.Column(db.Integer, db.ForeignKey('alat.id'), nullable=False)
    id_peminjam = db.Column(db.Integer, db.ForeignKey('peminjam_alat.id'), nullable=False)

    def __init__(self, id_alat, id_peminjam):
        self.id_alat = id_alat
        self.id_peminjam = id_peminjam

    def __repr__(self):
        return f'alat: {self.id}, peminjam: {self.id_peminjam}'
