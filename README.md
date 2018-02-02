# CloudComputingAssignment1
AWS EC2 instance is created for deploying the web app in cloud

Flask frame work is used to create the web app. For this, Installed Flask using the below command 
$ sudo pip install Flask 
Httpd is installed instead of apache webserver since EC2 is centos and 
wsgi container is installed using the below commands:

$ sudo yum install httpd 
$ sudo yum install mod_wsgi-python27.x86_64

Configuring the wsgi container with apache/httpd server

Create a file /home/ec2-user/webtool.wsgi
import sys sys.path.append('/home/ec2-user/flask-prod') from helloworld import app as application

Create a file /etc/httpd/sites-available/my.webtool
<virtualhost *:80> ServerName 127.0.0.1

WSGIDaemonProcess webtool u
ser=www-data group=www-data threads=5 home=/home/ec2-user/ WSGIScriptAlias / /home/ec2-user/webtool.wsgi

<directory /home/ec2-user> WSGIProcessGroup webtool WSGIApplicationGroup %{GLOBAL} WSGIScriptReloading On Order deny,allow Allow from all

Activate wsgi ln -s /etc/httpd/sites-available/my.webtool /etc/httpd/conf.d/my.webtool

Now templates directory is created to place html files which flask will read and render them.

Place index.html in templates folder and helloworld.py in /home/ec2-user/ folder.

The web app is used to take input of two strings and compare them to determine whether they are same or not.

