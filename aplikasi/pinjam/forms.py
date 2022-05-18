from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from aplikasi.models import Fasyankes


def pilih_fasyankes():
    return Fasyankes.query

class Input(FlaskForm):    
    peminjam_alat =  SelectField('Peminjam Alat',
        choices=[('none','...Pilih..'),('Andi P','Andi Purba'),('Azizil T','Azizil Tiara Putra'),('M Agung','M Agung S'),('M Ilham','M Ilham Maulana'),('Sandra M','Sandra Monika'),('Demtania','Demtania'),('Robiyansyah','Robiyansyah'),('Elvira','Elvira'), ('Hendro','Hendro')])    
    tujuan = QuerySelectField(query_factory=pilih_fasyankes, allow_blank=True, get_label='nama')
    tanggal_berangkat = DateField('Tanggal Keberangkatan', validators=[DataRequired()])  
    tanggal_kembali = DateField('Tanggal Kembali', validators=[DataRequired()])  
    keterangan = StringField("Keterangan", validators="")
    simpan = SubmitField('Lanjut')

class Form_add_alat(FlaskForm):
    kd_alat =  StringField('Kode Alat', validators=[DataRequired()])
    simpan = SubmitField('Simpan')