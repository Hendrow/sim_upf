from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email
from wtforms_sqlalchemy.fields import QuerySelectField
from aplikasi.models import Fasyankes


def pilih_fasyankes():
    return Fasyankes.query

class Input(FlaskForm):
    petugas_catat = SelectField('Petugas Pencatat',
        choices=[('none','...Pilih..'),('Andi P','Andi Purba'),('Azizil T','Azizil Tiara Putra'),('M Agung','M Agung S'),('M Ilham','M Ilham Maulana'),('Sandra M','Sandra Monika'),('Demtania','Demtania'),('Robiyansyah','Robiyansyah'),('Elvira','Elvira')])
    peminjam_alat =  SelectField('Peminjam Alat',
        choices=[('none','...Pilih..'),('Andi P','Andi Purba'),('Azizil T','Azizil Tiara Putra'),('M Agung','M Agung S'),('M Ilham','M Ilham Maulana'),('Sandra M','Sandra Monika'),('Demtania','Demtania'),('Robiyansyah','Robiyansyah'),('Elvira','Elvira')])    
    tanggal = DateField('Tanggal peminjaman', validators=[DataRequired()])
    kordinator_tim = SelectField('Kordinator Tim',
        choices=[('none','...Pilih..'),('Andi P','Andi Purba'),('Azizil T','Azizil Tiara Putra'),('M Agung','M Agung S'),('M Ilham','M Ilham Maulana'),('Sandra M','Sandra Monika'),('Demtania','Demtania'),('Robiyansyah','Robiyansyah'),('Elvira','Elvira')])
    fasyankes = QuerySelectField(query_factory=pilih_fasyankes, allow_blank=True, get_label='nama')
    simpan = SubmitField('Lanjut')