from flask import Blueprint, render_template, redirect, url_for, session
from aplikasi import db
from aplikasi.models import Pinjam, Fasyankes
from .forms import Input

mod = Blueprint('pinjam',__name__, template_folder='templates')


@mod.route('/pinjam')
def index():
    if 'username' in session:
        data = {
            'title': 'Peminjaman alat',
            'header' : 'Peminjaman alat',
            'pinjam': Pinjam.query.all()
        }
        return render_template('pinjam/index.html', data=data)
    
    return redirect(url_for('user.login'))


@mod.route('/pinjam/input', methods=['GET','POST'])
def input():
    if 'username' in session:
        data = {
            'title': 'Forn peminjaman',
            'header' : 'Form peminjaman'
        }
        form = Input()
        form.fasyankes.query = Fasyankes.query.order_by(Fasyankes.nama).all()

        if form.validate_on_submit():
            peminjam = form.peminjam.data
            petugas = form.petugas.data
            tanggal = form.tanggal.data
            kordinator_tim = form.kordinatorTim.data
            fasyankes = str(form.fasyankes.data)

            print(fasyankes)
            # return "{}".format(fasyankes)

            if peminjam != petugas:
                p = Pinjam(peminjam=peminjam, petugas=petugas, tanggal=tanggal, kordinatorTim= kordinator_tim, fasyankes=fasyankes, status='null')
                db.session.add(p)
                db.session.commit()

                query = Pinjam.query.order_by(Pinjam.id.desc()).first()
                return redirect(url_for('pinjam.daftar',id=query.id))

        return render_template('pinjam/input.html', data=data, form=form)
    
    return redirect(url_for('user.login'))


@mod.route('/pinjam/input/<int:id>', methods=['GET','POST'])
def daftar(id):
    if 'username' in session:
        data = {
            'title': 'Daftar peminjaman',
            'header' : 'Daftar Peminjaman'
        }
        return render_template('pinjam/daftar_pinjam.html', data=data)
    return redirect(url_for('user.login'))


@mod.route('/pinjam/scan')
def scan():
    data = {
            'title': 'Scan',
            'header' : 'Scan'
        }
    return render_template('pinjam/scanqrcode.html', data=data)