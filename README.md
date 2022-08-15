# pythonProject
一个python的项目

## 1. 安装环境
### 1.1 安装虚拟环境
pip install virtualenv

### 1.2 创建虚拟环境，叫venv，可以自定义
virtualenv venv

### 1.3 加载虚拟环境
source venv/bin/active
windows: source ./activate

### 1.4 退出虚拟环境
deactive就行

### 1.5 通过requirement.txt安装包 
requirement.txt的生成是pip freeze > requirement.txt生成的
pip install -r requirement.txt

### 1.6 查看新环境安装的包
pip list

### 1.7 遇到的问题
./manage.py shell时报错，原因是Django的版本和python的匹配，需要升级下Django，pip install -U Django


1. source ./venv/bin/active
2. ./manage.py startapp user  => create use module
3. ./manage.py shell => into debug mode

test
