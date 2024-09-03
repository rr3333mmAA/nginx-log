# Nginx Log Parser

This is a simple python Django application that parses nginx log files from Google Drive url and displays the parsed data in a admin-panel.


## Run manually
```bash
pip install -r requirements.txt
```
```bash
python manage.py runserver
```

## Run via Docker
```bash
docker build --tag "nginx_log" .
```
```bash
docker run "nginx_log"
```


## Django commands
- Parse nginx log files from Google Drive url and store the parsed data in the database. Example:
```bash
python manage.py parse_log https://drive.google.com/file/d/18Ss9afYL8xTeyVd0ZTfFX9dqja4pBGVp/view
```


## Database
The application uses sqlite3 database. The database is created automatically when the application is run for the first time. The database is stored in the file `db.sqlite3`.