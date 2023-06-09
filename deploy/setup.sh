#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/LiliyaSemenenko/profiles-rest-api.git'

PROJECT_BASE_PATH='/usr/local/apps/profiles-rest-api'

echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

# Create project directory
mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# Create virtual environment
mkdir -p $PROJECT_BASE_PATH/env
python3 -m venv $PROJECT_BASE_PATH/env

# Install python packages
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/env/bin/pip install uwsgi==2.0.21 #2.0.18

# Run migrations and collectstatic
cd $PROJECT_BASE_PATH
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput

# Configure supervisor
cp $PROJECT_BASE_PATH/deploy/supervisor_profiles_api.conf /etc/supervisor/conf.d/profiles_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart profiles_api

# Configure nginx
cp $PROJECT_BASE_PATH/deploy/nginx_profiles_api.conf /etc/nginx/sites-available/profiles_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/profiles_api.conf /etc/nginx/sites-enabled/profiles_api.conf
systemctl restart nginx.service

echo "DONE! :)"


### ORIGINAL
###################################################################

# #!/usr/bin/env bash

# set -e

# # TODO: Set to URL of git repo.
# PROJECT_GIT_URL='https://github.com/LiliyaSemenenko/profiles-rest-api.git'

# # dir we'll store our project on a server
# PROJECT_BASE_PATH='/usr/local/apps/profiles-rest-api'

# # Set Ubuntu Language
# locale-gen en_GB.UTF-8

# # Install Python, SQLite and pip
# echo "Installing dependencies..."
# apt-get update
# # nginx: the webserver that is going to serve the static files and act as a proxy to our uWSGI service 
# # that is going to run in supervisor
# apt-get install -y python3-dev python3-venv sqlite python-pip supervisor nginx git

# # Create project directory
# mkdir -p $PROJECT_BASE_PATH
# git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# # Create virtual environment
# python3 -m venv $PROJECT_BASE_PATH/env

# # Install Python packages within requirments.txt file
# $PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt uwsgi==2.0.21

# # Run migrations
# $PROJECT_BASE_PATH/env/bin/python $PROJECT_BASE_PATH/manage.py migrate

# # Setup Supervisor to run our uwsgi process.
# # Supervisor: app on Linux that allows you to manage processes (Python)
# cp $PROJECT_BASE_PATH/deploy/supervisor_profiles_api.conf /etc/supervisor/conf.d/profiles_api.conf
# supervisorctl reread
# supervisorctl update
# supervisorctl restart profiles_api

# # Setup nginx to make our application accessible.
# # nginx web server is used to serve the static files
# cp $PROJECT_BASE_PATH/deploy/nginx_profiles_api.conf /etc/nginx/sites-available/profiles_api.conf
# rm /etc/nginx/sites-enabled/default
# ln -s /etc/nginx/sites-available/profiles_api.conf /etc/nginx/sites-enabled/profiles_api.conf
# systemctl restart nginx.service

# echo "DONE! :)"