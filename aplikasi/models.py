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

    def __repr__(self):
        return "Nama alat : {}".format(self.nmAlat)


class Logkalibrasi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tempat_kalibrasi = db.Column(db.String(55), nullable = False)
    tgl_kalibrasi = db.Column(db.DateTime)
    hasil = db.Column(db.String(25))
    alat_id = db.Column(db.Integer, db.ForeignKey('alat.id'))

    def __repr__(self):
        return "Tempat : {}, Tanggal : {}".format(self.tempatKalibrasi, self.tglKalibrasi)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable= False)
    email = db.Column(db.String(50), unique=True)
    nmLengkap = db.Column(db.String(100), nullable=False)
    gambar = db.Column(db.String(100))

    def __repr__(self):
        return "Username : {}".format(self.username)

class Loguser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    aksi = db.Column(db.String(25), nullable=False)
    tanggal = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return "aksi : {}".format(self.aksi)


class Fasyankes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    alamat = db.Column(db.String(125), nullable=False)
    kota = db.Column(db.String(25), nullable=False)
    provinsi = db.Column(db.String(25))
    email = db.Column(db.String(30))
    telepon = db.Column(db.String(45))
    fax = db.Column(db.String(30))

    def __repr__(self):
        return "{}".format(self.nama)


class Pinjam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    peminjam = db.Column(db.String(25), nullable=False)
    petugas = db.Column(db.String(25), nullable=False)
    tanggal = db.Column(db.DateTime, nullable=False)
    kordinatorTim = db.Column(db.String(25))
    status = db.Column(db.String(25), nullable=False)
    fasyankes = db.Column(db.String(100), nullable=False)
    alatPinjam = db.relationship('Daftarpinjam', backref='pinjam', lazy=True)

    def __repr__(self):
        return "id Pinjam : {}".format(self.id)


class Daftarpinjam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aksesoris = db.Column(db.String(50), nullable=False)
    ket = db.Column(db.String(15), nullable=False)
    idPinjam = db.Column(db.Integer, db.ForeignKey('pinjam.id'), nullable=False)
    idAlat = db.Column(db.Integer, db.ForeignKey('alat.id'), nullable=False)

    def __repr__(self):
        return "id Daftar : {}".format(self.id)


class Logalat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aktivitas = db.Column(db.String(25), nullable=False)
    tujuan = db.Column(db.String(100))
    tanggal = db.Column(db.DateTime, default=datetime.now())
    idAlat = db.Column(db.Integer, db.ForeignKey('alat.id'), nullable=False)

    def __repr__(self):
        return "id Logalat : {}".format(self.id)


