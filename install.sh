#!/bin/bash
base_python_interpreter=""
project_domain=""
project_path=`pwd`

read -p "Python interpreter: " base_python_interpreter
read -p "Your domain without protocol (for example, google.com): " project_domain
`$base_python_interpreter -m venv env`
source env/bin/activate
pip install -U pip
pip install -r requirements.txt

sed -i "s~dbms_template_path~$project_path~g" systemd/wiki.service
sed -i "s~dbms_template_domain~$project_domain~g" src/config/settings.py

sudo ln -s $project_path/systemd/wiki.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
