from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Input(FlaskForm):
    nmAlat =  StringField('Nama alat', validators=[DataRequired()])
    merk =  StringField('Merk alat', validators=[DataRequired()])
    tipe =  StringField('Tipe alat', validators=[DataRequired()])
    noSeri =  StringField('No Seri', validators=[DataRequired()])
    aksesoris =  StringField('Aksesoris alat')
    thPengadaan =  StringField('Tahun pengadaan')
    ket =  StringField('Keterangan')
    simpan = SubmitField('Simpan')


class Edit(FlaskForm):
    nmAlat =  StringField('Nama alat', validators=[DataRequired()])
    merk =  StringField('Merk alat', validators=[DataRequired()])
    tipe =  StringField('Tipe alat', validators=[DataRequired()])
    noSeri =  StringField('No Seri', validators=[DataRequired()])
    aksesoris =  StringField('Aksesoris alat')
    thPengadaan =  StringField('Tahun pengadaan')
    ket =  StringField('Keterangan')
    edit = SubmitField('Update')