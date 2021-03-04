from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email, Length


class Register(FlaskForm):
    username =  StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    password =  PasswordField('Password', validators=[DataRequired(), EqualTo('confirm'), Length(min=6, max=50)])
    confirm = PasswordField('Repeat Password')
    email = StringField('Email', validators=[DataRequired(), Email()])
    nmLengkap = StringField('Nama lengkap', validators=[DataRequired(), Length(min=7, max=30)])
    submit = SubmitField('Submit')