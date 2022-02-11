from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from sqlalchemy import exc
from .forms import Register, Edit_user
from aplikasi import db, bcrypt
from aplikasi.models import Users


mod = Blueprint('user',__name__, template_folder='templates')


@mod.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        user = request.form['username']
        paswd = request.form['password']
        
        u = Users.query.filter_by(username=user).first()
        if u:
            if bcrypt.check_password_hash(u.password, paswd):
                session['username'] = user
                session['nm_lengkap'] = u.nm_lengkap
                session['level'] = u.level
                return redirect(url_for('main.index'))
            else:
                flash('Password anda salah!!', 'warning')
                return redirect(url_for('user.login'))

        flash('Username tidak ditemukan!!','info')
        return redirect(url_for('user.login'))
        
    return render_template('user/login.html')


@mod.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('user.login'))


@mod.route('/user/list')
def list():
    data = {
        'title':'Users list',
        'header':'Users list',
        'user' : Users.query.all()
    }

    return render_template('user/index.html', data=data)


@mod.route('/user/add', methods=['GET','POST'])
def reg():
    data = {
        'title':'Add user',
        'header':'Add user'
    }

    form = Register()
    if form.validate_on_submit():
        try:
            username = form.username.data
            pw_hash = bcrypt.generate_password_hash(form.password.data)
            email = form.email.data
            nm_lengkap = form.nm_lengkap.data
            level = form.level.data
            pwdnew = pw_hash.decode("utf-8", "ignore")

            user = Users(username, pwdnew, email, nm_lengkap,level, "")
            db.session.add(user)
            db.session.commit()
            flash('User baru berhasil dibuat!!','success')
            return redirect(url_for('user.list')) 
        except exc.IntegrityError:
            db.session.rollback()
            flash('Maaf, data sudah ada !!!. Silahkan gunakan yang lain.','warning')
            return redirect(url_for('user.reg'))        

    return render_template('user/register.html', data=data, form=form)

@mod.route('/user/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    data = {
        'title':'Edit user',
        'header':'Edit user'
    }
    user = Users.query.get_or_404(id)

    if user:
        form = Edit_user()
        if form.validate_on_submit():
            user.username = form.username.data
            user.email = form.email.data
            user.nm_lengkap = form.nm_lengkap.data
            user.level = form.level.data
            
            db.session.commit()

            flash("User berhasil diupdate!","info")
            return redirect(url_for('user.list'))
        
        form.username.data = user.username
        form.email.data = user.email
        form.nm_lengkap.data = user.nm_lengkap
        form.level.data = user.level

        return render_template('user/edit.html', data=data, form=form)

    
@mod.route('/user/hapus/<int:id>', methods=['GET','POST'])
def hapus(id):
    user = Users.query.get_or_404(id)
    if user:
        db.session.delete(user)
        db.session.commit()

        flash("Data berhasil dihapus!!","info")
        return redirect(url_for('user.list'))
