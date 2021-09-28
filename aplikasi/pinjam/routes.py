from flask import Blueprint, render_template, redirect, url_for, session, flash
from aplikasi import db
from aplikasi.models import Pinjam, Fasyankes, Loguser
from .forms import Input

mod = Blueprint('pinjam',__name__, template_folder='templates')


@mod.route('/pinjam', methods=['GET'])
def index():
    if 'username' in session:
        data = {
            'title': 'Daftar Peminjaman',
            'header' : 'Daftar Peminjaman',
            'pinjam': Pinjam.query.filter_by(status='submit').all()
        }
        return render_template('pinjam/index.html', data=data)
    
    return redirect(url_for('user.login'))

@mod.route('/pinjam/draf', methods=['GET','POST'])
def draf():
    if 'username' in session:
        data = {
            'title':'Draf Peminjaman',
            'header':'Draf peminjaman',
            'pinjam': Pinjam.query.filter_by(status='input').all()
        }
        return render_template('pinjam/draf_pinjam.html', data=data)

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
            peminjam_alat = form.peminjam_alat.data
            petugas_catat = form.petugas_catat.data
            tanggal = form.tanggal.data
            kordinator_tim = form.kordinator_tim.data
            status = 'input'
            fasyankes = str(form.fasyankes.data)

            print(fasyankes)
            # return "{}".format(fasyankes)

            if peminjam_alat != petugas_catat:
                # status input untuk proses input belum selesai, submit untuk proses yang sudah selesai
                pinjam = Pinjam(peminjam_alat,petugas_catat, tanggal,kordinator_tim, status, fasyankes)
                db.session.add(pinjam)
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

@mod.route('/pinjam/<int:id>/hapus', methods=['GET','POST'])
def hapus(id):
    if 'username' in session:
        p = Pinjam.query.get_or_404(id)
        if p:
            db.session.delete(p)
            aksi = f"pinjam del id:{p.id}"
            log = Loguser(session['username'], aksi)
            db.session.add(log)

            db.session.commit()
            flash("1 data sudah dihapus..", "warning")
            return redirect(url_for('pinjam.index'))

    return redirect(url_for('user.login'))


@mod.route('/pinjam/scan')
def scan():
    data = {
            'title': 'Scan',
            'header' : 'Scan'
        }
    return render_template('pinjam/scanqrcode.html', data=data)