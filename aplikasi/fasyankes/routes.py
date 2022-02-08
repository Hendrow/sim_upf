from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from aplikasi import db
from aplikasi.models import Fasyankes, Loguser
from .forms import Input, Edit


mod = Blueprint('fasyankes',__name__, template_folder='templates')


@mod.route('/fasyankes')
def index():
    if 'username' in session:
        data = {'title':'Data Fasyankes',
            'header':'Data Fasyankes',
            'fasyankes': Fasyankes.query.all()}

        return render_template('fasyankes/index.html', data=data)
    
    return redirect(url_for('user.login'))


@mod.route('/fasyankes/input', methods=['GET','POST'])
def input():
    if 'username' in session:
        data = {'title':'Input Fasyankes',
            'header':'Input Fasyankes'}

        form=Input()
        if form.validate_on_submit():            
            nama = form.nama.data
            status = form.status.data
            alamat = form.alamat.data
            kota = form.kota.data
            provinsi = form.provinsi.data
            email = form.email.data
            telepon = form.telepon.data
            fax = form.fax.data
            
            # input data ke dalam table fasyankes
            add_fasyankes = Fasyankes(nama, status, alamat, kota, provinsi, email, telepon, fax)
            db.session.add(add_fasyankes)
            
            # flush data fasyankes sebelum commit
            db.session.flush()

            aksi = f"add fasyankes: {add_fasyankes.id}"
            log = Loguser(session['username'], aksi)
            db.session.add(log)
            # commit data add fasyankes dan loguser
            db.session.commit()

            flash('Data berhasil disimpan!!!','success')
            return redirect(url_for('fasyankes.index'))
            
        return render_template('fasyankes/input.html', data=data, form=form)
    
    return redirect(url_for('user.login'))


@mod.route('/fasyankes/<int:id>/edit', methods=['GET','POST'])
def edit(id):
    if 'username' in session:
        data = {'title':'Edit data',
            'header':'Edit data'}
        cari = Fasyankes.query.get_or_404(id)

        form = Edit()
        if form.validate_on_submit():
            cari.nama = form.nama.data
            cari.status = form.status.data
            cari.alamat = form.alamat.data
            cari.kota = form.kota.data
            cari.provinsi = form.provinsi.data
            cari.email = form.email.data
            cari.telepon = form.telepon.data
            cari.fax = form.fax.data

            aksi = f"fasyankes edit: {cari.id}"
            log = Loguser(session['username'], aksi)
            db.session.add(log)
            db.session.commit()

            flash('Data berhasil diupdate!!','success')
            return redirect(url_for('fasyankes.index'))

        form.nama.data = cari.nama
        form.status.data = cari.status
        form.alamat.data = cari.alamat
        form.kota.data = cari.kota
        form.provinsi.data = cari.provinsi
        form.email.data = cari.email
        form.telepon.data = cari.telepon
        form.fax.data = cari.fax

        return render_template('fasyankes/edit.html', data=data, form=form)

    return redirect(url_for('user.login'))


@mod.route('/fasyankes/<int:id>/hapus', methods=['GET','POST'])
def hapus(id):
    if 'username' in session:
        f = Fasyankes.query.get_or_404(id)
        if f:
            db.session.delete(f)

            aksi = f"fasyankes del:{f.nama}"
            log = Loguser(session['username'], aksi)
            db.session.add(log)
            db.session.commit()

            flash('Data telah terhapus !!','warning')
            return redirect(url_for('fasyankes.index'))
    
    return redirect(url_for('user.login'))