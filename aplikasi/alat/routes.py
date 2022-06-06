from flask import Blueprint, render_template, redirect, url_for, session, flash
from .forms import Input, Edit
from aplikasi import db
from aplikasi.models import Alat, Loguser

mod = Blueprint('alat',__name__, template_folder='templates')


@mod.route('/alat/daftar')
def index():
    if 'username' in session:
        data = {
            'title': 'Data Alat',
            'header' : 'Data Alat Kalibrasi'
        }

        alat = Alat.query.order_by(Alat.id).all()
        return render_template('alat/daftar_alat.html', data=data, alat=alat)
    else:
        return redirect(url_for('user.login'))    


@mod.route('/alat/tambah', methods=['GET','POST'])
def add():
    if 'username' in session:
        data = {
            'title': 'Input Alat',
            'header' : 'Input Alat'
        }

        form = Input()
        if form.validate_on_submit():
            alat = Alat.query.order_by(Alat.id.desc()).first()
            if alat:
                id_number = alat.id + 1
                if len(str(id_number)) < 5:
                    urut = "0" * (5-len(str(id_number))) + str(id_number)
                    kd = f"PK{urut}"
            else:
                id_number = 1
                urut = "0" * (5-1) + str(id_number)
                kd = f"PK{urut}"

            kd_alat = kd
            nm_alat = form.nm_alat.data
            merk = form.merk.data
            tipe = form.tipe.data
            no_seri = form.no_seri.data
            tgl_kalibrasi = form.tgl_kalibrasi.data
            aksesoris = form.aksesoris.data
            th_pengadaan = form.th_pengadaan.data
            ket = form.ket.data

            add_alat = Alat(kd_alat, nm_alat, merk, tipe, no_seri, aksesoris, th_pengadaan, ket, tgl_kalibrasi)
            db.session.add(add_alat)

            aksi = f"input alat:{kd_alat}"

            catatan = Loguser(session['username'], aksi)
            db.session.add(catatan)
            db.session.commit()

            flash('Data sudah disimpan!!','success')
            return redirect(url_for('alat.index'))

        return render_template('alat/tambah_alat.html', data=data, form=form)
    else:
        return redirect(url_for('user.login'))


@mod.route('/alat/<int:id>/edit', methods=['GET','POST'])
def edit(id):
    if 'username' in session:
        data = {
            'title': 'Edit alat',
            'header' : 'Edit alat'
        }

        alat = Alat.query.get_or_404(id)
        if alat:
            form = Edit()
            if form.validate_on_submit():
                alat.nm_alat = form.nm_alat.data
                alat.merk = form.merk.data
                alat.tipe = form.tipe.data
                alat.no_seri = form.no_seri.data
                alat.tgl_kalibrasi = form.tgl_kalibrasi.data
                alat.aksesoris = form.aksesoris.data
                alat.th_pengadaan = form.th_pengadaan.data
                alat.ket = form.ket.data

                aksi = f"edit alat id:{alat.id}"

                catatan = Loguser(session['username'], aksi)
                db.session.add(catatan)

                db.session.commit()
                flash("Data berhasil diupdate!!", "info")
                return redirect(url_for('alat.index'))

            form.nm_alat.data = alat.nm_alat
            form.merk.data = alat.merk
            form.tipe.data = alat.tipe
            form.no_seri.data = alat.no_seri
            form.tgl_kalibrasi.data = alat.tgl_kalibrasi
            form.aksesoris.data = alat.aksesoris
            form.th_pengadaan.data = alat.th_pengadaan
            form.ket.data = alat.ket

            return render_template('alat/edit_alat.html',data=data, form=form)
            
    return redirect(url_for('user.login'))


@mod.route('/alat/<int:id>/hapus', methods=['GET','POST'])
def hapus(id):
    if 'username' in session:
        alat = Alat.query.get_or_404(id)
        if alat:
            db.session.delete(alat)

            aksi = f"hapus alat id:{alat.id}"
            log = Loguser(session['username'], aksi)
            db.session.add(log)

            db.session.commit()
            flash("Data berhaisl dihapus!!", "info")
            return redirect(url_for('alat.index'))
    
    return redirect(url_for('user.login'))

    