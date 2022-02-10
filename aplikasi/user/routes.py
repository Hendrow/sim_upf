from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from sqlalchemy import exc
from .forms import Register
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
                return redirect(url_for('main.index'))
            else:
                flash('Username/password salah!!!', 'danger')
                return redirect(url_for('user.login'))

        flash('Username/password tidak ada!!','warning')
        return redirect(url_for('user.login'))
        
    return render_template('user/login.html')


@mod.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('user.login'))


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
            pwdnew = pw_hash.decode("utf-8", "ignore")

            u = Users(username, pwdnew, email, nm_lengkap, "")
            db.session.add(u)
            db.session.commit()
            flash('Register user baru berhasil!','success')
            return redirect(url_for('user.reg')) 
        except exc.IntegrityError:
            db.session.rollback()
            flash('Maaf, data sudah ada !!!. Silahkan gunakan yang lain.','danger')
            return redirect(url_for('user.reg'))        

    return render_template('user/register.html', data=data, form=form)