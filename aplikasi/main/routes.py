from flask import Blueprint, render_template, redirect, url_for, session

mod = Blueprint('main',__name__, template_folder='templates')


@mod.route('/')
@mod.route('/index')
def index():
    if 'username' in session:
        return redirect(url_for('main.dashboard'))
    else:
        return redirect(url_for('user.login'))

@mod.route('/dashboard')
def dashboard():
    if 'username' in session:
        data = {
            'title': 'Dashboard',
            'header' : 'Dashboard',
            'nama' : session.get('nm_lengkap')
        }
        return render_template('dashboard.html', data=data)

    return redirect(url_for('user.login'))