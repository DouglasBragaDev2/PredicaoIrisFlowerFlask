# [Predição Iris Flower in Python Flask](#)

Projeto de predição com Iris Flower com Front end em Flask

<br />
<br />

![Flask Dashboard Argon - Open-Source Flask Boilerplate.](https://github.com/DouglasBragaDev2/PredicaoIrisFlowerFlask/blob/master/static/assets/img/imagen/screen.png)

<br />

## Build from sources

```bash
$ # Get the code
$ git clone https://github.com/DouglasBragaDev2/PredicaoIrisFlowerFlask.git
$ cd PredicaoIrisFlowerFlask
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv --no-site-packages env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv --no-site-packages env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Database
$ pip3 install -r requirements.txt
$
$ # OR with PostgreSQL connector
$ # pip install -r requirements-pgsql.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
