from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class Input(FlaskForm):
    nm_alat =  StringField('Nama alat', validators=[DataRequired()])
    merk =  StringField('Merk alat', validators=[DataRequired()])
    tipe =  StringField('Tipe alat', validators=[DataRequired()])
    no_seri =  StringField('No Seri', validators=[DataRequired()])
    tgl_kalibrasi = DateField('Tgl. Kalibrasi')  
    aksesoris =  StringField('Aksesoris alat')
    th_pengadaan =  StringField('Tahun pengadaan')
    ket =  StringField('Keterangan')
    simpan = SubmitField('Simpan')


class Edit(FlaskForm):
    nm_alat =  StringField('Nama alat', validators=[DataRequired()])
    merk =  StringField('Merk alat', validators=[DataRequired()])
    tipe =  StringField('Tipe alat', validators=[DataRequired()])
    no_seri =  StringField('No Seri', validators=[DataRequired()])
    tgl_kalibrasi = DateField('Tgl. Kalibrasi')
    aksesoris =  StringField('Aksesoris alat')
    th_pengadaan =  StringField('Tahun pengadaan')
    ket =  StringField('Keterangan')
    edit = SubmitField('Update')