from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email, Length


class Register(FlaskForm):
    username =  StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    password =  PasswordField('Password', validators=[DataRequired(), EqualTo('confirm'), Length(min=6, max=50)])
    confirm = PasswordField('Repeat Password')
    email = StringField('Email', validators=[DataRequired(), Email()])
    nm_lengkap = StringField('Nama lengkap', validators=[DataRequired(), Length(min=6, max=30)])
    level =  SelectField('Level',
        choices=[('none','...Pilih..'),('admin','Admin'),('pengguna','Pengguna')])  
    submit = SubmitField('Submit')


class Edit_user(FlaskForm):
    username =  StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])    
    email = StringField('Email', validators=[DataRequired(), Email()])
    nm_lengkap = StringField('Nama lengkap', validators=[DataRequired(), Length(min=6, max=30)])
    level =  SelectField('Level',
        choices=[('none','...Pilih..'),('admin','Admin'),('pengguna','Pengguna')])  
    submit = SubmitField('Submit')