#coding=utf-8
#加载wtf表单模块
from flask import Flask
from flask.ext.wtf import Form
from flask_wtf.csrf import CsrfProtect
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, validators
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email

app = Flask(__name__)
CsrfProtect(app)

#定义招新表单
class Join_imformation(Form):
    xiangmu = [('',u'请选择'), (u'电影',u'电影'), (u'新闻', u'新闻'), (u'纪录片', u'纪录片'), (u'内地综艺',u'内地综艺'),
               (u'足球',u'足球'), (u'动漫',u'动漫'), (u'音乐',u'音乐'), (u'MV',u'MV'), (u'英美剧',u'英美剧'),
               (u'大陆剧',u'大陆剧'), (u'港台剧', u'港台剧'), (u'日韩剧',u'日韩剧'), (u'版主',u'版主'), (u'美工',u'美工') ]

    name = StringField(u'姓名',validators=[DataRequired(u'请输入姓名')])
    sex = SelectField(u'性别', choices=[('',u'请选择'),(u'男',u'男'), (u'女', u'女')] )
    banji = StringField(u'班级',validators=[DataRequired(u'请输入班级')])
    school = SelectField(u'学校', choices=[('',u'请选择'), (u'本科',u'本科'), (u'专科', u'专科'), (u'技师', u'技师')] )
    disk = StringField(u'硬盘容量',validators=[DataRequired(u'请输入硬盘容量')])
    email = StringField(u'电子邮件', validators=[DataRequired(u'请输入电子邮件地址'), Email(u'无效的邮箱地址')])
    phone = StringField(u'手机号码',validators=[DataRequired(u'请输入手机号码')])
    
    lixiang_username = StringField(u'荔香站用户名',validators=[DataRequired(u'请输入荔香站用户名')])
    block = SelectField(u'应聘板块', choices=xiangmu )
    block_backup = SelectField(u'备选应聘板块', choices=xiangmu)
    source = StringField(u'资源来源',validators=[DataRequired(u'请输入资源来源')])
    uptime = StringField(u'每日在线时间',validators=[DataRequired(u'请输入每日在线时间')])
    photo = FileField(u'照片', validators=[FileRequired(u'请上传照片'),FileAllowed(['jpg'], u'只接受JPG格式图片')])
    submit = SubmitField(u'提交') 
    
#定义登录表单
class Login(Form):
    username = StringField(u'用户名',validators=[DataRequired(u'请输入用户名')])
    password = PasswordField(u'密码',validators=[DataRequired(u'请输入密码')])
    remember_me = BooleanField(u'保持登陆', default=False)
    submit = SubmitField(u'登陆') 