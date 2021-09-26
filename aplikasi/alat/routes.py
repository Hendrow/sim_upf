from flask import Blueprint, render_template, redirect, url_for, session, flash
from .forms import Input, Edit
from aplikasi import db
from aplikasi.models import Alat, Loguser

mod = Blueprint('alat',__name__, template_folder='templates')


@mod.route('/alat/daftar')
def index():
    if 'username' in session:
        data = {
            'title': 'Alat Kalibrasi',
            'header' : 'Daftar Alat'
        }

        alat = Alat.query.all()
        return render_template('alat/daftar_alat.html', data=data, alat=alat)
    else:
        return redirect(url_for('user.login'))    


@mod.route('/alat/tambah', methods=['GET','POST'])
def add():
    if 'username' in session:
        data = {
            'title': 'Input data',
            'header' : 'Input data'
        }

        form = Input()
        if form.validate_on_submit():
            nm_alat = form.nm_alat.data
            merk = form.merk.data
            tipe = form.tipe.data
            no_seri = form.no_seri.data
            aksesoris = form.aksesoris.data
            th_pengadaan = form.th_pengadaan.data
            ket = form.ket.data

            m_alat = Alat(nm_alat=nm_alat, merk=merk, tipe=tipe, no_seri=no_seri, aksesoris=aksesoris, th_pengadaan=th_pengadaan, ket=ket)
            db.session.add(m_alat)

            aksi = f"tambah alat: {nm_alat}"
            log = Loguser(username=session['username'], aksi=aksi)
            db.session.add(log)
            db.session.commit()

            flash('Data sudah tersimpan..','success')
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
                alat.aksesoris = form.aksesoris.data
                alat.th_pengadaan = form.th_pengadaan.data
                alat.ket = form.ket.data

                aksi = "Edit alat id: " +str(alat.id)
                log = Loguser(username=session['username'], aksi=aksi)
                db.session.add(log)

                db.session.commit()
                flash("Update data success...", "info")
                return redirect(url_for('alat.index'))

            form.nm_alat.data = alat.nm_alat
            form.merk.data = alat.merk
            form.tipe.data = alat.tipe
            form.no_seri.data = alat.no_seri
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

            aksi = "Del alat id:" +str(alat.id)
            log = Loguser(username=session['username'], aksi = aksi)
            db.session.add(log)

            db.session.commit()
            flash("1 data sudah dihapus..", "warning")
            return redirect(url_for('alat.index'))
    
    return redirect(url_for('user.login'))

    