#coding=utf-8
from sql import db
#加载密码散列模块
from werkzeug.security import generate_password_hash, check_password_hash

#定义报名
class Join(db.Model):
    __tablename__ = 'joins'
    #记录编号
    id = db.Column(db.Integer, primary_key=True)
    #姓名
    name = db.Column(db.String(64), unique=True, index=True)
    #电子邮件
    email = db.Column(db.String(64), unique=True)
    #性别
    sex = db.Column(db.String(64) )
    #班级
    banji = db.Column(db.String(64) )
    #学校
    school = db.Column(db.String(64) )
    #硬盘容量
    disk = db.Column(db.String(64) )
    #手机号码
    phone = db.Column(db.Integer)
    #荔香用户
    lx_username = db.Column(db.String(64) )
    #应聘板块
    block = db.Column(db.String(64) )
    #备选应聘
    block_backup = db.Column(db.String(64) )
    #资源来源
    source = db.Column(db.String(64) )
    #每日在线时间
    uptime = db.Column(db.String(64) )
    #照片文件
    photo = db.Column(db.String(64), unique=True)
    
#定义用户
class User(db.Model):
    __tablename__ = 'users'
    #用户id
    id = db.Column(db.Integer, primary_key=True)
    #用户名
    username = db.Column(db.String(64), unique=True, index=True)
    #密码(散列值)
    password_hash = db.Column(db.String(128))
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    #Flask-login需要用到的几个判断
    #是否已登陆
    def is_authenticated(self):
        return True
    #账号是否有效
    def is_active(self):
        return True
    #是否陌生人
    def is_anonymous(self):
        return False
    #返回用户id
    def get_id(self):
        return unicode(self.id)


    def __repr__(self):
        return '<User %r>' % self.username