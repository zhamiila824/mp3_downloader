# mp3_downloader
# Installation and run
From you command line:
```
$ git clone https://github.com/jamilya824/mp3_downloader.git
$ virtualenv venv -p python3
$ source venv/bin/activate
$ cd mp3_downloader
$ pip install -r requirements.txt
$ python manage.py runserver
```

Before running server:
1) create .env file in root directory with:
```
  SECRET_KEY=your_secret_key
  EMAIL_HOST_USER=your_email_username
  EMAIL_HOST_PASSWORD=your_email_password
```
2) make migrations:
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py sqlmigrate download 0001
```
3) create superuser(to see admin page):
```
$ python manage.py createsuperuser
```
4) in second terminal run the worker:
```
$ celery -A mp3_downloader worker -l info
```
