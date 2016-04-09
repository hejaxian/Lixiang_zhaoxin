#coding=utf-8
#加载数据库模块
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

#配置数据库
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql+mysqldb://[sql_user]:[sql_passwd]@[host:port]/[db_name]'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 5
app.config['SQLALCHEMY_POOL_SIZE'] = 5
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 10
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 5  

    
db = SQLAlchemy(app)