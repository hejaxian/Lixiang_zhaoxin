#coding=utf-8
from sql import *
from sql_model import *

db.drop_all()
db.create_all()

hjx = User(username='hejiaxian', password='kengdiene')
ct = User(username='ct', password='ctnmb')
db.session.add(hjx)
db.session.add(ct)
db.session.commit()