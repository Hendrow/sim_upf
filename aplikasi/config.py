from datetime import timedelta


SECRET_KEY = '-9UDAJR2Gldkja0fu397hhhhkj;dlaf'
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
# SQLALCHEMY_DATABASE_URI = 'postgresql://upfk:mariana01@localhost/upfk'
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:echo1234@localhost/upfk'
SQLALCHEMY_TRACK_MODIFICATIONS = False
PERMANENT_SESSION_LIFETIME =  timedelta(minutes=10)