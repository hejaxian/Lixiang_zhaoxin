# Lixiang_zhaoxin

荔香站招新登记页面

本程序基于Python 2.7,使用Flask框架和MySQL数据库。
依赖包已在requirement.txt中给出。

使用：
1、下载本程序 
```
git clone https://github.com/hejaxian/Lixiang_zhaoxin.git
```

2、在程序根目录下进入虚拟环境
```
source venv/bin/activate
```

3、安装依赖包
进入虚拟环境后执行以下命令
```
pip install -r requirement.txt
```

注：如果在Centos环境下运行，请自行yum install mysql-python

4、配置数据库
编辑sql.py
更改其中的第九行
```
'mysql+mysqldb://[sql_user]:[sql_passwd]@[host:port]/[db_name]'
```
[sql_user]为数据库用户名  
[sql_passwd]为数据库密码  
[host:port]为数据库服务器地址以及端口  
[db_name]为数据库名

5、测试程序
在程序目录下执行以下命令
```
python main.py
```
然后访问http://localhost:5000测试本程序是否可用。

6、创建Supervisor守护进程

服务配置文件如下（该配置仅供测试，实际运行配置需要酌情更改）
```
[program:zhaoxin]
command = gunicorn -w 4 -b 0.0.0.0:8002 main:app -k gevent --log-level=debug
directory = /var/python/lx_zhaoxin
startsecs = 0
stopwaitsecs = 0
autostart = true
autorestart = true
stdout_logfile = /var/log/zx_std.log
stderr_logfile = /var/log/zx_err.log 
```

[program:zhaoxin]为supervisor服务名称，如需要更改请自行更改。  
directory为本程序所在目录，请酌情更改。  
--log-level=debug 为日志等级，在生产环境中请更换为info。  
-b 0.0.0.0:8002 为监听地址以及端口，若使用Nginx作为前端改为127.0.0.1:8002或其他端口。  

7、测试守护进程
添加服务后重启supervisor
```
service supervisor restart 或 systemctl restart supervisord
```
查看守护进程状态
```
supervisorctl status zhaoxin
```
如果在运行请访问http://localhost:8002测试是否可用。

8、配置Web服务器
如果需要使用Nginx或者Apache作为web服务器，只需要在守护进程工作正常后，反向代理http://127.0.0.1:8002即可。
