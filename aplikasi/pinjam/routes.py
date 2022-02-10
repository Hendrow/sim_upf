from flask import Blueprint, render_template, redirect, url_for, session, flash
from aplikasi import db
from aplikasi.models import Peminjam_alat, Fasyankes, Loguser
from .forms import Input

mod = Blueprint('pinjam',__name__, template_folder='templates')


@mod.route('/pinjam', methods=['GET'])
def index():
    if 'username' in session:
        data = {
            'title': 'Data Peminjaman',
            'header' : 'Data Peminjaman',
            'pinjam': Peminjam_alat.query.all()
        }
        return render_template('pinjam/index.html', data=data)
    
    return redirect(url_for('user.login'))


@mod.route('/pinjam/input', methods=['GET','POST'])
def input():
    if 'username' in session:
        data = {
            'title': 'Input Peminjaman',
            'header' : 'Input Peminjaman'
        }
        form = Input()
        form.tujuan.query = Fasyankes.query.order_by(Fasyankes.nama).all()

        if form.validate_on_submit():
            peminjam_alat = form.peminjam_alat.data
            petugas_catat = session.get('nm_lengkap')
            # tanggal = form.tanggal.data
            status = 'Pinjam'
            tujuan = str(form.tujuan.data)
            tanggal_berangkat = form.tanggal_berangkat.data
            tanggal_kembali = form.tanggal_kembali.data
            keterangan = form.keterangan.data

            if peminjam_alat != petugas_catat:
                # status input untuk proses yang belum selesai, submit untuk proses yang sudah selesai
                pinjam = Peminjam_alat(peminjam_alat,petugas_catat, status, tujuan, tanggal_berangkat,tanggal_kembali, keterangan)
                db.session.add(pinjam)
                db.session.commit()

                query = Peminjam_alat.query.order_by(Peminjam_alat.id.desc()).first()
                return redirect(url_for('pinjam.daftar',id=query.id))
            else:
                flash("Peminjam dan Pencatat tidak boleh sama!!!", "warning")
                return redirect(url_for('pinjam.input'))

        return render_template('pinjam/input.html', data=data, form=form)
    
    return redirect(url_for('user.login'))


@mod.route('/pinjam/input/<int:id>', methods=['GET','POST'])
def daftar(id):
    if 'username' in session:
        data = {
            'title': 'Daftar peminjaman',
            'header' : 'Daftar Peminjaman'
        }
        return render_template('pinjam/input_alat.html', data=data)
    return redirect(url_for('user.login'))


@mod.route('/pinjam/<int:id>/hapus', methods=['GET','POST'])
def hapus(id):
    if 'username' in session:
        p = Peminjam_alat.query.get_or_404(id)
        if p:
            db.session.delete(p)
            aksi = f"pinjam del id:{p.id}"
            log = Loguser(session['username'], aksi)
            db.session.add(log)

            db.session.commit()
            flash("1 data sudah dihapus..", "warning")
            return redirect(url_for('pinjam.index'))

    return redirect(url_for('user.login'))

