[uwsgi]
#使用nginx连接时使用
socket=127.0.0.1:8080
#直接做web服务器使用
#http=127.0.0.1:8080
#项目目录
chdir=/home/python/Desktop/market
#项目中wsgi.py文件的目录，相对于项目目录
wsgi-file=market/wsgi.py
processes=4
threads=2
master=True
pidfile=uwsgi.pid
daemonize=uwsgi.log
virtualenv=/home/python/.virtualenvs/test1
