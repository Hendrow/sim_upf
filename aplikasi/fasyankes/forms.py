from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email


class Input(FlaskForm):
    nama =  StringField('Nama Fasyankes', validators=[DataRequired()])
    status =  SelectField('Status', 
        choices=[('none','--Pilihan--'),('perusahaan','Perusahaan'),('klinik','Klinik'),
        ('lab','Laboratorium'),('instansi','Instansi Pemerintah/Kementerian'),('rs pemerintah','RS. Pemerintah'),('rs swasta','RS. Swasta'),
        ('puskesmas','Puskesmas')])
    alamat = StringField("Alamat", validators=[DataRequired()])
    kota = StringField("Kota", validators=[DataRequired()])
    provinsi = StringField("Provinsi", validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(), Email()])
    telepon = StringField("Telepon", validators=[DataRequired()])
    fax = StringField("Fax")
    simpan = SubmitField('Simpan')


class Edit(FlaskForm):
    nama =  StringField('Nama Fasyankes', validators=[DataRequired()])
    status =  SelectField('Status', 
        choices=[('none','--Pilihan--'),('perusahaan','Perusahaan'),('klinik','Klinik'),
        ('lab','Laboratorium'),('instansi','Instansi Pemerintah/Kementerian'),('rs pemerintah','RS. Pemerintah'),('rs swasta','RS. Swasta'),
        ('puskesmas','Puskesmas')])
    alamat = StringField("Alamat", validators=[DataRequired()])
    kota = StringField("Kota", validators=[DataRequired()])
    provinsi = StringField("Provinsi", validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(), Email()])
    telepon = StringField("Telepon", validators=[DataRequired()])
    fax = StringField("Fax")
    update = SubmitField('Update')