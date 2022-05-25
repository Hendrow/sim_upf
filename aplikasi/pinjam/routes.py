from flask import Blueprint, jsonify, render_template, redirect, url_for, session, flash, request
from aplikasi import db
from aplikasi.models import Log_pinjam, Peminjam_alat, Fasyankes, Loguser, Alat
from .forms import Input, Form_add_alat
from datetime import datetime

mod = Blueprint('pinjam',__name__, template_folder='templates')


@mod.route('/pinjam', methods=['GET'])
def index():
    if 'username' in session:
        data = {
            'title': 'Data Peminjaman',
            'header' : 'Data Peminjaman',
            'pinjam': Peminjam_alat.query.order_by(Peminjam_alat.tanggal.desc()).limit(50).all()
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
            status = 'Input'
            tujuan = str(form.tujuan.data)
            tanggal_berangkat = form.tanggal_berangkat.data
            tanggal_kembali = form.tanggal_kembali.data
            keterangan = form.keterangan.data

            if peminjam_alat != session.get('nm_lengkap'):
                # status input untuk proses yang belum selesai, submit untuk proses yang sudah selesai
                pinjam = Peminjam_alat(peminjam_alat,petugas_catat, status, tujuan, tanggal_berangkat,tanggal_kembali, keterangan)
                db.session.add(pinjam)
                db.session.commit()

                return redirect(url_for('pinjam.daftar',id=pinjam.id))
            else:
                flash("Maaf petugas catat tidak boleh meminjam !!!", "error")
                return redirect(url_for('pinjam.input'))

        return render_template('pinjam/input.html', data=data, form=form)
    
    return redirect(url_for('user.login'))


@mod.route('/pinjam/input/<int:id>', methods=['GET','POST'])
def daftar(id):
    if 'username' in session:
        data = {
            'title': 'Daftar peminjaman',
            'header' : 'Daftar Peminjaman',
            'query' : Peminjam_alat.query.get_or_404(id)
        }

        form = Form_add_alat()
        if form.validate_on_submit():
            kd_alat = form.kd_alat.data
            # mencari id kode alat
            alat = Alat.query.filter_by(kd_alat=kd_alat).first()
            if alat:
                # FILTER ALAT TIDAK BOLEH SAMA PADA 1 PEMINJAM
                rangkap = 0
                cari = Log_pinjam.query.filter_by(id_peminjam=id).all()
                for i in cari:
                    if i.id_alat == alat.id:
                        rangkap = 1

                if rangkap==0:
                    qlog = Log_pinjam(alat.id, id,"")
                    db.session.add(qlog)
                    db.session.commit()
                    flash('Data berhasil ditambahkan','success')
                else:
                    flash('Maaf, Data sudah ada!','danger')
                                
                return redirect(url_for('pinjam.daftar', id=id))

        detail = Log_pinjam.query.filter_by(id_peminjam=id).all()
        return render_template('pinjam/input_alat.html', data=data, detail=detail, form=form)
    return redirect(url_for('user.login'))

@mod.route('/pinjam/inputalat/<int:id>', methods=['GET','POST'])
def inputalat(id):
    if request.method == "POST":
        id_alat = request.form['hasil']        
        id_peminjam = id

        print(f'{id_alat} and {id_peminjam}')

        q = Log_pinjam(id_alat, id_peminjam,"")
        db.session.add(q)
        db.session.commit()
        flash('Data berhasil ditambahkan!','success')

        detail = Log_pinjam.query.filter_by(id_peminjam=id_peminjam).all()
        
    return jsonify({'htmlresponse': render_template('pinjam/response.html', detail=detail )})


@mod.route('/pinjam/<int:id>/hapus', methods=['GET','POST'])
def hapus(id):
    if 'username' in session:
        pinjam = Peminjam_alat.query.get(id)
        if pinjam:
            db.session.delete(pinjam)

        logpinjam = Log_pinjam.query.filter_by(id_peminjam=id).all()
        if logpinjam:               
            # hapus id diatas pada table Peminjaman_alat dan Log_pinjam
            db.session.delete(logpinjam)            
               
            
        aksi = f"menghapus peminjaman alat id:{pinjam.id}"
        log = Loguser(session['username'], aksi)
        db.session.add(log)

        db.session.commit()
        flash("Data berhasil dihapus!!", "info")
        return redirect(url_for('pinjam.index'))

    return redirect(url_for('user.login'))


@mod.route('/pinjam/lihat_data/<int:id>')
def lihat_data(id):
    if 'username' in session:
        data = {
            'title' : 'Daftar Pinjam Alat',
            'header' :'Daftar Pinjam Alat'
        }
        peminjam = Peminjam_alat.query.get(id)
        lihat = Log_pinjam.query.filter_by(id_peminjam=id).all()
        return render_template('pinjam/daftar_pinjam.html', data=data, lihat=lihat, peminjam=peminjam)
    return redirect(url_for('user.login'))


@mod.route('/pinjam/hapus_alat/<int:id>', methods=['GET','POST'])
def hapus_alat(id):
    if "username" in session:
        # cek id pada table
        clog = Log_pinjam.query.get_or_404(id)
        if clog:
            nm_alat= clog.alat.nm_alat
            id_peminjam = clog.id_peminjam
            db.session.delete(clog)

            aksi = f"hapus peminjaman alat:{nm_alat}"
            log = Loguser(session['username'], aksi)
            db.session.add(log)

            # eksekusi query
            db.session.commit()
            flash(f'Alat {clog.alat.nm_alat} berhasil dihapus!!','info')
            return redirect(url_for('pinjam.daftar', id=id_peminjam))
    return redirect(url_for('user.login'))


@mod.route('/pinjam/simpan_proses/<int:id>', methods=['GET','POST'])
def simpan_proses(id):
    if "username" in session:
        pinjam = Peminjam_alat.query.get_or_404(id)
        if pinjam:
            pinjam.status ='Pinjam'

            aksi = f"Pinjam alat: {pinjam.id} simpan"
            log = Loguser(session['username'], aksi)
            db.session.add(log)
            db.session.commit()

            flash('Proses peminjaman alat selesai!','success')
            return redirect(url_for('pinjam.index'))

    return redirect(url_for('user.login'))


@mod.route('/pinjam/selesai/<int:id>', methods=['GET','POST'])
def selesai(id):
    if "username" in session:
        pinjam = Peminjam_alat.query.get_or_404(id)
        if pinjam:
            pinjam.status ='dikembalikan'
            pinjam.tanggal_selesai = datetime.now()

            aksi = f"Pengembalian alat: {pinjam.id} simpan"
            log = Loguser(session['username'], aksi)
            db.session.add(log)
            db.session.commit()

            flash('Proses pengembalian alat selesai!','success')
            return redirect(url_for('pinjam.index'))
    return redirect(url_for('user.login'))


@mod.route('/pinjam/pengembalian/<int:id>')
def pengembalian(id):
    if "username" in session:
        data = {
            'title' : 'Pengembalian Alat',
            'header' :'Pengembalian Alat'
        }
        peminjam = Peminjam_alat.query.get(id)
        lihat = Log_pinjam.query.filter_by(id_peminjam=id).all()
        
        return render_template('pinjam/pengembalian.html', data=data, lihat=lihat, peminjam=peminjam)
    return redirect(url_for('user.login'))


@mod.route('/pinjam/note/<int:id>', methods=['GET','POST'])
def note(id):
    l = Log_pinjam.query.get_or_404(id)
    if l:
        if request.method == "POST":
            note = request.form['note']
            l.note = note
            db.session.commit()
            return redirect(url_for('pinjam.pengembalian', id=l.id_peminjam))
    