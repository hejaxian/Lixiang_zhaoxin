#!/usr/bin/env python
#coding=utf-8
from flask import Flask, render_template, request, session, redirect, flash, g, url_for, send_from_directory
#加载bootstrap框架模块
from flask.ext.bootstrap import Bootstrap
#加载Flask-login模块
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
#加载表单
from form import *
#加载数据库模型
from sql_model import *
import os.path

app = Flask(__name__)
bootstrap = Bootstrap(app)
#配置密匙
app.config['SECRET_KEY'] = 'any string'
app.config['SECURITY_PASSWORD_SALT'] = 'my_precious_two'
#配置Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
#配置照片目录
photodir = os.path.join(app.root_path,'photos')

@login_manager.unauthorized_handler
def unauthorized():
    return redirect("/login")
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
#路由
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join_us',methods=['POST','GET'])
def join_us():
    form = Join_imformation()
    if form.validate_on_submit():
       join = Join(name=form.name.data, sex=form.sex.data, banji=form.banji.data, school=form.school.data,
                   disk=form.disk.data, email=form.email.data, phone=form.phone.data, lx_username=form.lixiang_username.data,
                   block=form.block.data, block_backup=form.block_backup.data, source=form.source.data, uptime=form.uptime.data)
       filename = form.lixiang_username.data + ".jpg"
       join.photo = filename
       form.photo.data.save('photos/' + filename)
       db.session.add(join)
       db.session.commit()
       flash(u'登记成功!')
    return render_template('join_us.html',form=form)
    
@app.route('/login',methods=['POST','GET'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/manage")
        else:
            flash(u'用户名或密码错误')
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")
    
@app.route('/manage')
def manage():    
    g.baoming = Join.query.all()
    return render_template('manage.html')
    
@app.route('/detail/<int:id>')
def detail(id):    
    g.detail = Join.query.filter_by(id = id).first()
    return render_template('detail.html')
    
@app.route('/photo/<filename>')
def photo(filename):
    return send_from_directory(photodir,filename)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)