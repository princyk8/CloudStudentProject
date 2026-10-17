
#!/usr/bin/env bash
set -o errexit

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install gunicorn
python -m gunicorn --version

python manage.py collectstatic --noinput
python manage.py migrate
